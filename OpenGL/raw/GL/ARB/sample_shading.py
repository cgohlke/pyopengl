'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_sample_shading'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_sample_shading')
GL_MIN_SAMPLE_SHADING_VALUE_ARB=_C('GL_MIN_SAMPLE_SHADING_VALUE_ARB',0x8C37)
GL_SAMPLE_SHADING_ARB=_C('GL_SAMPLE_SHADING_ARB',0x8C36)
@_f
@_p.types(None,_cs.GLfloat)
def glMinSampleShadingARB(value):pass
