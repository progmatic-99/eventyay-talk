#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath('../src'))

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pretalx.settings")
django.setup()

# PyEnchant is required for spellchecking only, and somewhat bothersome
# to install on some systems.
try:
    import enchant
    HAS_PYENCHANT = True
except:
    HAS_PYENCHANT = False

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib_django',
    'releases',
]
if HAS_PYENCHANT:
    extensions.append('sphinxcontrib.spelling')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = 'pretalx'
copyright = '2017-{}, Tobias Kunze'.format(date.today().year)
author = 'Tobias Kunze'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# from pretalx import __version__  # TODO
# The full version, including alpha/beta/rc tags.
from pretalx import __version__
version = '.'.join(__version__.split('.')[:2])
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    '_static',
    os.path.abspath('../src/pretalx/static/vendored/forkawesome/fonts/'),
]
html_additional_pages = {
    'index': 'index.html'
}
html_theme = 'pretalx_theme'
html_theme_path = [os.path.abspath('_themes')]
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
html_logo = 'images/logo.svg'
html_favicon = os.path.abspath('../src/pretalx/static/common/img/favicon-32x32.png')
# html_link_suffix = ''

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pretalxdoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

linkcheck_ignore = [
    'https://pretalx.yourdomain.com',
    'http://localhost',
    'http://127.0.0.1',
    r'https://github.com/pretalx/pretalx/issues/\d+',  # The release notes are auto generated and contain a LOT of issue links
]

# Configure releases
releases_release_uri = 'https://pypi.org/project/pretalx/%s/'
releases_issue_uri = 'https://github.com/pretalx/pretalx/issues/%s'
releases_unstable_prehistory = True

# GitHub integration
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "pretalx", # Username
    "github_repo": "pretalx", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/doc/", # Path in the checkout to the docs root
}

# Autodoc options
autodoc_member_order = 'groupwise'

# Spelling options
if HAS_PYENCHANT:
    spelling_lang = 'en_GB'
    spelling_word_list_filename='spelling_wordlist.txt'
    spelling_show_suggestions=True
