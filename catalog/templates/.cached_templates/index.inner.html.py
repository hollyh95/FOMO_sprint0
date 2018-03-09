# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520558410.9446669
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.inner.html'
_template_uri = 'index.inner.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        splice = context.get('splice', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<ul>\n')
        for p in splice:
            __M_writer('    <img src="')
            __M_writer(str(p.image_url()))
            __M_writer('" />\n\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.inner.html", "uri": "index.inner.html", "source_encoding": "utf-8", "line_map": {"18": 0, "24": 1, "25": 2, "26": 3, "27": 3, "28": 3, "29": 6, "35": 29}}
__M_END_METADATA
"""
