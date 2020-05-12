from attr import attrs, attrib


@attrs(kw_only=True, slots=True, auto_attribs=True)
class Channel:
    name: str
    homepage: str
    config: dict = {}
