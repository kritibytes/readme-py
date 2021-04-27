#!/usr/bin/env python3
from readme_py import *
import os
os.chdir('./test')

license_section = LicenseSection("MIT","https://choosealicense.com/licenses/mit/")

readme = Readme(
    title="ReadmePY",
    description="Python library to generate perfect READMEs",
    sections=[
        license_section
    ]
)

generator(readme)