"""{{ cookiecutter.plugin_name }} classes for categorical variables."""

import polars as pl

from metasyn.distribution.discrete import DiscreteUniformDistribution
from metasyn.distribution.discrete import PoissonDistribution
from metasyn.distribution.discrete import UniqueKeyDistribution
from metasyn.distribution.discrete import DiscreteTruncatedNormalDistribution
from metasyn.distribution.discrete import DiscreteNormalDistribution

{{ cookiecutter.__metadist_import }}


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}UniqueKey(UniqueKeyDistribution):
#     """UniqueKey distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DiscreteUniform(DiscreteUniformDistribution):
#     """DiscreteUniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Poisson(PoissonDistribution):
#     """Poisson distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DiscreteTruncatedNormal(DiscreteTruncatedNormalDistribution):
#     """Discrete truncated normal distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")

# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DiscreteNormal(DiscreteNormalDistribution):
#     """Discrete normal distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")

