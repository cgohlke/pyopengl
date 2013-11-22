'''OpenGL extension SGIX.texture_multi_buffer

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.texture_multi_buffer to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/texture_multi_buffer.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SGIX.texture_multi_buffer import *

def glInitTextureMultiBufferSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION