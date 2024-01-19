"""{{ cookiecutter.plugin_name }} classes for categorical variables."""

import polars as pl

from metasyn.distribution.categorical import MultinoulliDistribution

{{ cookiecutter.__metadist_import }}

# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Multinoulli(MultinoulliDistribution):
#     """{{cookiecutter.plugin_name}} implementation for multinoulli distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
