# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519709952.829747
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/manager/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
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
        def content():
            return render_content(context._locals(__M_locals))
        productList = context.get('productList', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
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
        __M_writer = context.writer()
        __M_writer('\n    <h1>Products</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        productList = context.get('productList', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n       <div class="wrapper animated fadeIn">\n    <a class=\'btn btn-primary\' href="/manager/create/">Create Product</a>\n    <br>\n    <br>\n    <table class="table table-striped">\n        <tr>\n            <th>Category</th>\n            <th>Name</th>\n            <th>Price</th>\n            <th>Description</th>\n            <th>Quantity</th>\n            <th></th>\n        </tr>\n')
        for product in productList:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(product.category.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(product.price))
            __M_writer('</td>\n                <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n')
            if product.__class__.__name__ == 'BulkProduct':
                __M_writer('                <td>')
                __M_writer(str(product.quantity))
                __M_writer('</td>\n')
            else:
                __M_writer('                <td>1</td>\n')
            __M_writer('                <td><a class=\'btn btn-primary\' href="/manager/edit/')
            __M_writer(str(product.id))
            __M_writer('">Edit</a>&nbsp;<a class=\'btn btn-danger\' href="/manager/delete/')
            __M_writer(str(product.id))
            __M_writer('">Delete</a></td>\n            </tr>\n')
        __M_writer('    </table>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 5, "48": 37, "54": 3, "60": 3, "66": 7, "73": 7, "74": 21, "75": 22, "76": 23, "77": 23, "78": 24, "79": 24, "80": 25, "81": 25, "82": 26, "83": 26, "84": 27, "85": 28, "86": 28, "87": 28, "88": 29, "89": 30, "90": 32, "91": 32, "92": 32, "93": 32, "94": 32, "95": 35, "101": 95}}
__M_END_METADATA
"""
