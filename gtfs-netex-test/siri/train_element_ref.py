from dataclasses import dataclass

from .train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainElementRef(TrainElementRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
