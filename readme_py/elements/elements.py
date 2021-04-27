from dataclasses import dataclass
from typing import List

class Element:
    def to_markdown(self) -> str:
        return ""

@dataclass
class Link(Element):
    text: str
    href: str

    def to_markdown(self) -> str:
        return f"[{self.text}]({self.href})"

@dataclass
class Image(Element):
    alt: str
    src: str
    
    def to_markdown(self) -> str:
        return f"![{self.alt}]({self.src})"

class Li(Element):
    elements: List[Element] = []

    def __init__(self,elements: List[Element] = []) -> None:
        self.elements = elements

    def add(self,element: Element) -> None:
        self.elements.append(element)

    def to_markdown(self) -> str:
        return ""
        

class ULi(Li):
    def to_markdown(self) -> str:
        return "\n".join([f"-\t{el.to_markdown()}" for el in self.elements])

class OLi(Li):
    def to_markdown(self) -> str:
        return "\n".join([f"{i+1}.\t{self.elements[i].to_markdown()}" for i in range(len(self.elements))])

@dataclass
class P(Element):
    text: str = ""
    
    def to_markdown(self) -> str:
        return self.text
    
@dataclass
class Header(Element):
    size:int
    text:str
    
    def to_markdown(self) -> str:
        return f"{'#'*self.size} {self.text}"
    
class Br(Element):
    def to_markdown(self) -> str:
        return "\n"