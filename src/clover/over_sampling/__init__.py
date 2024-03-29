"""This module includes classes for clustering-based oversampling.

A general class for clustering-based oversampling as well as specific
clustering-based oversamplers are provided.
"""

from importlib.util import find_spec

from ._cluster import (
    ClusterOverSampler,
    clone_modify,
    extract_inter_data,
    extract_intra_data,
    generate_in_cluster,
    modify_nn,
)
from ._kmeans_smote import KMeansSMOTE

__all__: list[str] = [
    'ClusterOverSampler',
    'KMeansSMOTE',
    'modify_nn',
    'clone_modify',
    'extract_inter_data',
    'extract_intra_data',
    'generate_in_cluster',
]

if find_spec('somoclu') is not None:
    from ._gsomo import GeometricSOMO  # noqa: F401
    from ._somo import SOMO  # noqa: F401

    __all__.append('SOMO')
    __all__.append('GeometricSOMO')
