# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521485842.978504
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content_top', 'content']


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
        maxPages = context.get('maxPages', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        selected = context.get('selected', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        selected = context.get('selected', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1 class="text-center">\n')
        if selected is None:
            __M_writer('            All Categories\n')
        else:
            __M_writer('            ')
            __M_writer(str(selected.name))
            __M_writer('\n')
        __M_writer('    </h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        maxPages = context.get('maxPages', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="pagination">\n         <div class="row text-right"><a id="getLastPage"><i class="fa fa-arrow-left"></i></a> <span id=\'currentPage\'>1</span> of <span id=\'maxPages\'>')
        __M_writer(str(maxPages))
        __M_writer('</span> <a id="getNextPage"><i class="fa fa-arrow-right"></i></a></div>\n        <div class="wrapper">\n        <ul id="products">\n\n        </ul>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "41": 2, "46": 12, "51": 24, "57": 4, "64": 4, "65": 6, "66": 7, "67": 8, "68": 9, "69": 9, "70": 9, "71": 11, "77": 15, "84": 15, "85": 17, "86": 17, "92": 86}}
__M_END_METADATA
"""
