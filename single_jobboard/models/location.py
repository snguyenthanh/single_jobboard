from attr import attrs, attrib


@attrs(kw_only=True, slots=True, auto_attribs=True)
class Location:
    city: str = None
    country: str = None
