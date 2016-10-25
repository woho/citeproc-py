
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

def bibliography_wrap(text):
    return '\\startitemize\n' + text + '\stopitemize'

def citation_format(key, text):
    if key is not None:
        return '\\goto{' + text + '}[bib:' + key + ']'
    else:
        return text

def bibliography_entry_format(key, first_part, second_part):
    if key is not None and first_part is not None:
        first_part = '\\reference[bib:' + key + ']{' + first_part.strip() + '} ' + \
            first_part.strip()
    elif key is not None:
        second_part = '\\reference[bib:' + key + ']{' + second_part + '}' + \
            second_part
    if first_part is None:
        return '	\\item ' + second_part + '\n'
    else:
        return '	\\sym{' + first_part.strip() + '} ' + second_part + '\n'

def preformat(text):
    return text

def escape(text):
    return text.replace("\\", "\\\\").replace("{", "\{").replace("}", "\}")

def italic(string):
    return "{\\it " + escape(string) + "}"

def oblique(string):
    return "{\\sl " + escape(string) + "}"

def bold(string):
    return "{\\bf " + escape(string) + "}"

light = str

def underline(string):
    return "{\\underbar " + escape(string) + "}"

def superscript(string):
    return "\\high{" + escape(string) + "}"

def subscript(string):
    return "\\low{" + escape(string) + "}"

def smallcaps(string):
    return "{\\sc " + escape(string) + "}"
