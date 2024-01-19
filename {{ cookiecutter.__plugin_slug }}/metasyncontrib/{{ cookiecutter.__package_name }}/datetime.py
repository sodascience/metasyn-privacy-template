"""{{ cookiecutter.plugin_name }} classes for date/time/datetime distributions."""

from __future__ import annotations
import datetime as dt

import polars as pl

from metasyn.distribution.datetime import DateTimeUniformDistribution
from metasyn.distribution.datetime import TimeUniformDistribution
from metasyn.distribution.datetime import DateUniformDistribution

{{ cookiecutter.__metadist_import }}


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DateTimeUniform(DateTimeDistributionUniform):
#     """DateTimeUniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}TimeUniform(TimeUniformDistribution):
#     """TimeUniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DateUniform(DateUniformDistribution):
#     """DateUniform distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
