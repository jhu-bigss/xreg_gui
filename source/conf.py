# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'BIGSS xreg GUI Documentation'
copyright = '2024, BIGSS Lab'
author = 'Ping-Cheng Ku'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx_copybutton'
    'sphinx_rtd_theme',

]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'navigation_depth': 4
}
html_static_path = ['_static']

html_use_index = True
html_show_sourcelink = True
html_show_sphinx = True
html_baseurl = 'https://jhu-bigss.github.io/xreg_gui/'


html_secnumber_suffix = ' '
numfig = True
