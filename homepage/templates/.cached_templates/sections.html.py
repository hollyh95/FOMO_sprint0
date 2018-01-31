# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517350965.232536
_enable_loop = True
_template_filename = '/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content_top', 'content_left', 'content_right', 'content', 'error_message', 'body_footer']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def error_message():
            return render_error_message(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
        def content_top():
            return render_content_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'error_message'):
            context['self'].error_message(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_footer'):
            context['self'].body_footer(**pageargs)
        

        __M_writer('\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n\n<p>Lorem ipsum dolor amet hammock art party palo santo, cardigan pour-over asymmetrical hashtag chicharrones heirloom. Ennui normcore gastropub, hashtag copper mug gentrify taxidermy. Cold-pressed health goth mumblecore keffiyeh hammock gastropub. Pabst vaporware tattooed stumptown, aesthetic twee organic chambray snackwave. Crucifix 8-bit bitters hoodie live-edge craft beer. Truffaut humblebrag meh, fixie mlkshk asymmetrical portland meggings shabby chic occupy bitters YOLO kale chips kitsch gluten-free. Trust fund freegan dreamcatcher chambray selfies hella ramps.\n    </p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n <p>Lorem ipsum dolor amet hammock art party palo santo, cardigan pour-over asymmetrical hashtag chicharrones heirloom. Ennui normcore gastropub, hashtag copper mug gentrify taxidermy. Cold-pressed health goth mumblecore keffiyeh hammock gastropub. Pabst vaporware tattooed stumptown, aesthetic twee organic chambray snackwave. Crucifix 8-bit bitters hoodie live-edge craft beer. Truffaut humblebrag meh, fixie mlkshk asymmetrical portland meggings shabby chic occupy bitters YOLO kale chips kitsch gluten-free. Trust fund freegan dreamcatcher chambray selfies hella ramps.\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n    <p>Lorem ipsum dolor amet hammock art party palo santo, cardigan pour-over asymmetrical hashtag chicharrones heirloom. Ennui normcore gastropub, hashtag copper mug gentrify taxidermy. Cold-pressed health goth mumblecore keffiyeh hammock gastropub. Pabst vaporware tattooed stumptown, aesthetic twee organic chambray snackwave. Crucifix 8-bit bitters hoodie live-edge craft beer. Truffaut humblebrag meh, fixie mlkshk asymmetrical portland meggings shabby chic occupy bitters YOLO kale chips kitsch gluten-free. Trust fund freegan dreamcatcher chambray selfies hella ramps.\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <p>Iceland coloring book aesthetic hella edison bulb fam subway tile, blue bottle biodiesel four dollar toast chambray poke palo santo. Pop-up mixtape brooklyn skateboard, knausgaard thundercats ramps. Tilde tousled bicycle rights tumeric swag edison bulb echo park. Enamel pin humblebrag shaman pickled, roof party keffiyeh cornhole irony adaptogen bespoke hot chicken. Banh mi mumblecore typewriter raclette mlkshk. Art party humblebrag fam austin.\n    </p>\n<p>Humblebrag chia beard kinfolk, venmo butcher hammock health goth normcore. Keytar leggings raw denim keffiyeh chia forage tofu gochujang sartorial microdosing synth ethical. Austin pour-over migas, ramps truffaut la croix jean shorts af. Organic quinoa enamel pin poke lomo woke lumbersexual health goth disrupt vexillologist. Raw denim synth copper mug deep v. Hell of ethical actually stumptown keytar synth. Copper mug paleo actually pok pok dreamcatcher shaman crucifix kale chips venmo.</p>\n</p>\n\n<p>Iceland coloring book aesthetic hella edison bulb fam subway tile, blue bottle biodiesel four dollar toast chambray poke palo santo. Pop-up mixtape brooklyn skateboard, knausgaard thundercats ramps. Tilde tousled bicycle rights tumeric swag edison bulb echo park. Enamel pin humblebrag shaman pickled, roof party keffiyeh cornhole irony adaptogen bespoke hot chicken. Banh mi mumblecore typewriter raclette mlkshk. Art party humblebrag fam austin.\n    </p>\n<p>Humblebrag chia beard kinfolk, venmo butcher hammock health goth normcore. Keytar leggings raw denim keffiyeh chia forage tofu gochujang sartorial microdosing synth ethical. Austin pour-over migas, ramps truffaut la croix jean shorts af. Organic quinoa enamel pin poke lomo woke lumbersexual health goth disrupt vexillologist. Raw denim synth copper mug deep v. Hell of ethical actually stumptown keytar synth. Copper mug paleo actually pok pok dreamcatcher shaman crucifix kale chips venmo.</p>\n</p>\n\n<p>Iceland coloring book aesthetic hella edison bulb fam subway tile, blue bottle biodiesel four dollar toast chambray poke palo santo. Pop-up mixtape brooklyn skateboard, knausgaard thundercats ramps. Tilde tousled bicycle rights tumeric swag edison bulb echo park. Enamel pin humblebrag shaman pickled, roof party keffiyeh cornhole irony adaptogen bespoke hot chicken. Banh mi mumblecore typewriter raclette mlkshk. Art party humblebrag fam austin.\n    </p>\n<p>Humblebrag chia beard kinfolk, venmo butcher hammock health goth normcore. Keytar leggings raw denim keffiyeh chia forage tofu gochujang sartorial microdosing synth ethical. Austin pour-over migas, ramps truffaut la croix jean shorts af. Organic quinoa enamel pin poke lomo woke lumbersexual health goth disrupt vexillologist. Raw denim synth copper mug deep v. Hell of ethical actually stumptown keytar synth. Copper mug paleo actually pok pok dreamcatcher shaman crucifix kale chips venmo.</p>\n</p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_error_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def error_message():
            return render_error_message(context)
        __M_writer = context.writer()
        __M_writer('\n    <p>This site is under construction. Sorry for any inconvenience!</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_footer():
            return render_body_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hollyholland/PycharmProjects/FOMO1/FOMO/homepage/templates/sections.html", "uri": "sections.html", "source_encoding": "utf-8", "line_map": {"28": 0, "45": 1, "50": 8, "55": 13, "60": 18, "65": 36, "70": 40, "75": 43, "81": 3, "87": 3, "93": 10, "99": 10, "105": 15, "111": 15, "117": 20, "123": 20, "129": 38, "135": 38, "141": 42, "147": 42, "153": 147}}
__M_END_METADATA
"""
