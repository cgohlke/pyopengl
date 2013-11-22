'''OpenGL extension SGIX.visual_select_group

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIX.visual_select_group to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/visual_select_group.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.SGIX.visual_select_group import *

def glInitVisualSelectGroupSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION