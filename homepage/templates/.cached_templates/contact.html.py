# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516817924.4533591
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<title>Contact</title>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<h1>Contact Us</h1>\n\n<form action="/contact/" method="POST">\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0')
        __M_writer(str( csrf_input ))
        __M_writer('\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0<br>\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Name:<input class="form-control" type="text" name="name">\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0<br>\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Message:<textarea class="form-control" name="message"></textarea>\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0<br>\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0<input class="btn btn-primary" type="submit" value="Submit">\n\xa0\xa0\xa0\xa0</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 19, "47": 5, "54": 5, "55": 10, "56": 10, "62": 56}}
__M_END_METADATA
"""
