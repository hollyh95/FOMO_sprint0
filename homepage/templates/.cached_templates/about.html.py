# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516773231.806737
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\n\n<title>About</title>\n ')
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
        __M_writer("\n\n<h1>\n    About us\n</h1>\n<h2>\n    Return policy\n</h2>\n<p>All items must be accompanied by a valid receipt\n\nReturn Period\n<ol>\n          <li>3 days for serialized product subject to a 10% restocking fee</li>\n            <li>7 days for accessories</li>\n    </ol>\n\nMerchandise must be in like new condition and in complete original packaging\n\nNon-Returnable Items\n<ol>\n          <li>Reeds (unless sealed in original box)</li>\n         <li>Opened Software, DVDs and CDs</li>\n    <li>Recorders, Tin Whistles, Jaw Harps, Nose Flutes, Harmonicas, In Ear</li>\n    <li>Clearance Items, Red Tag Items, and Consignments Sales</li>\n    <li>Gift Cards</li>\n    <li>Repair Parts, Drum Heads or other items that have been installed</li>\n    <li>Shipping</li>\n    </ol>\n\nCancelled Special Orders and Layaway are subject to a 20% restocking fee\n\nRefunds will be given in the form of original payment or store credit\n<ol>\n    <li>Cash refunds over $50.00 will be in the form of a company check mailed to                the customer's address</li>\n    <li>Payments by check will be refunded in the form of a company check 14 days              after the original purchase mailed to the customer's home address</li>\n</ol>\nWarranties limited to those of the manufacturer\n\nGift purchases made from November 20th to December 24th will be accepted until January 6th\n\nSummerhays Music Center of Orem reserves the right to deny the return of any item for any reason</p>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "40": 46, "46": 4, "52": 4, "58": 52}}
__M_END_METADATA
"""
