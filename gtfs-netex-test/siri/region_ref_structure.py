from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class RegionRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
