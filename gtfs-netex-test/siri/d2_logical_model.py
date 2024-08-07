from dataclasses import dataclass

from .d2_logical_model_1 import D2LogicalModel1

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class D2LogicalModel(D2LogicalModel1):
    class Meta:
        name = "d2LogicalModel"
        namespace = "http://datex2.eu/schema/2_0RC1/2_0"
