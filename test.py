#!/usr/bin/env python3
from readme_py import *
import os
os.chdir('./test')

AboutMeText = P(f"""\
Hello. I am {bold('Yunis Huseynzade')} from {italic(bold('Azerbaijan'))}.{br}
I am {code('Python Developer')}.""")

class AboutMe(Section):
    title = "About Me"
    inner = [
        AboutMeText,
        Header(3,"My Projects"),
        P("I have some open-source libraries:"),
        ULi([
            Link('Python Script Manager','https://github.com/yunisdev/python-script-manager'),
            Link('num2azerbaijani','https://github.com/yunisdev/num2azerbaijani'),
            Link('AjaxSimpler','https://github.com/yunisdev/AjaxSimpler')
        ]),
        Header(3,'My Education'),
        OLi([
            P('School no. 309'),
            P('Pragmatech Education and Development Center')
        ])
    ]

license_section = LicenseSection("MIT","https://choosealicense.com/licenses/mit/")

readme = Readme(
    title="ReadmePY",
    description="Python library to generate perfect READMEs",
    sections=[
        AboutMe(),
        license_section
    ]
)

generator(readme)