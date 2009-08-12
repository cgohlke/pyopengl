'''OpenGL extension EXT.framebuffer_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.framebuffer_multisample to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.framebuffer_multisample import *
### END AUTOGENERATED SECTION