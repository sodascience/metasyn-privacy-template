"""{{ cookiecutter.plugin_name }} privacy class."""

from metasyn.privacy import BasePrivacy


class {{ cookiecutter.__plugin_camel }}Privacy(BasePrivacy):
    """{{ cookiecutter.plugin_name }} privacy class.
    """
    name = "{{ cookiecutter.__package_name }}"

    def __init__(self):  # Add to the arguments/parameters here.
        raise NotImplementedError("Privacy class not implemented.")

    def to_dict(self) -> dict:
        raise NotImplementedError("Privacy class unfinished!")
        return {
            "type": self.name,
            "parameters": {
                "parameter_name": self.parameter_value
            }
        }
