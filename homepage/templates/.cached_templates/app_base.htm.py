# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516775089.311813
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['navbar']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        __M_writer('\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/index/"/>Home</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'about' else ''))
        __M_writer('"><a href="/about/"</>About</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'contact' else ''))
        __M_writer('"><a href="/contact/">Contact</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'faq' else ''))
        __M_writer('"><a href="/faq/">FAQ</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'terms' else ''))
        __M_writer('"><a href="/terms/">Terms and Conditions</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp_router_page == 'sections' else ''))
        __M_writer('"><a href="/sections/">Sections</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 12, "47": 5, "54": 5, "55": 6, "56": 6, "57": 7, "58": 7, "59": 8, "60": 8, "61": 9, "62": 9, "63": 10, "64": 10, "65": 11, "66": 11, "72": 66}}
__M_END_METADATA
"""
