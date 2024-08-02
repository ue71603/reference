from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Order:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: int = field(
        metadata={
            "required": True,
        }
    )
