from dataclasses import dataclass, field
from typing import List

from .defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DurationContentStructure:
    duration_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "DurationText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
