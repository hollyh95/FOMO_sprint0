# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520476464.35071
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['error_message', 'navbar', 'content_top', 'content_left', 'content', 'content_right', 'body_footer']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def error_message():
            return render_error_message(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
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
        __M_writer('homepage/media/bootstrap/css/bootstrap-theme.min.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/styles/custom.css">\n\n\n')
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
        __M_writer('                    </ul>\n                  </div><!--/.nav-collapse -->\n                </div><!--/.container-fluid -->\n              </nav>\n\n           </head>\n    <body>\n        <main>\n<div class="container-fluid">\n            <div class="text-center & content_top">\n             <div content = "header">\n                ')
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
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 112, "19": 0, "41": 2, "46": 9, "47": 21, "48": 22, "49": 22, "50": 24, "51": 24, "52": 25, "53": 25, "54": 26, "55": 26, "56": 30, "57": 31, "58": 31, "63": 53, "64": 57, "65": 58, "66": 60, "67": 61, "68": 61, "69": 61, "70": 62, "71": 62, "72": 64, "77": 76, "82": 84, "87": 90, "92": 96, "97": 114, "103": 8, "109": 8, "115": 49, "121": 49, "127": 75, "133": 75, "139": 82, "145": 82, "151": 88, "157": 88, "163": 94, "169": 94, "175": 111, "181": 111, "182": 112, "183": 113, "184": 113, "190": 184}}
__M_END_METADATA
"""
