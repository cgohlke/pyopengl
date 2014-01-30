'''OpenGL extension ARB.draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.draw_buffers to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/draw_buffers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.draw_buffers import *

def glInitDrawBuffersARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy as _lazy
@_lazy( glDrawBuffersARB )
def glDrawBuffersARB( baseOperation, n=None, bufs=None ):
    """glDrawBuffersARB( bufs ) -> bufs 
    
    Wrapper will calculate n from dims of bufs if only 
    one argument is provided...
    """
    if bufs is None:
        bufs = n
        n = None
    bufs = arrays.GLenumArray.asArray( bufs )
    if n is None:
        n = arrays.GLenumArray.arraySize( bufs )
    return baseOperation( n,bufs )

from OpenGL.GL import glget
glget.addGLGetConstant( GL_MAX_DRAW_BUFFERS_ARB, (1,) )
# Should have output arrays for the buffers too???
