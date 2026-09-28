import re

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'r') as f:
    content = f.read()

new_tabs_bg = """<fill color="#050505">
				<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>
			</fill>
			<fill color="%accent_color%">
				<placement x="0" y="398" w="%screen_width%" h="2"/>
			</fill>"""

# row1_y is 256. tab_height is 96. 256 + 96 = 352. Wait! row1_y is 256 but in ui.xml:
# <variable name="row1_y" value="256"/>
# So y="256" + 96 = 352. So the border should be at 350.

new_tabs_bg_corrected = """<fill color="#08080A">
				<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>
			</fill>
			<fill color="%accent_color%">
				<placement x="0" y="350" w="%screen_width%" h="2"/>
			</fill>"""

# Actually, the original is:
# <fill color="%accent_color%">
#     <placement x="0" y="row1_y" w="%screen_width%" h="tab_height"/>
# </fill>

content = re.sub(
    r'<fill color="%accent_color%">\s*<placement x="0" y="row1_y" w="%screen_width%" h="tab_height"/>\s*</fill>',
    new_tabs_bg_corrected,
    content
)

with open('/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/ui.xml', 'w') as f:
    f.write(content)

print("Tabs patched.")
