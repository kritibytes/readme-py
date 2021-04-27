from ..elements import Element
from typing import List, Any
from ..addons import Link
from ..markdown import header, br
from dataclasses import dataclass, field


class Section:
    title: str = ""
    inner: List[Element] = []
    header_size: int = 2

    def to_markdown(self):
        markdown_text: str = ""
        markdown_text += header(self.header_size, self.title) + br*2

        for el in self.inner:
            markdown_text += el.to_markdown() + br*2

        return markdown_text


class Readme:
    title: str = ""
    description: str = ""
    badges: List[Any] = []
    sections: List[Section] = []

    def __init__(self, title: str = "", description: str = "", sections: List[Section] = [], badges: List[Any] = []) -> None:
        self.title = title
        self.description = description
        self.badges = badges
        self.sections = sections

    def to_markdown(self):
        markdown_text: str = ""
        markdown_text += header(1, self.title) + br*2

        for section in self.sections:
            markdown_text += section.to_markdown()

        return markdown_text


class LicenseSection(Section):
    def __init__(self, license_type: str, license_link: str) -> None:
        self.title = "License"
        self.inner.append(Link(license_type, license_link))
