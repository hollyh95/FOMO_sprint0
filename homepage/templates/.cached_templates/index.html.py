# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520282962.764886
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content_top', 'content', 'content_footer']


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
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_footer():
            return render_content_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_footer'):
            context['self'].content_footer(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row text-center">\n    <div class="col-md-6">\n        <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/721582_1.jpg" alt="Cat playing sax">\n    </div>\n    <div class="col-md-6">\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <br>\n        <a href="/account/signup/" class="btn btn-primary">Sign up now</a>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n <h1>Welcome to FOMO!</h1>\n<h2>Here you can get everything you need to do stuff with music</h2>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_footer():
            return render_content_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "40": 1, "45": 24, "50": 29, "55": 33, "61": 3, "68": 3, "69": 6, "70": 6, "76": 26, "82": 26, "88": 32, "94": 32, "100": 94}}
__M_END_METADATA
"""
