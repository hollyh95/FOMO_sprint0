# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516774558.000448
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        __M_writer = context.writer()
        __M_writer('\n\n<title>FAQ</title>\n\n')
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
        __M_writer = context.writer()
        __M_writer('\n<h1>Frequently Asked Questions</h1>\n<p>\n    <ul>\n    <li>How do I find my Windows product key?</li>\n    <li>HMy Windows 7 product key won\'t verify. What\'s the problem?</li>\n    <li>HI bought Windows 7 through a website. After talking to the merchant, I was told I had a "system builder" product key. Why doesn\'t that work?</li>\n    <li>HI purchased my copy of Windows through a university. Can I download it here?</li>\n    <li>HI\'m running a Mac and get an error message when I click Download Tool Now. What\'s wrong?</li>\n    <li>HWindows came pre-installed on my device, can I use media from this site to download and install?</li>\n</ul>\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "40": 17, "46": 5, "52": 5, "58": 52}}
__M_END_METADATA
"""
