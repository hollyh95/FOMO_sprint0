# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521525949.8954759
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/details.html'
_template_uri = 'details.html'
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
        mainImage = context.get('mainImage', UNDEFINED)
        price = context.get('price', UNDEFINED)
        imageList = context.get('imageList', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        quantity = context.get('quantity', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        description = context.get('description', UNDEFINED)
        name = context.get('name', UNDEFINED)
        productType = context.get('productType', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="name" class=\'text-center\'>\n        <h1>')
        __M_writer(str(name))
        __M_writer('</h1>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        mainImage = context.get('mainImage', UNDEFINED)
        price = context.get('price', UNDEFINED)
        imageList = context.get('imageList', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        quantity = context.get('quantity', UNDEFINED)
        def content():
            return render_content(context)
        description = context.get('description', UNDEFINED)
        productType = context.get('productType', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="details">\n        <div class="row">\n            <div class="col-md-2">\n')
        for pi in imageList:
            __M_writer('                    <div class="small-image-tile">\n                        <img id=\'')
            __M_writer(str(pi.filename))
            __M_writer('\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('/catalog/media/products/')
            __M_writer(str(pi.filename))
            __M_writer('" alt="thumbnail">\n                    </div>\n')
        __M_writer('            </div>\n            <div class="col-md-4">\n                <div class="main-image">\n                     <img class="main-image-img" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/catalog/media/products/')
        __M_writer(str(mainImage))
        __M_writer('" alt="main image">\n                </div>\n                <div>\n                    <p></p>\n                    <button class="btn btn-primary" id="butt">Buy Now</button>\n')
        if productType == 'BulkProduct':
            __M_writer('                        <p id="quantity">Quanity: ')
            __M_writer(str( quantity ))
            __M_writer('</p>\n')
        __M_writer('\n                </div>\n            </div>\n\n            <div class="col-md-4">\n                <div class="description">\n                    <b class="text-info">$')
        __M_writer(str( price ))
        __M_writer('</b>\n                    <p>')
        __M_writer(str( description ))
        __M_writer('</p>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/catalog/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 7, "56": 41, "62": 3, "69": 3, "70": 5, "71": 5, "77": 9, "90": 9, "91": 13, "92": 14, "93": 15, "94": 15, "95": 15, "96": 15, "97": 15, "98": 15, "99": 18, "100": 21, "101": 21, "102": 21, "103": 21, "104": 26, "105": 27, "106": 27, "107": 27, "108": 29, "109": 35, "110": 35, "111": 36, "112": 36, "118": 112}}
__M_END_METADATA
"""
