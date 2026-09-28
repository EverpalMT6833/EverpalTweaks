import re

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'r') as f:
    content = f.read()

# Replace keyboard key colors
content = content.replace('<key-alphanumeric color="#000000"', '<key-alphanumeric color="#111111"')
content = content.replace('<key-other color="#000000"', '<key-other color="#151515"')

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'w') as f:
    f.write(content)

print("Keyboard key colors patched.")
