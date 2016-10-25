
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *


def preformat(text):
    return text

def escape(text):
    return text.replace("\\", "\\\\").replace("{", "\{").replace("}", "\}")

def italic(string):
    return "\\textit{" + escape(string) + "}"

def oblique(string):
    return "\\textit{" + escape(string) + "}"

def bold(string):
    return "\\textbf{" + escape(string) + "}"

Light = str

def underline(string):
    return "\\underline{" + escape(string) + "}"

def superscript(string):
    return "\\textsuperscript{" + escape(string) + "}"

def subscript(string):
    return "\\textsubscript{" + escape(string) + "}"

def smallcaps(string):
    return "\\textsc{" + escape(string) + "}"
