"""{{ cookiecutter.plugin_name }} classes for string variables."""

from metasyn.distribution.faker import FakerDistribution, UniqueFakerDistribution
from metasyn.distribution.faker import FreeTextDistribution
from metasyn.distribution.regex import RegexDistribution, UniqueRegexDistribution

{{ cookiecutter.__metadist_import }}


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Faker(FakerDistribution):
#     """Faker distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}UniqueFaker(UniqueFakerDistribution):
#     """Unique faker distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}FreeText(FreeTextDistribution):
#     """Free Text distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Regex(RegexDistribution):
#     """Regex distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}UniqueRegex(UniqueRegexDistribution):
#     """UniqueRegex distribution implementation with {{ cookiecutter.plugin_name|lower }}."""
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
