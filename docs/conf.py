"""Sphinx configuration."""
project = "My Github Toolbox"
author = "Mario Scalas"
copyright = "2023, Mario Scalas"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
