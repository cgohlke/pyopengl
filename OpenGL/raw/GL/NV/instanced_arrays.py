'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_instanced_arrays'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_instanced_arrays')
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_NV=_C('GL_VERTEX_ATTRIB_ARRAY_DIVISOR_NV',0x88FE)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribDivisorNV(index,divisor):pass
