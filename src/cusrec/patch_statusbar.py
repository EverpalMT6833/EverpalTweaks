import re

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'r') as f:
    content = f.read()

# Make the status bar background totally transparent since the header is already a nice dark #050505
content = content.replace('<fill color="#00000030">', '<fill color="#00000000">')

# Also in ui.xml, let's fix any remaining #111111 for keyboards to OLED black.
content = content.replace('color="#111111"', 'color="#000000"')
# Keyboard text from #5b5b5bff to #888888
content = content.replace('textcolor="#5b5b5bff"', 'textcolor="#888888"')

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'w') as f:
    f.write(content)

print("Statusbar and keyboard colors patched.")
