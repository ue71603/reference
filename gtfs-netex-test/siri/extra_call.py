from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ExtraCall:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
