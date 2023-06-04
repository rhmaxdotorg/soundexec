#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# SoundExec (transmitter app) - component 1 of 2
#
# Tool for executing commands, file transfer and clipboard manipulation over-the-air without the need for wires or internet
#
# Usage
# $ ./soundexec-send.py "text to send" OR filename.txt
#

import os
import sys
import ggwave
import pyaudio

# config
ARGS = 1

PROTOCOL_ID = 1
VOLUME = 20

CHANNELS = 1
RATE = 48000
FPB = 4096

def main():
	if(len(sys.argv) != 2):
		print("Usage: %s \"text to send\" OR filename.txt\n" % sys.argv[0])
		return

	if(os.path.isfile(sys.argv[1])):
		text = readFile(sys.argv[1])
	else:
		text = sys.argv[1]

	pya = pyaudio.PyAudio()
	wave = ggwave.encode(text, protocolId=PROTOCOL_ID, volume=VOLUME)

	stream = pya.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=FPB)

	stream.write(wave, len(wave)//4)
	stream.stop_stream()
	stream.close()

	pya.terminate()

	print("sent!")

	return

def readFile(path):
	try:
		file = open(path, 'r')
		content = file.read()
	except:
		pass

	return content

if(__name__ == '__main__'):
	main()
