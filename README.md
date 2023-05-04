# MetaSynth plugin template 

Template for creating plugins for the MetaSynth library. Follow these steps to create a new plugin from this template:

- Install cookiecutter: `pip install cookiecutter` on the command line.
- Use the template: `cookiecutter https://github.com/sodascience/metasynth-plugin-template`

The template is now ready to use. To finish your plugin, edit the following modules:

- `metasynthcontrib.{plugin_name}.privacy`: If you are writing a new privacy plugin, edit the `__init__` and `to_dict` methods. Otherwise delete this file.
- `metasynthcontrib.{plugin_name}.base`: Change the `privacy` class variable if necessary.
- `metasynthcontrib.{plugin_name}.categorical/continuous/datetime/string/discrete`: Implement distributions here.
- `metasynthcontrib.{plugin_name}.provider`: Add the newly implemented distributions.

Your plugin should now be ready to go. GitHub actions is part of the template, so after pushing your new plugin to GitHub it should automatically start testing your code.
