# -*- coding: utf-8 -*-

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['rst2pdf.pdfbuilder']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'german test'
copyright = u'2010, Werner'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1'
# The full version, including alpha/beta/rc tags.
release = '1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'de'


# -- Options for PDF output ----------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
pdf_documents = [('index', u'twcb-de', u'Das Weinkellerbuch', u'Werner F Bruhin')]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'sphinx-mine']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed = True

# Language to be used for hyphenation support
pdf_language = "de_DE"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 1

# If false, no coverpage is generated.
pdf_use_coverpage = True

pdf_default_dpi = 300

pdf_page_template = 'customPage'

pdf_invariant = True
pdf_real_footnotes = True
