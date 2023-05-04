"""{{ cookiecutter.plugin_name }} classes for categorical variables."""

import polars as pl

from metasynth.distribution.discrete import DiscreteUniformDistribution
from metasynth.distribution.discrete import PoissonDistribution
from metasynth.distribution.discrete import UniqueKeyDistribution

from metasynthcontrib.{{ cookiecutter.__package_name }}.base import Base{{ cookiecutter.__plugin_camel }}


# class {{ cookiecutter.__plugin_camel }}UniqueKey(Base{{ cookiecutter.__plugin_camel }}, UniqueKeyDistribution):
#     """UniqueKey distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}DiscreteUniform(Base{{ cookiecutter.__plugin_camel }}, DiscreteUniformDistribution):
#     """DiscreteUniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}Poisson(Base{{ cookiecutter.__plugin_camel }}, PoissonDistribution):
#     """Poisson distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
