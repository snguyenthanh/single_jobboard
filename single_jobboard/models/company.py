from attr import attrs, attrib


@attrs(kw_only=True, slots=True, auto_attribs=True)
class Company:
    name: str
    rating: float = None
    logo: str = None
