# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521520480.871212
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
        for p in splice:
            __M_writer('<a href="/catalog/details/')
            __M_writer(str( p.id ))
            __M_writer('">\n<li><div class=\'catalog-element\'><div class=\'catalog-title text-center\'>')
            __M_writer(str(p.name))
            __M_writer("</div>\n    <div class='catalog-price'>$")
            __M_writer(str(p.price))
            __M_writer('</div><img src="')
            __M_writer(str(p.image_url()))
            __M_writer('" /></div>\n</li>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.inner.html", "uri": "index.inner.html", "source_encoding": "utf-8", "line_map": {"18": 0, "24": 1, "25": 2, "26": 2, "27": 2, "28": 3, "29": 3, "30": 4, "31": 4, "32": 4, "33": 4, "39": 33}}
__M_END_METADATA
"""
