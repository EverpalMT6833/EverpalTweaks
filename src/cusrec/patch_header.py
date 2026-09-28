import re

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'r') as f:
    content = f.read()

new_header = """<fill color="#050505">
				<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>
			</fill>
			<fill color="%accent_color%">
				<placement x="0" y="252" w="%screen_width%" h="4"/>
			</fill>"""

content = re.sub(
    r'<fill color="%accent_color%">\s*<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\s*</fill>',
    new_header,
    content
)

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'w') as f:
    f.write(content)

print("Header patched.")
