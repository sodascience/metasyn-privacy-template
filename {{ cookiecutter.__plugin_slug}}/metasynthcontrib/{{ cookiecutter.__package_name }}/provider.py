"""Module contains distribution tree for {{ cookiecutter.plugin_name|lower }}."""

from __future__ import annotations
from metasynth.provider import BaseDistributionProvider
from metasynth.distribution.base import BaseDistribution


class {{ cookiecutter.__plugin_camel }}Provider(BaseDistributionProvider):
    """Distribution tree that contains safe distributions using {{ cookiecutter.plugin_name|lower }}.
    """

    @property
    def name(self):
        return "{{cookiecutter.__package_name}}"

    @property
    def version(self):
        return "1.0"

    @property
    def distributions(self) -> list[type[BaseDistribution]]:
        return [
            # Add your distributions here.
        ]
