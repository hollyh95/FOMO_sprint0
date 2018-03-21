# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520913254.36625
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/app_base.htm'
_template_uri = '/homepage/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
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
        

        __M_writer('\n')
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
        __M_writer(str('active' if request.dmp.page == 'index' else ''))
        __M_writer('"><a href="/index/"/>Home</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'about' else ''))
        __M_writer('"><a href="/about/"</>About</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'contact' else ''))
        __M_writer('"><a href="/contact/">Contact</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'faq' else ''))
        __M_writer('"><a href="/faq/">FAQ</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'terms' else ''))
        __M_writer('"><a href="/terms/">Terms and Conditions</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'sections' else ''))
        __M_writer('"><a href="/sections/">Sections</a></li>\n<li class="nav-item ')
        __M_writer(str('active' if request.dmp.page == 'sections' else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\n\n')
        if request.user.is_authenticated:
            __M_writer('<li class="nav-item ')
            __M_writer(str('active' if request.dmp.page == 'index' else ''))
            __M_writer('"><a href="/manager/index/">Product</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/app_base.htm", "uri": "/homepage/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 17, "48": 5, "55": 5, "56": 6, "57": 6, "58": 7, "59": 7, "60": 8, "61": 8, "62": 9, "63": 9, "64": 10, "65": 10, "66": 11, "67": 11, "68": 12, "69": 12, "70": 14, "71": 15, "72": 15, "73": 15, "79": 73}}
__M_END_METADATA
"""
