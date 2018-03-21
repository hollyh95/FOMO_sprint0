# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520913616.74094
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['error_message', 'navbar', 'content_top', 'content_left', 'content', 'content_right', 'body_footer']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def error_message():
            return render_error_message(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n\n    <div class="text-center">\n            <div class="header & error_message">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'error_message'):
            context['self'].error_message(**pageargs)
        

        __M_writer('\n            </div>\n    </div>\n\n\n    <head>\n\n\n\n        <title>FOMO</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n        <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap-theme.min.css">\n\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n\n\n\n             <!-- Static navbar -->\n              <nav class="navbar navbar-inverse navbar-static-top">\n                <div class="container-fluid">\n                  <div class="navbar-header">\n                    <a class="navbar-brand" href="index"><i class="fa fa-ravelry" aria-hidden="true"></i></a>\n                  </div>\n                  <ul id="navbar" class="navbar-collapse collapse">\n\n\n                    <ul class="nav navbar-nav">\n\n\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\n                    </ul>\n\n                    <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated:
            __M_writer('                        <li><a href="/account/logout/">Logout</a></li>\n')
        if request.user.is_authenticated == False:
            __M_writer('                        <li class="')
            __M_writer(str( 'active' if request.dmp.page == 'account/login' else ''))
            __M_writer('"><a href="/account/login/">Login</a></li>\n                        <li class="')
            __M_writer(str( 'active' if request.dmp.page == 'account/signup' else ''))
            __M_writer('"><a href="/account/signup/">Signup</a></li>\n')
        __M_writer('                    </ul>\n                  </div><!--/.nav-collapse -->\n                </div><!--/.container-fluid -->\n              </nav>\n\n           </head>\n    <body>\n        <main>\n<div class="container-fluid">\n            <div class="text-center & content_top">\n             <div class="header">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n            </div>\n            </div>\n\n\n            <div class="col-md-2 & content_left">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n            </div>\n\n            <div class="col-md-8 & content">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            </div>\n\n            <div class="col-md-2 & content_right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n            </div>\n</div>\n\n\n        </main>\n\n<div>\n    </br>\n    </br>\n    </br>\n    </br>\n    </br>\n</div>\n\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_footer'):
            context['self'].body_footer(**pageargs)
        

        __M_writer('\n\n\n    </body>\n\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_error_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def error_message():
            return render_error_message(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        __M_writer('\n\n                        <li><a href="#">Custom navbar</a></li>\n\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_footer():
            return render_body_footer(context)
        __M_writer = context.writer()
        __M_writer('\n                        ')
        __M_writer('\n                            &copy; Copyright ')
        __M_writer(str( datetime.now().year ))
        __M_writer('. All rights reserved.\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 111, "20": 0, "42": 2, "47": 9, "48": 21, "49": 22, "50": 22, "51": 24, "52": 24, "53": 25, "54": 25, "55": 29, "56": 30, "57": 30, "62": 52, "63": 56, "64": 57, "65": 59, "66": 60, "67": 60, "68": 60, "69": 61, "70": 61, "71": 63, "76": 75, "81": 83, "86": 89, "91": 95, "96": 113, "102": 8, "108": 8, "114": 48, "120": 48, "126": 74, "132": 74, "138": 81, "144": 81, "150": 87, "156": 87, "162": 93, "168": 93, "174": 110, "180": 110, "181": 111, "182": 112, "183": 112, "189": 183}}
__M_END_METADATA
"""
