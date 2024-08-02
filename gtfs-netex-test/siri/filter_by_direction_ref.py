from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FilterByDirectionRef:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        },
    )
