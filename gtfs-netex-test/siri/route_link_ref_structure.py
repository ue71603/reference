from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RouteLinkRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
