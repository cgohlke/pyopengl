'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ATI_texture_env_combine3'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_texture_env_combine3')
GL_MODULATE_ADD_ATI=_C('GL_MODULATE_ADD_ATI',0x8744)
GL_MODULATE_SIGNED_ADD_ATI=_C('GL_MODULATE_SIGNED_ADD_ATI',0x8745)
GL_MODULATE_SUBTRACT_ATI=_C('GL_MODULATE_SUBTRACT_ATI',0x8746)

