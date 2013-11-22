'''OpenGL extension ARB.create_context_robustness

This module customises the behaviour of the 
OpenGL.raw.GLX.ARB.create_context_robustness to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/create_context_robustness.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.ARB.create_context_robustness import *

def glInitCreateContextRobustnessARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION