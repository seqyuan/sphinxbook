# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sys
from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE.parent), str(HERE / "extensions")]


# -- Project information -----------------------------------------------------
# The master toctree document.
master_doc = "index"

project = 'papers'
copyright = ''
author = ''


exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"
pygments_dark_style = "native"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# html_show_sourcelink = True
html_theme = "furo"

# Set link name generated in the top bar.
html_title = "bioinfo documentation"
html_logo = "logo.png"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#003262",
        "color-brand-content": "#003262",
        "admonition-font-size": "var(--font-size-normal)",
        "admonition-title-font-size": "var(--font-size-normal)",
        "code-font-size": "var(--font-size--small)",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/annoroad/anno_papaer",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/override.css", "css/sphinx_gallery.css"]
html_show_sphinx = False
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "nbsphinx_link",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",  # needs to be after napoleon
    "sphinx.ext.autosummary",
    *[p.stem for p in (HERE / "extensions").glob("*.py")],
    "sphinx_copybutton",
    "sphinx_gallery.load_style",
    #"sphinx_remove_toctrees",
    "sphinx_design",
    "sphinx_tags"
    #"recommonmark",
    #"sphinxext.opengraph",
    #"autoapi.extension",
]

tags_create_tags = True
tags_create_badges = True
# tags_output_dir = "_tags"  # default
tags_overview_title = ""  # default: "Tags overview"
tags_extension = ["md", "rst", "ipynb"]  # default: ["rst"]
tags_intro_text = "Tags in this page:"  # default: "Tags:"
tags_page_title = "All papers"  # default: "My tags:"
tags_page_header = "Pages with this tag"  # default: "With this tag"
tags_index_head = "Tags in this site"  # default: "Tags"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
nbsphinx_execute = "never"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".


nbsphinx_thumbnails_df = pd.read_table('gallary-fig.txt', header=None, index_col=None)
nbsphinx_thumbnails = {row[0]:row[1] for i,row in nbsphinx_thumbnails_df.iterrows()}

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
'preamble': r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
}
