from typing import List, Any
from ..addons import Link

class Section:
    title: str
    inner: List[Any]


class Readme:
    title: str
    description: str
    badges: List
    sections: List[Section]


class LicenseSection(Section):
    def __init__(self, license_type: str, license_link: str) -> None:
        self.title = "License"
        self.inner.append(Link(license_type,license_link))
