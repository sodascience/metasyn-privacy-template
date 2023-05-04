"""{{ cookiecutter.plugin_name }} classes for string variables."""

from metasynth.distribution.faker import FakerDistribution
from metasynth.distribution.regex import RegexDistribution, UniqueRegexDistribution

from metasynthcontrib.{{ cookiecutter.__package_name }}.base import Base{{ cookiecutter.__plugin_camel }}


# class {{ cookiecutter.__plugin_camel }}Faker(Base{{ cookiecutter.__plugin_camel }}, FakerDistribution):
#     """Faker distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}Regex(Base{{ cookiecutter.__plugin_camel }}, RegexDistribution):
#     """Regex distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# class {{ cookiecutter.__plugin_camel }}UniqueRegex(Base{{ cookiecutter.__plugin_camel }}, UniqueRegexDistribution):
#     """UniqueRegex distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")

