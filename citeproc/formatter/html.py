
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

try:
    from html import escape
except ImportError:
    from cgi import escape

def bibliography_wrap(text):
    return '<div class="csl-bib-body">\n' + text + '\n</div>'

def citation_format(key, text):
    if key is not None:
        return '<a href="#ref:' + key + '">' + text + '</a>'
    else:
        return text

def bibliography_entry_format(key, first_part, second_part):
    if key is not None:
        anchor = ' id="ref:' + key + '"'
    else:
        anchor = ''
    if first_part is not None:
        return ' <div' + anchor + ' class="csl-entry">\n   <div class="csl-left-margin">' + \
            first_part.strip() + '</div>\n   <div class="csl-right-margin">\n    ' + \
            second_part.strip() + '  \n   </div>  \n </div>'
    else:
        return ' <div' + anchor + ' class="csl-entry">\n   ' + second_part + '\n </div>'

def preformat(text):
    return escape(str(text), quote=False)

def italic(text):
    return '<i>' + text + '</i>'

def oblique(text):
    return italic(text)

def bold(text):
    return '<b>' + text + '</b>'

def light(text):
    return '<l>' + text + '</l>'

def light(text):
    return '<u>' + text + '</u>'

def superscript(text):
    return '<sup>' + text + '</sup>'

def subscript(text):
    return '<sub>' + text + '</sub>'

def smallcaps(text):
    return '<span style="font-variant:small-caps;">' + text + '</span>'
