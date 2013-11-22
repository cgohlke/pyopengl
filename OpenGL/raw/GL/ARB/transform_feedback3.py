'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_transform_feedback3'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_transform_feedback3')
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS=_C('GL_MAX_TRANSFORM_FEEDBACK_BUFFERS',0x8E70)
GL_MAX_VERTEX_STREAMS=_C('GL_MAX_VERTEX_STREAMS',0x8E71)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBeginQueryIndexed(target,index,id):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glDrawTransformFeedbackStream(mode,id,stream):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEndQueryIndexed(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetQueryIndexediv(target,index,pname,params):pass
