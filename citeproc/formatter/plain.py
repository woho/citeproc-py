
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

def bibliography_wrap(text):
    return text.strip()

def citation_format(key, text):
    return text

def bibliography_entry_format(key, first_part, second_part):
    if first_part is None:
        return second_part + '\n'
    else:
        return first_part.strip() + ' ' + second_part + '\n'

preformat = str
italic = str
oblique = str
bold = str
light = str
underline = str
superscript = str
subscript = str
smallcaps = str
