from dataclasses import dataclass
from ..elements import Element


@dataclass
class Link(Element):
    text: str
    href: str

    def to_markdown(self):
        return f"[{self.text}]({self.href})"
