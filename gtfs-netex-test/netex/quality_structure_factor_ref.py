from dataclasses import dataclass

from .quality_structure_factor_ref_structure import QualityStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorRef(QualityStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
