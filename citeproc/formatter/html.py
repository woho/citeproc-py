
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

class TagWrapper(str):
    tag = None
    attributes = None

    @classmethod
    def _wrap(cls, text):
        if cls.attributes:
            attrib = ' ' + ' '.join(['{}="{}"'.format(key, value)
                                     for key, value in cls.attributes.items()])
        else:
            attrib = ''
        return '<{tag}{attrib}>{text}</{tag}>'.format(tag=cls.tag,
                                                      attrib=attrib,text=text)

    def __new__(cls, text):
        return super(TagWrapper, cls).__new__(cls, cls._wrap(text))


class Italic(TagWrapper):
    tag = 'i'


class Oblique(Italic):
    pass


class Bold(TagWrapper):
    tag = 'b'


class Light(TagWrapper):
    tag = 'l'


class Underline(TagWrapper):
    tag = 'u'


class Superscript(TagWrapper):
    tag = 'sup'


class Subscript(TagWrapper):
    tag = 'sub'


class SmallCaps(TagWrapper):
    tag = 'span'
    attributes = {'style': 'font-variant:small-caps;'}
