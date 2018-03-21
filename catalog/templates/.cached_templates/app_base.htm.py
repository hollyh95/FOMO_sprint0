# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521611146.39277
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content_left', 'content_right']


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
    return runtime._inherit_from(context, '/homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        active_id = context.get('active_id', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        lastFiveProds = context.get('lastFiveProds', UNDEFINED)
        request = context.get('request', UNDEFINED)
        clist = context.get('clist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        active_id = context.get('active_id', UNDEFINED)
        request = context.get('request', UNDEFINED)
        clist = context.get('clist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <div>\n    <ul class=\'list-group\'>\n        <li><a class="list-group-item ')
        __M_writer(str( 'active' if request.dmp.urlparams[0] == '' else ''))
        __M_writer('" href="/catalog/index/">All Products</a></li>\n')
        for category in clist:
            __M_writer('            <li><a class="list-group-item ')
            __M_writer(str( 'active' if category.id == active_id else ''))
            __M_writer('" href="/catalog/index/')
            __M_writer(str( category.id ))
            __M_writer('">')
            __M_writer(str( category.name ))
            __M_writer('</a></li>\n')
        __M_writer('    </ul>\n   </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lastFiveProds = context.get('lastFiveProds', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer("\n    <div class='text-center'>\n        <b>Recently Viewed</b>\n")
        for product in lastFiveProds:
            if product.images.all().first() is None:
                __M_writer('                <div class=\'recently-viewed-thumbnail\'>\n                    <a href="/catalog/details/')
                __M_writer(str(product.id))
                __M_writer('"><img src="')
                __M_writer(str(STATIC_URL))
                __M_writer('/catalog/media/products/notfound.jpg" alt="recently viewed thumbnail"></a>\n                </div>\n')
            else:
                __M_writer('                <div class=\'recently-viewed-thumbnail\'>\n                    <a href="/catalog/details/')
                __M_writer(str(product.id))
                __M_writer('"><img src="')
                __M_writer(str(STATIC_URL))
                __M_writer('/catalog/media/products/')
                __M_writer(str(product.images.all().first().filename))
                __M_writer('" alt="recently viewed thumbnail"></a>\n                </div>\n')
        __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 12, "53": 29, "59": 3, "68": 3, "69": 6, "70": 6, "71": 7, "72": 8, "73": 8, "74": 8, "75": 8, "76": 8, "77": 8, "78": 8, "79": 10, "85": 14, "93": 14, "94": 17, "95": 18, "96": 19, "97": 20, "98": 20, "99": 20, "100": 20, "101": 22, "102": 23, "103": 24, "104": 24, "105": 24, "106": 24, "107": 24, "108": 24, "109": 28, "115": 109}}
__M_END_METADATA
"""
