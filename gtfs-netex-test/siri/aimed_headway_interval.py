from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AimedHeadwayInterval:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: XmlDuration = field(
        metadata={
            "required": True,
        }
    )
