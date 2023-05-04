"""Base class for all {{ cookiecutter.plugin_name|lower }} distributions."""

from metasynth.distribution.base import BaseDistribution


class Base{{ cookiecutter.__plugin_camel }}(BaseDistribution):
    """{{cookiecutter.plugin_name}} class to set privacy and provenance of distributions."""
    privacy = "{{ cookiecutter.privacy }}"
    provenance = "{{ cookiecutter.__package_name }}"
