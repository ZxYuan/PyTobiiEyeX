# A demo for tracking eyedata using Tobii EyeX Controller. 2015.4.3 Yuan
# Tested in Python 2.7.6 (32 bit)
# Dependencies
# 	Tobii.EyeX.Client.dll: an original client library supplied by Tobii
#	MinimalGazeDataStream.dll: A C++ wrapper library for tracking eye based on the client dll above						
# 	python modules: psychopy, win32api

from psychopy import visual, core

from ctypes import *
import win32api

if __name__ == '__main__':
	# Load the dll
	tobii_dll=CDLL('MinimalGazeDataStream.dll')

	# Experiment config
	win = visual.Window()
	msg = visual.TextStim(win, text=u"Hello World!")

	# ========== Trial 1 ==========
	# Start tracking
	tobii_dll.tobii_start(False)

	# Show stimulus and wait for 3 seconds
	msg.draw()
	win.flip()
	core.wait(3)
	win.close()

	# Stop tracking
	tobii_dll.tobii_stop()

	# Save eyedata to file
	tobii_dll.tobii_save("output_1.txt")
	# ========== Trial 1 end ==========

	# ========== Trial 2 ==========
	# Start tracking
	tobii_dll.tobii_start()

	core.wait(3)

	# Stop tracking
	tobii_dll.tobii_stop()

	# Save eyedata to file
	tobii_dll.tobii_save("output_2.txt")
	# ========== Trial 2 end ==========

	# Release the dll
	win32api.FreeLibrary(tobii_dll._handle)
	