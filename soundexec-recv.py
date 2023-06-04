#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# SoundExec (receiver app) - component 2 of 2
#
# Tool for executing commands and clipboard manipulation over-the-air without the need for wires or internet
#
# Usage
# $ ./soundexec-recv.py
#

import os
import sys
import ggwave
import pyaudio
import pyperclip

# receiver config
EXECUTE_CMD = False
CLIPBOARD = True

# general config
CHANNELS = 1
RATE = 48000
FPB = 4096

BUFFER = 1024

def main():
	pya = pyaudio.PyAudio()

	stream = pya.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FPB)

	print("Listening...")

	instance = ggwave.init()

	try:
		while True:
			data = stream.read(BUFFER, exception_on_overflow=False)
			result = ggwave.decode(instance, data)

			if(not result is None):
				try:
					text = result.decode("utf-8")

					if(EXECUTE_CMD):
						print("EXECUTE_CMD: %s" % text)

						try:
							os.system(text)
						except:
							pass

					if(CLIPBOARD):
						print("CLIPBOARD: %s" % text)

						try:
							pyperclip.copy(text)
							#pyperclip.paste(text)
						except:
							pass
				except:
					pass

	except KeyboardInterrupt:
		pass

	ggwave.free(instance)

	stream.stop_stream()
	stream.close()

	pya.terminate()

	return

if(__name__ == '__main__'):
	main()
