"""Data-type definitions for EGL/GLES"""
import ctypes
pointer = ctypes.pointer

EGLBoolean = ctypes.c_uint32
EGLenum = ctypes.c_uint32
EGLint = c_int = ctypes.c_int32

EGLConfig = ctypes.c_size_t
EGLContext = ctypes.c_size_t
EGLDisplay = ctypes.c_size_t
EGLSurface = ctypes.c_size_t
EGLClientBuffer = ctypes.c_size_t
EGLImageKHR = ctypes.c_size_t

EGLScreenMESA = ctypes.c_ulong
EGLModeMESA = ctypes.c_ulong

EGLNativeFileDescriptorKHR = ctypes.c_int

EGLSyncKHR = EGLSyncNV = ctypes.c_voidp
EGLTimeKHR = EGLTimeNV = ctypes.c_ulonglong
EGLuint64KHR = EGLuint64NV = ctypes.c_ulonglong
EGLStreamKHR = ctypes.c_voidp
EGLsizeiANDROID = ctypes.c_size_t

class EGLClientPixmapHI( ctypes.Structure):
    _fields_ = [
        ('pData',ctypes.c_voidp),
        ('iWidth',EGLint),
        ('iHeight',EGLint),
        ('iStride',EGLint),
    ]
class wl_display( ctypes.Structure):
    """Opaque structure from Mesa Wayland API"""
    _fields_ = []

# These are X11... no good, really...
EGLNativeDisplayType = ctypes.c_size_t # Display *
EGLNativePixmapType = ctypes.c_size_t # Pixmap 
EGLNativeWindowType = ctypes.c_size_t # Window

NativeDisplayType = EGLNativeDisplayType 
NativePixmapType = EGLNativePixmapType
NativeWindowType = EGLNativeWindowType

del ctypes 
del pointer 