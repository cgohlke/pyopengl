'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIX_resample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_resample')
GL_PACK_RESAMPLE_SGIX=_C('GL_PACK_RESAMPLE_SGIX',0x842C)
GL_RESAMPLE_DECIMATE_SGIX=_C('GL_RESAMPLE_DECIMATE_SGIX',0x8430)
GL_RESAMPLE_REPLICATE_SGIX=_C('GL_RESAMPLE_REPLICATE_SGIX',0x842E)
GL_RESAMPLE_ZERO_FILL_SGIX=_C('GL_RESAMPLE_ZERO_FILL_SGIX',0x842F)
GL_UNPACK_RESAMPLE_SGIX=_C('GL_UNPACK_RESAMPLE_SGIX',0x842D)

