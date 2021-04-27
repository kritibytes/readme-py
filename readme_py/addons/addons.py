from dataclasses import dataclass

@dataclass
class Link:
    text: str
    href: str

    def to_markdown(self):
        return f"[{self.text}]({self.href})"