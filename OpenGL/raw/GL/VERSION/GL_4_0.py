'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_VERSION_GL_4_0'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_VERSION_GL_4_0',error_checker=_errors._error_checker)
GL_ACTIVE_SUBROUTINES=_C('GL_ACTIVE_SUBROUTINES',0x8DE5)
GL_ACTIVE_SUBROUTINE_MAX_LENGTH=_C('GL_ACTIVE_SUBROUTINE_MAX_LENGTH',0x8E48)
GL_ACTIVE_SUBROUTINE_UNIFORMS=_C('GL_ACTIVE_SUBROUTINE_UNIFORMS',0x8DE6)
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS=_C('GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS',0x8E47)
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH=_C('GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH',0x8E49)
GL_COMPATIBLE_SUBROUTINES=_C('GL_COMPATIBLE_SUBROUTINES',0x8E4B)
GL_DOUBLE_MAT2=_C('GL_DOUBLE_MAT2',0x8F46)
GL_DOUBLE_MAT2x3=_C('GL_DOUBLE_MAT2x3',0x8F49)
GL_DOUBLE_MAT2x4=_C('GL_DOUBLE_MAT2x4',0x8F4A)
GL_DOUBLE_MAT3=_C('GL_DOUBLE_MAT3',0x8F47)
GL_DOUBLE_MAT3x2=_C('GL_DOUBLE_MAT3x2',0x8F4B)
GL_DOUBLE_MAT3x4=_C('GL_DOUBLE_MAT3x4',0x8F4C)
GL_DOUBLE_MAT4=_C('GL_DOUBLE_MAT4',0x8F48)
GL_DOUBLE_MAT4x2=_C('GL_DOUBLE_MAT4x2',0x8F4D)
GL_DOUBLE_MAT4x3=_C('GL_DOUBLE_MAT4x3',0x8F4E)
GL_DOUBLE_VEC2=_C('GL_DOUBLE_VEC2',0x8FFC)
GL_DOUBLE_VEC3=_C('GL_DOUBLE_VEC3',0x8FFD)
GL_DOUBLE_VEC4=_C('GL_DOUBLE_VEC4',0x8FFE)
GL_DRAW_INDIRECT_BUFFER=_C('GL_DRAW_INDIRECT_BUFFER',0x8F3F)
GL_DRAW_INDIRECT_BUFFER_BINDING=_C('GL_DRAW_INDIRECT_BUFFER_BINDING',0x8F43)
GL_FRACTIONAL_EVEN=_C('GL_FRACTIONAL_EVEN',0x8E7C)
GL_FRACTIONAL_ODD=_C('GL_FRACTIONAL_ODD',0x8E7B)
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS=_C('GL_FRAGMENT_INTERPOLATION_OFFSET_BITS',0x8E5D)
GL_GEOMETRY_SHADER_INVOCATIONS=_C('GL_GEOMETRY_SHADER_INVOCATIONS',0x887F)
GL_INT_SAMPLER_CUBE_MAP_ARRAY=_C('GL_INT_SAMPLER_CUBE_MAP_ARRAY',0x900E)
GL_ISOLINES=_C('GL_ISOLINES',0x8E7A)
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E1E)
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E1F)
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET=_C('GL_MAX_FRAGMENT_INTERPOLATION_OFFSET',0x8E5C)
GL_MAX_GEOMETRY_SHADER_INVOCATIONS=_C('GL_MAX_GEOMETRY_SHADER_INVOCATIONS',0x8E5A)
GL_MAX_PATCH_VERTICES=_C('GL_MAX_PATCH_VERTICES',0x8E7D)
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET=_C('GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET',0x8E5F)
GL_MAX_SUBROUTINES=_C('GL_MAX_SUBROUTINES',0x8DE7)
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS=_C('GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS',0x8DE8)
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_INPUT_COMPONENTS',0x886C)
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS',0x8E83)
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS',0x8E81)
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS',0x8E85)
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS=_C('GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS',0x8E89)
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E7F)
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS',0x886D)
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS',0x8E86)
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS',0x8E82)
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS',0x8E8A)
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E80)
GL_MAX_TESS_GEN_LEVEL=_C('GL_MAX_TESS_GEN_LEVEL',0x8E7E)
GL_MAX_TESS_PATCH_COMPONENTS=_C('GL_MAX_TESS_PATCH_COMPONENTS',0x8E84)
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS=_C('GL_MAX_TRANSFORM_FEEDBACK_BUFFERS',0x8E70)
GL_MAX_VERTEX_STREAMS=_C('GL_MAX_VERTEX_STREAMS',0x8E71)
GL_MAX_VERTEX_STREAMS=_C('GL_MAX_VERTEX_STREAMS',0x8E71)
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET=_C('GL_MIN_FRAGMENT_INTERPOLATION_OFFSET',0x8E5B)
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET=_C('GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET',0x8E5E)
GL_MIN_SAMPLE_SHADING_VALUE=_C('GL_MIN_SAMPLE_SHADING_VALUE',0x8C37)
GL_NUM_COMPATIBLE_SUBROUTINES=_C('GL_NUM_COMPATIBLE_SUBROUTINES',0x8E4A)
GL_PATCHES=_C('GL_PATCHES',0x000E)
GL_PATCH_DEFAULT_INNER_LEVEL=_C('GL_PATCH_DEFAULT_INNER_LEVEL',0x8E73)
GL_PATCH_DEFAULT_OUTER_LEVEL=_C('GL_PATCH_DEFAULT_OUTER_LEVEL',0x8E74)
GL_PATCH_VERTICES=_C('GL_PATCH_VERTICES',0x8E72)
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY=_C('GL_PROXY_TEXTURE_CUBE_MAP_ARRAY',0x900B)
GL_QUADS=_C('GL_QUADS',0x0007)
GL_SAMPLER_CUBE_MAP_ARRAY=_C('GL_SAMPLER_CUBE_MAP_ARRAY',0x900C)
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW=_C('GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',0x900D)
GL_SAMPLE_SHADING=_C('GL_SAMPLE_SHADING',0x8C36)
GL_TESS_CONTROL_OUTPUT_VERTICES=_C('GL_TESS_CONTROL_OUTPUT_VERTICES',0x8E75)
GL_TESS_CONTROL_SHADER=_C('GL_TESS_CONTROL_SHADER',0x8E88)
GL_TESS_EVALUATION_SHADER=_C('GL_TESS_EVALUATION_SHADER',0x8E87)
GL_TESS_GEN_MODE=_C('GL_TESS_GEN_MODE',0x8E76)
GL_TESS_GEN_POINT_MODE=_C('GL_TESS_GEN_POINT_MODE',0x8E79)
GL_TESS_GEN_SPACING=_C('GL_TESS_GEN_SPACING',0x8E77)
GL_TESS_GEN_VERTEX_ORDER=_C('GL_TESS_GEN_VERTEX_ORDER',0x8E78)
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY=_C('GL_TEXTURE_BINDING_CUBE_MAP_ARRAY',0x900A)
GL_TEXTURE_CUBE_MAP_ARRAY=_C('GL_TEXTURE_CUBE_MAP_ARRAY',0x9009)
GL_TRANSFORM_FEEDBACK=_C('GL_TRANSFORM_FEEDBACK',0x8E22)
GL_TRANSFORM_FEEDBACK_BINDING=_C('GL_TRANSFORM_FEEDBACK_BINDING',0x8E25)
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE',0x8E24)
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED=_C('GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED',0x8E23)
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER',0x84F0)
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER',0x84F1)
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',0x900F)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBeginQueryIndexed(target,index,id):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTransformFeedback(target,id):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparatei(buf,modeRGB,modeAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBlendEquationi(buf,mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBlendFuncSeparatei(buf,srcRGB,dstRGB,srcAlpha,dstAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendFunci(buf,src,dst):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glDrawArraysIndirect(mode,indirect):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glDrawElementsIndirect(mode,type,indirect):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDrawTransformFeedback(mode,id):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glDrawTransformFeedbackStream(mode,id,stream):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEndQueryIndexed(target,index):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetActiveSubroutineName(program,shadertype,index,bufSize,length,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetActiveSubroutineUniformName(program,shadertype,index,bufSize,length,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetActiveSubroutineUniformiv(program,shadertype,index,pname,values):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetProgramStageiv(program,shadertype,pname,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetQueryIndexediv(target,index,pname,params):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLcharArray)
def glGetSubroutineIndex(program,shadertype,name):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,_cs.GLenum,arrays.GLcharArray)
def glGetSubroutineUniformLocation(program,shadertype,name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLuintArray)
def glGetUniformSubroutineuiv(shadertype,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLdoubleArray)
def glGetUniformdv(program,location,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTransformFeedback(id):pass
@_f
@_p.types(None,_cs.GLfloat)
def glMinSampleShading(value):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPatchParameterfv(pname,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPatchParameteri(pname,value):pass
@_f
@_p.types(None,)
def glPauseTransformFeedback():pass
@_f
@_p.types(None,)
def glResumeTransformFeedback():pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble)
def glUniform1d(location,x):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform1dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble)
def glUniform2d(location,x,y):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform2dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glUniform3d(location,x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform3dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glUniform4d(location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform4dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2x3dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2x4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3x2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3x4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4x2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4x3dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glUniformSubroutinesuiv(shadertype,count,indices):pass
