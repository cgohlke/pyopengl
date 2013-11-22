'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_geometry_shader4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_geometry_shader4')
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB=_C('GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB',0x8DA7)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',0x8CD4)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB=_C('GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB',0x8DA9)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB=_C('GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB',0x8DA8)
GL_GEOMETRY_INPUT_TYPE_ARB=_C('GL_GEOMETRY_INPUT_TYPE_ARB',0x8DDB)
GL_GEOMETRY_OUTPUT_TYPE_ARB=_C('GL_GEOMETRY_OUTPUT_TYPE_ARB',0x8DDC)
GL_GEOMETRY_SHADER_ARB=_C('GL_GEOMETRY_SHADER_ARB',0x8DD9)
GL_GEOMETRY_VERTICES_OUT_ARB=_C('GL_GEOMETRY_VERTICES_OUT_ARB',0x8DDA)
GL_LINES_ADJACENCY_ARB=_C('GL_LINES_ADJACENCY_ARB',0x000A)
GL_LINE_STRIP_ADJACENCY_ARB=_C('GL_LINE_STRIP_ADJACENCY_ARB',0x000B)
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB=_C('GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB',0x8DE0)
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB=_C('GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB',0x8C29)
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB=_C('GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB',0x8DE1)
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB=_C('GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB',0x8DDF)
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB=_C('GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB',0x8DDD)
GL_MAX_VARYING_COMPONENTS=_C('GL_MAX_VARYING_COMPONENTS',0x8B4B)
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB=_C('GL_MAX_VERTEX_VARYING_COMPONENTS_ARB',0x8DDE)
GL_PROGRAM_POINT_SIZE_ARB=_C('GL_PROGRAM_POINT_SIZE_ARB',0x8642)
GL_TRIANGLES_ADJACENCY_ARB=_C('GL_TRIANGLES_ADJACENCY_ARB',0x000C)
GL_TRIANGLE_STRIP_ADJACENCY_ARB=_C('GL_TRIANGLE_STRIP_ADJACENCY_ARB',0x000D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTextureARB(target,attachment,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLenum)
def glFramebufferTextureFaceARB(target,attachment,texture,level,face):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTextureLayerARB(target,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glProgramParameteriARB(program,pname,value):pass
