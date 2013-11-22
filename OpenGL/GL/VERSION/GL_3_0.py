'''OpenGL extension VERSION.GL_3_0

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_3_0 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_3_0.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.VERSION.GL_3_0 import *

def glInitGl30VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
glget.addGLGetConstant( GL_NUM_EXTENSIONS, (1,))
from ctypes import c_char_p
glGetStringi.restype = c_char_p

from OpenGL.GL.ARB.vertex_array_object import *
from OpenGL.GL.ARB.texture_buffer_object import *
from OpenGL.GL.ARB.framebuffer_object import *
from OpenGL.GL.ARB.map_buffer_range import *

GL_DEPTH_BUFFER = constant.Constant( 'GL_DEPTH_BUFFER', 0x8223 )
GL_STENCIL_BUFFER = constant.Constant( 'GL_STENCIL_BUFFER', 0x8224 )
