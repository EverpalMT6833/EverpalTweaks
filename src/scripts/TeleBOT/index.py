#!/usr/bin/env python3
import os
import sys
import time
import json
import threading
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
VERSION = "2"
CLAIM_LEASE = 120
STALE_AFTER = 30 * 60
BOT_TOKEN = os.environ.get("BOT_TOKEN")
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tg_bridge_state.json")
API = "https://api.telegram.org/bot" + BOT_TOKEN
BOT_ID = 0
pending = {}
seen_total = 0
confirmed = -1
BOT_USERNAME = ""
claimed_until = {}
lock = threading.Lock()
started_at = time.time()


def api(method, params=None, timeout=65):
    data = urllib.parse.urlencode(params or {}).encode()
    req = urllib.request.Request(API + "/" + method, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def save_state():
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump({"confirmed": confirmed}, f)
    os.replace(tmp, STATE_FILE)


def load_state():
    global confirmed
    try:
        with open(STATE_FILE) as f:
            confirmed = int(json.load(f).get("confirmed", -1))
    except (OSError, ValueError, KeyError):
        confirmed = -1


def mentions_bot(msg):
    want = ("@" + BOT_USERNAME).lower()
    for key in ("entities", "caption_entities"):
        for ent in msg.get(key) or []:
            if ent.get("type") != "mention":
                continue
            text = msg.get("text") or msg.get("caption") or ""
            start, length = ent.get("offset", 0), ent.get("length", 0)
            if text[start:start + length].lower() == want:
                return True
    return False


def replies_to_bot(msg):
    reply = msg.get("reply_to_message") or {}
    return (reply.get("from") or {}).get("id") == BOT_ID


def qualifies(msg):
    """Private: everything. Groups: only mentions of / replies to the bot."""
    ctype = msg.get("chat", {}).get("type")
    if ctype == "private":
        return True
    if ctype in ("group", "supergroup"):
        return mentions_bot(msg) or replies_to_bot(msg)
    return False


def sender_name(sender):
    return (sender.get("first_name", "") + " " + sender.get("last_name", "")).strip()


def poller():
    global confirmed, seen_total
    while True:
        try:
            with lock:
                offset = confirmed + 1
            params = {"timeout": "50",
                      "allowed_updates": json.dumps(["message"]),
                      "offset": str(offset)}
            res = api("getUpdates", params)
            if not res.get("ok"):
                print("getUpdates not ok:", res, flush=True)
                time.sleep(5)
                continue
            for upd in res.get("result", []):
                uid = upd["update_id"]
                msg = upd.get("message")
                if not msg or not qualifies(msg):
                    with lock:
                        confirmed = max(confirmed, uid)
                    continue
                sender = msg.get("from", {})
                if sender.get("is_bot"):
                    with lock:
                        confirmed = max(confirmed, uid)
                    continue
                text = msg.get("text") or msg.get("caption") or ""
                with lock:
                    if uid not in pending and uid > confirmed:
                        msg_date = msg.get("date") or time.time()
                        seen_total += 1
                        pending[uid] = {
                            "update_id": uid,
                            "chat_id": msg["chat"]["id"],
                            "chat_type": msg["chat"].get("type"),
                            "chat_title": msg["chat"].get("title", ""),
                            "message_id": msg["message_id"],
                            "date": msg_date,
                            "from_name": sender_name(sender),
                            "username": sender.get("username"),
                            "text": text,
                            "is_command": text.startswith("/"),
                            "stale": (time.time() - msg_date) > STALE_AFTER,
                        }
            save_state()
        except Exception as e:  # network blip: wait and retry, offset untouched
            print("poll error:", repr(e), flush=True)
            time.sleep(5)


def serve_messages():
    now = time.time()
    with lock:
        out = []
        for uid, m in pending.items():
            if claimed_until.get(uid, 0) > now:
                continue
            claimed_until[uid] = now + CLAIM_LEASE
            out.append(m)
        return out


def ack_ids(ids):
    global confirmed
    with lock:
        for i in ids:
            pending.pop(i, None)
            claimed_until.pop(i, None)
        if pending:
            confirmed = max(confirmed, min(pending) - 1)
        elif ids:
            confirmed = max(confirmed, max(ids))
    save_state()
    return {"acked": len(ids), "pending": len(pending), "confirmed": confirmed}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"  # close after each response; no chunked encoding
    server_version = "tg_bridge/2"

    def _send(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            with lock:
                self._send({"ok": True, "pending": len(pending),
                            "confirmed": confirmed,
                            "uptime_s": int(time.time() - started_at),
                            "seen_total": seen_total,
                            "version": VERSION})
        elif self.path == "/messages":
            self._send(serve_messages())
        else:
            self._send({"error": "not found"}, 404)

    def do_POST(self):
        if self.path == "/ack":
            try:
                length = int(self.headers.get("Content-Length", 0))
                ids = json.loads(self.rfile.read(length) or b"{}").get("ids", [])
                self._send(ack_ids([int(i) for i in ids]))
            except Exception as e:
                self._send({"error": repr(e)}, 400)
        else:
            self._send({"error": "not found"}, 404)

    def log_message(self, *a):
        pass  # keep the terminal clean


def main():
    global BOT_ID, BOT_USERNAME
    if "PASTE_BOT_TOKEN" in BOT_TOKEN:
        sys.exit("Edit index.py and paste the bot token into BOT_TOKEN first.")
    me = api("getMe", timeout=20)
    if not me.get("ok"):
        sys.exit("Bad bot token: %r" % (me,))
    BOT_ID = me["result"]["id"]
    BOT_USERNAME = me["result"]["username"]
    load_state()
    threading.Thread(target=poller, daemon=True).start()
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print("tg_bridge v2 up: bot @%s, port %d, confirmed offset %d"
          % (BOT_USERNAME, PORT, confirmed), flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
