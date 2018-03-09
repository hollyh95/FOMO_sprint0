# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520576991.242115
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content_top', 'content_left', 'content']


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
        selected = context.get('selected', UNDEFINED)
        maxPages = context.get('maxPages', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_top():
            return render_content_top(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        clist = context.get('clist', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        selected = context.get('selected', UNDEFINED)
        def content_top():
            return render_content_top(context)
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


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content_left():
            return render_content_left(context)
        clist = context.get('clist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <div>\n    <ul class=\'list-group\'>\n        <li><a class="list-group-item ')
        __M_writer(str( 'active' if request.dmp.urlparams[0] == '' else ''))
        __M_writer('" href="/catalog/index/">All Categories</a></li>\n')
        for category in clist:
            if request.dmp.urlparams[0] == '${category.id}':
                __M_writer('            <li><a class="list-group-item active" href="/catalog/index/')
                __M_writer(str( category.id ))
                __M_writer('">')
                __M_writer(str( category.name ))
                __M_writer('</a></li>\n')
            else:
                __M_writer('            <li><a class="list-group-item" href="/catalog/index/')
                __M_writer(str( category.id ))
                __M_writer('">')
                __M_writer(str( category.name ))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n   </div>\n')
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
        __M_writer('</span> <a id="getNextPage"><i class="fa fa-arrow-right"></i></a></div>\n        <div class="wrapper">\n        <ul id="products">\n\n        </ul>\n    </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "45": 2, "50": 12, "55": 27, "60": 38, "66": 4, "73": 4, "74": 6, "75": 7, "76": 8, "77": 9, "78": 9, "79": 9, "80": 11, "86": 14, "94": 14, "95": 17, "96": 17, "97": 18, "98": 19, "99": 20, "100": 20, "101": 20, "102": 20, "103": 20, "104": 21, "105": 22, "106": 22, "107": 22, "108": 22, "109": 22, "110": 25, "116": 29, "123": 29, "124": 31, "125": 31, "131": 125}}
__M_END_METADATA
"""
