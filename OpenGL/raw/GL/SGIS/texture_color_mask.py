'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIS_texture_color_mask'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_texture_color_mask')
GL_TEXTURE_COLOR_WRITEMASK_SGIS=_C('GL_TEXTURE_COLOR_WRITEMASK_SGIS',0x81EF)
@_f
@_p.types(None,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glTextureColorMaskSGIS(red,green,blue,alpha):pass
