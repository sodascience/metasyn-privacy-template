"""{{ cookiecutter.plugin_name }} classes for date/time/datetime distributions."""

from __future__ import annotations
import datetime as dt

import polars as pl

from metasynth.distribution.datetime import UniformDateTimeDistribution
from metasynth.distribution.datetime import UniformTimeDistribution
from metasynth.distribution.datetime import UniformDateDistribution

from metasynthcontrib.{{ cookiecutter.__package_name }}.base import Base{{ cookiecutter.__plugin_camel }}


# class {{ cookiecutter.__plugin_camel }}UniformDateTime(Base{{ cookiecutter.__plugin_camel }}, UniformDateTimeDistribution):
#     """UniformDateTime distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}UniformTime(Base{{ cookiecutter.__plugin_camel }}, UniformTimeDistribution):
#     """UniformTime distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}UniformDate(Base{{ cookiecutter.__plugin_camel }}, UniformDateDistribution):
#     """UniformDate distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
