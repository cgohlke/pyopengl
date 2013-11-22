'''OpenGL extension EXT.create_context_es2_profile

This module customises the behaviour of the 
OpenGL.raw.GLX.EXT.create_context_es2_profile to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/create_context_es2_profile.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.EXT.create_context_es2_profile import *

def glInitCreateContextEs2ProfileEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION