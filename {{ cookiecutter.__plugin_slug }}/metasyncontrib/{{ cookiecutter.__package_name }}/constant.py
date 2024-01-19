from metasyn.distribution.constant import ConstantDistribution, DiscreteConstantDistribution
from metasyn.distribution.constant import StringConstantDistribution, TimeConstantDistribution
from metasyn.distribution.constant import DateConstantDistribution, DateTimeConstantDistribution

{{ cookiecutter.__metadist_import }}


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}Constant(ConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for continuous constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DiscreteConstant(DiscreteConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for discrete constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}StringConstant(StringConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for String constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")


# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}TimeConstant(TimeConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for Time constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")

# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DateConstant(DateConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for Date constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")

# {{ cookiecutter.__decorate }}
# class {{ cookiecutter.prefix }}DateTimeConstant(DateTimeConstantDistribution):
#     """{{cookiecutter.plugin_name}} implementation for DateTime constant distribution.
#     """
#
#     @classmethod
#     def _fit(cls, values: pl.Series, extra_argument=default_value):
#         raise NotImplementedError("This distribution is not implemented yet.")
