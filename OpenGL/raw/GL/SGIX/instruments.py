'''OpenGL extension SGIX.instruments

Overview (from the spec)
	
	This extension allows the gathering and return of performance
	measurements from within the graphics pipeline by adding
	instrumentation.
	
	There are two reasons to do this.  The first is as a part of some
	type of fixed-frame-rate load management scheme.  If we know that
	the pipeline is stalled or struggling to process the amount of
	data we have given it so far, we can reduce the level of detail of
	the remaining objects in the current frame or the next frame, or
	adjust the framebuffer resolution for the next frame if we have a
	video-zoom capability available.  We can call this type of
	instrumentation Load Monitoring.
	
	The second is for performance tuning and debugging of an
	application. It might tell us how many triangles were culled or
	clipped before being rasterized.  We can call this simply Tuning.
	
	Load Monitoring requires that the instrumentation and the access
	of the measurements be efficient, otherwise the instrumentation
	itself will reduce performance more than any load-management
	scheme could hope to offset.  Tuning does not have the same
	requirements.
	
	The proposed extension adds a call to setup a measurements return
	buffer, similar to FeedbackBuffer but with an asynchrounous
	behavior to prevent filling the pipeline with NOP's while waiting
	for the data to be returned.
	
	Note that although the extension has been specified without any
	particular instruments, defining either a device dependent or
	device independent instrument should be as simple as introducing
	an extension consisting primarily of a new enumerant to identify
	the instrument.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/instruments.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_instruments'
GL_INSTRUMENT_BUFFER_POINTER_SGIX = constant.Constant( 'GL_INSTRUMENT_BUFFER_POINTER_SGIX', 0x8180 )
GL_INSTRUMENT_MEASUREMENTS_SGIX = constant.Constant( 'GL_INSTRUMENT_MEASUREMENTS_SGIX', 0x8181 )
glGetInstrumentsSGIX = platform.createExtensionFunction( 
	'glGetInstrumentsSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLint, 
	argTypes=(),
	doc = 'glGetInstrumentsSGIX(  ) -> constants.GLint',
	argNames = (),
)

glInstrumentsBufferSGIX = platform.createExtensionFunction( 
	'glInstrumentsBufferSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLintArray,),
	doc = 'glInstrumentsBufferSGIX( GLsizei(size), GLintArray(buffer) ) -> None',
	argNames = ('size', 'buffer',),
)

glPollInstrumentsSGIX = platform.createExtensionFunction( 
	'glPollInstrumentsSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLint, 
	argTypes=(arrays.GLintArray,),
	doc = 'glPollInstrumentsSGIX( GLintArray(marker_p) ) -> constants.GLint',
	argNames = ('marker_p',),
)

glReadInstrumentsSGIX = platform.createExtensionFunction( 
	'glReadInstrumentsSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint,),
	doc = 'glReadInstrumentsSGIX( GLint(marker) ) -> None',
	argNames = ('marker',),
)

glStartInstrumentsSGIX = platform.createExtensionFunction( 
	'glStartInstrumentsSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(),
	doc = 'glStartInstrumentsSGIX(  ) -> None',
	argNames = (),
)

glStopInstrumentsSGIX = platform.createExtensionFunction( 
	'glStopInstrumentsSGIX', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint,),
	doc = 'glStopInstrumentsSGIX( GLint(marker) ) -> None',
	argNames = ('marker',),
)


def glInitInstrumentsSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )