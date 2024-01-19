"""{{ cookiecutter.plugin_name }} classes for continuous variables."""

import polars as pl

from metasyn.distribution.continuous import UniformDistribution
from metasyn.distribution.continuous import NormalDistribution, LogNormalDistribution
from metasyn.distribution.continuous import ExponentialDistribution
from metasyn.distribution.continuous import TruncatedNormalDistribution

{{ cookiecutter.__metadist_import }}


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Uniform(UniformDistribution):
#     """Uniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.__plugin_camel }}TruncatedNormal(Base{{ cookiecutter.__plugin_camel }}, TruncatedNormalDistribution):
#     """TruncatedNormal distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.__plugin_camel }}Normal(Base{{ cookiecutter.__plugin_camel }}, NormalDistribution):
#     """Normal distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.__plugin_camel }}LogNormal(Base{{ cookiecutter.__plugin_camel }}, LogNormalDistribution):
#     """LogNormal distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.__plugin_camel }}Exponential(Base{{ cookiecutter.__plugin_camel }}, ExponentialDistribution):
#     """Exponential distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
