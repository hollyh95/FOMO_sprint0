# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516818004.952925
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
        def content_top():
            return render_content_top(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def error_message():
            return render_error_message(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('homepage/styles/custom.css"\n\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n\n\n\n             <!-- Static navbar -->\n              <nav class="navbar navbar-default navbar-static-top">\n                <div class="container-fluid">\n                  <div class="navbar-header">\n                    <a class="navbar-brand" href="index"><i class="fa fa-ravelry" aria-hidden="true"></i></a>\n                  </div>\n                  <ul id="navbar" class="navbar-collapse collapse">\n\n\n                    <ul class="nav navbar-nav">\n\n\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\n                    </ul>\n\n                    <ul class="nav navbar-nav navbar-right">\n\n                      <li class="dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Login <span class="caret"></span></a>\n                        <ul class="dropdown-menu">\n                          <li><a href="#">Sign in</a></li>\n                          <li><a href="#">Sign up</a></li>\n                          <li role="separator" class="divider"></li>\n                          <li class="dropdown-header">Nav header</li>\n                          <li><a href="#">Separated link</a></li>\n                          <li><a href="#">One more separated link</a></li>\n                        </ul>\n                      </li>\n                    </ul>\n\n                  </div><!--/.nav-collapse -->\n                </div><!--/.container-fluid -->\n              </nav>\n\n           </head>\n    <body>\n        <main>\n\n            <div class="text-center & content_top">\n             <div content = "header">\n                ')
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
        

        __M_writer('\n            </div>\n\n\n\n        </main>\n\n<div>\n    </br>\n    </br>\n    </br>\n    </br>\n    </br>\n</div>\n            <footer>\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_footer'):
            context['self'].body_footer(**pageargs)
        

        __M_writer('\n            </footer>\n\n    </body>\n\n</html>\n\n\n')
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
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 118, "19": 0, "40": 2, "45": 9, "46": 21, "47": 22, "48": 22, "49": 24, "50": 24, "51": 25, "52": 25, "53": 26, "54": 26, "55": 30, "56": 31, "57": 31, "62": 53, "67": 82, "72": 90, "77": 96, "82": 102, "87": 120, "93": 8, "99": 8, "105": 49, "111": 49, "117": 81, "123": 81, "129": 88, "135": 88, "141": 94, "147": 94, "153": 100, "159": 100, "165": 117, "171": 117, "172": 118, "173": 119, "174": 119, "180": 174}}
__M_END_METADATA
"""
