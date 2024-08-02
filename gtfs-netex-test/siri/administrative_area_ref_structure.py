from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AdministrativeAreaRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
