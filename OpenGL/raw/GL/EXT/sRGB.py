'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_sRGB'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_sRGB')
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT',0x8210)
GL_SRGB8_ALPHA8_EXT=_C('GL_SRGB8_ALPHA8_EXT',0x8C43)
GL_SRGB_ALPHA_EXT=_C('GL_SRGB_ALPHA_EXT',0x8C42)
GL_SRGB_EXT=_C('GL_SRGB_EXT',0x8C40)

