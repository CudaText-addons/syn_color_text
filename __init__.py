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

def do_color(n):
    st = ini_read(ini, 'colors', str(n), '')
    if st:
        ncolor = HTMLColorToPILColor(st)
        ed.set_attr(ATTRIB_COLOR_BG, ncolor)
    st = ini_read(ini, 'styles', str(n), '')
    if st:
        if 'b' in st: ed.set_attr(ATTRIB_SET_BOLD, 0)
        if 'i' in st: ed.set_attr(ATTRIB_SET_ITALIC, 0)
        if 'u' in st: ed.set_attr(ATTRIB_SET_UNDERLINE, 0)
        if 's' in st: ed.set_attr(ATTRIB_SET_STRIKEOUT, 0)

class Command:
    def color1(self): do_color(1)
    def color2(self): do_color(2)
    def color3(self): do_color(3)
    def color4(self): do_color(4)
    def color5(self): do_color(5)
    def color6(self): do_color(6)
        
    def format_bold(self):
        ed.set_attr(ATTRIB_SET_BOLD, 0)
    def format_italic(self):
        ed.set_attr(ATTRIB_SET_ITALIC, 0)
    def format_underline(self):
        ed.set_attr(ATTRIB_SET_UNDERLINE, 0)
        
    def clear_all(self):
        ed.set_attr(ATTRIB_CLEAR_ALL, 0)
    def clear_sel(self):
        ed.set_attr(ATTRIB_CLEAR_SELECTION, 0)
        
    def edit(self):
        file_open(ini)
