from sw import *
import os
import shutil
from .colorcode import *

ini = os.path.join(os.path.dirname(__file__), 'styles.ini')
ini0 = os.path.join(os.path.dirname(__file__), 'styles.sample.ini')
if os.path.isfile(ini0) and not os.path.isfile(ini):
    shutil.copyfile(ini0, ini)

if app_api_version()<'1.0.145':
    msg_box(MSG_ERROR, 'Plugin needs newer SynWrite')

def set_sel_attribute(n, nlen, attribs):
    for (att_id, attrib_n) in attribs:
        ed.set_sel(n, nlen)
        ed.set_attr(att_id, attrib_n)

def set_text_attribute(attribs):
    allwords = ini_read(ini, 'op', 'allwords', '0')
    if int(allwords) > 0:
        n, nlen = ed.get_sel()
        if nlen <= 0:
            carets = ed.get_carets()
            if carets: return
            x0, y0 = ed.get_caret_xy()

            n, nlen, word = ed.get_word(x0, y0)
        else:
            word = ed.get_text_sel()

        text = ed.get_text_all()
        ind = 0
        while ind != -1:
            if ind >= 0:
                ind = text.find(word, ind+1)
            else:
                ind = text.find(word)
            if ind >= 0:
                set_sel_attribute(ind, len(word),attribs)
        ed.set_sel(n, nlen)
    else:
        for (att_id, attrib_n) in attribs:
            ed.set_attr(att_id, attrib_n)

def do_color(n):
    attribs = []
    st = ini_read(ini, 'colors', str(n), '')
    if st:
        ncolor = HTMLColorToPILColor(st)
        attribs.extend([(ATTRIB_COLOR_BG,ncolor)])
    st = ini_read(ini, 'styles', str(n), '')
    if st:
        if 'b' in st: attribs.extend([(ATTRIB_SET_BOLD,0)])
        if 'i' in st: attribs.extend([(ATTRIB_SET_ITALIC,0)])
        if 'u' in st: attribs.extend([(ATTRIB_SET_UNDERLINE,0)])
        if 's' in st: attribs.extend([(ATTRIB_SET_STRIKEOUT,0)])
    if attribs:
        set_text_attribute(attribs)

class Command:
    def color1(self): do_color(1)
    def color2(self): do_color(2)
    def color3(self): do_color(3)
    def color4(self): do_color(4)
    def color5(self): do_color(5)
    def color6(self): do_color(6)

    def format_bold(self):
        set_text_attribute([(ATTRIB_SET_BOLD,0)])
    def format_italic(self):
        set_text_attribute([(ATTRIB_SET_ITALIC,0)])
    def format_underline(self):
        set_text_attribute([(ATTRIB_SET_UNDERLINE,0)])

    def clear_all(self):
        ed.set_attr(ATTRIB_CLEAR_ALL, 0)
    def clear_sel(self):
        set_text_attribute([(ATTRIB_CLEAR_SELECTION,0)])

    def edit(self):
        file_open(ini)
