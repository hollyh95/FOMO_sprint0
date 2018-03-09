# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519771785.063903
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/manager/templates/edit.html'
_template_uri = 'edit.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content_top']


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
        form = context.get('form', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        __M_writer(str( form ))
        __M_writer("\n\n<script>\n    $(document).ready(function() {\n    // disable type selector\n    //$('#id_type').prop('disabled', true);\n    if ($('#id_type').val() == 'BulkProduct') {\n        $('#id_itemID').closest('p').hide();\n        $('#id_maxRental').closest('p').hide();\n        $('#id_retireDate').closest('p').hide();\n    } else if ($('#id_type').val() == 'IndividualProduct') {\n        $('#id_quantity').closest('p').hide();\n        $('#id_reorder_trigger').closest('p').hide();\n        $('#id_reorder_quantity').closest('p').hide();\n        $('#id_maxRental').closest('p').hide();\n        $('#id_retireDate').closest('p').hide();\n    } else if ($('#id_type').val() == 'RentalProduct') {\n        $('#id_quantity').closest('p').hide();\n        $('#id_reorder_trigger').closest('p').hide();\n        $('#id_reorder_quantity').closest('p').hide();\n    }\n});\n</script>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/manager/templates/edit.html", "uri": "edit.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 29, "47": 3, "54": 3, "55": 5, "56": 5, "62": 56}}
__M_END_METADATA
"""
