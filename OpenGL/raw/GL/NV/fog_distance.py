'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_fog_distance'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_fog_distance')
GL_EYE_PLANE=_C('GL_EYE_PLANE',0x2502)
GL_EYE_PLANE_ABSOLUTE_NV=_C('GL_EYE_PLANE_ABSOLUTE_NV',0x855C)
GL_EYE_RADIAL_NV=_C('GL_EYE_RADIAL_NV',0x855B)
GL_FOG_DISTANCE_MODE_NV=_C('GL_FOG_DISTANCE_MODE_NV',0x855A)

