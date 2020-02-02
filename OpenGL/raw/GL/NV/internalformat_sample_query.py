'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_internalformat_sample_query'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_internalformat_sample_query',error_checker=_errors._error_checker)
GL_CONFORMANT_NV=_C('GL_CONFORMANT_NV',0x9374)
GL_MULTISAMPLES_NV=_C('GL_MULTISAMPLES_NV',0x9371)
GL_RENDERBUFFER=_C('GL_RENDERBUFFER',0x8D41)
GL_SUPERSAMPLE_SCALE_X_NV=_C('GL_SUPERSAMPLE_SCALE_X_NV',0x9372)
GL_SUPERSAMPLE_SCALE_Y_NV=_C('GL_SUPERSAMPLE_SCALE_Y_NV',0x9373)
GL_TEXTURE_2D_MULTISAMPLE=_C('GL_TEXTURE_2D_MULTISAMPLE',0x9100)
GL_TEXTURE_2D_MULTISAMPLE_ARRAY=_C('GL_TEXTURE_2D_MULTISAMPLE_ARRAY',0x9102)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,arrays.GLintArray)
def glGetInternalformatSampleivNV(target,internalformat,samples,pname,count,params):pass
