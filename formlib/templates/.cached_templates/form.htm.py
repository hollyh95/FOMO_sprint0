# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518329674.350162
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/formlib/templates/form.htm'
_template_uri = 'form.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n<div class="form-container">\n    <form id="')
        __M_writer(str( form.form_id ))
        __M_writer('" action="')
        __M_writer(str( form.form_action or '' ))
        __M_writer('" method="')
        __M_writer(str( form.form_method ))
        __M_writer('">\n\n')
        __M_writer('        ')
        __M_writer(str( csrf_input ))
        __M_writer('\n\n')
        __M_writer('        ')
        __M_writer(str( form.as_p() ))
        __M_writer('\n\n')
        __M_writer('        <p class="text-center"><button type="submit" class="btn btn-primary">')
        __M_writer(filters.html_escape(str( form.submit_text )))
        __M_writer('</button></p>\n\n    </form>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/formlib/templates/form.htm", "uri": "form.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 3, "26": 3, "27": 6, "28": 6, "29": 6, "30": 6, "31": 6, "32": 6, "33": 9, "34": 9, "35": 9, "36": 12, "37": 12, "38": 12, "39": 15, "40": 15, "41": 15, "47": 41}}
__M_END_METADATA
"""
