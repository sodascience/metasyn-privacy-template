"""{{ cookiecutter.plugin_name }} classes for categorical variables."""

import polars as pl

from metasynth.distribution.categorical import MultinoulliDistribution
from metasynthcontrib.{{ cookiecutter.__package_name }}.base import Base{{ cookiecutter.__plugin_camel }}


# class {{ cookiecutter.__plugin_camel }}Multinoulli(Base{{ cookiecutter.__plugin_camel }}, MultinoulliDistribution):
#     """{{cookiecutter.plugin_name}} implementation for multinoulli distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
