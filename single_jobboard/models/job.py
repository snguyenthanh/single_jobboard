from typing import List
from attr import attrs, attrib

from .company import Company
from .channel import Channel
from .location import Location


@attrs(kw_only=True, slots=True, auto_attribs=True)
class JobSummary:
    position: str
    salary: str = None
    company: Company
    channel: Channel
    location: Location = None
    remote: bool = False
    job_type: str = None
    experience_level = None
    date_posted: str
    period: str = None
    url: str


@attrs(kw_only=True, slots=True, auto_attribs=True)
class Job:
    position: str
    description: str
    salary: str = None
    company: Company
    channel: Channel
    reviews: List[dict] = []
    benefits: List[dict] = []
    location: Location = None
    remote: bool = False
    job_type: str = None
    industry: str = None
    experience_level = None
    date_posted: str
    period: str
