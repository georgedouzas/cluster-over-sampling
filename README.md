[scikit-learn]: <http://scikit-learn.org/stable/>
[imbalanced-learn]: <http://imbalanced-learn.org/stable/>
[SOMO]: <https://www.sciencedirect.com/science/article/abs/pii/S0957417417302324>
[KMeans-SMOTE]: <https://www.sciencedirect.com/science/article/abs/pii/S0020025518304997>
[G-SOMO]: <https://www.sciencedirect.com/science/article/abs/pii/S095741742100662X>
[black badge]: <https://img.shields.io/badge/%20style-black-000000.svg>
[black]: <https://github.com/psf/black>
[docformatter badge]: <https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg>
[docformatter]: <https://github.com/PyCQA/docformatter>
[ruff badge]: <https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json>
[ruff]: <https://github.com/charliermarsh/ruff>
[mypy badge]: <http://www.mypy-lang.org/static/mypy_badge.svg>
[mypy]: <http://mypy-lang.org>
[mkdocs badge]: <https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat>
[mkdocs]: <https://squidfunk.github.io/mkdocs-material>
[version badge]: <https://img.shields.io/pypi/v/cluster-over-sampling.svg>
[pythonversion badge]: <https://img.shields.io/pypi/pyversions/cluster-over-sampling.svg>
[downloads badge]: <https://img.shields.io/pypi/dd/cluster-over-sampling>
[gitter]: <https://gitter.im/cluster-over-sampling/community>
[gitter badge]: <https://badges.gitter.im/join%20chat.svg>
[discussions]: <https://github.com/georgedouzas/cluster-over-sampling/discussions>
[discussions badge]: <https://img.shields.io/github/discussions/georgedouzas/cluster-over-sampling>
[ci]: <https://github.com/georgedouzas/cluster-over-sampling/actions?query=workflow>
[ci badge]: <https://github.com/georgedouzas/cluster-over-sampling/actions/workflows/ci.yml/badge.svg?branch=main>
[doc]: <https://github.com/georgedouzas/cluster-over-sampling/actions?query=workflow>
[doc badge]: <https://github.com/georgedouzas/cluster-over-sampling/actions/workflows/doc.yml/badge.svg?branch=main>

# cluster-over-sampling

[![ci][ci badge]][ci] [![doc][doc badge]][doc]

| Category          | Tools    |
| ------------------| -------- |
| **Development**   | [![black][black badge]][black] [![ruff][ruff badge]][ruff] [![mypy][mypy badge]][mypy] [![docformatter][docformatter badge]][docformatter] |
| **Package**       | ![version][version badge] ![pythonversion][pythonversion badge] ![downloads][downloads badge] |
| **Documentation** | [![mkdocs][mkdocs badge]][mkdocs]|
| **Communication** | [![gitter][gitter badge]][gitter] [![discussions][discussions badge]][discussions] |

## Introduction

A general interface for clustering based over-sampling algorithms.

## Installation

For user installation, `cluster-over-sampling` is currently available on the PyPi's repository, and you can
install it via `pip`:

```bash
pip install cluster-over-sampling
```

Development installation requires to clone the repository and then use [PDM](https://github.com/pdm-project/pdm) to install the
project as well as the main and development dependencies:

```bash
git clone https://github.com/georgedouzas/cluster-over-sampling.git
cd cluster-over-sampling
pdm install
```

SOM clusterer requires optional dependencies:

```bash
pip install cluster-over-sampling[som]
```

## Usage

All the classes included in `cluster-over-sampling` follow the [imbalanced-learn] API using the functionality of the base
oversampler. Using [scikit-learn] convention, the data are represented as follows:

- Input data `X`: 2D array-like or sparse matrices.
- Targets `y`: 1D array-like.

The clustering-based oversamplers implement a `fit` method to learn from `X` and `y`:

```python
clustering_based_oversampler.fit(X, y)
```

They also implement a `fit_resample` method to resample `X` and `y`:

```python
X_resampled, y_resampled = clustering_based_oversampler.fit_resample(X, y)
```

## References

If you use `cluster-over-sampling` in a scientific publication, we would appreciate citations to any of the following papers:

- [G. Douzas, F. Bacao, "Self-Organizing Map Oversampling (SOMO) for imbalanced data set learning", Expert Systems with
    Applications, vol. 82, pp. 40-52, 2017.][SOMO]
- [G. Douzas, F. Bacao, F. Last, "Improving imbalanced learning through a heuristic oversampling method based on k-means and
    SMOTE", Information Sciences, vol. 465, pp. 1-20, 2018.][KMeans-SMOTE]
- [G. Douzas, F. Bacao, F. Last, "G-SOMO: An oversampling approach based on self-organized maps and geometric SMOTE", Expert
    Systems with Applications, vol. 183,115230, 2021.][G-SOMO]
