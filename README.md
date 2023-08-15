# SoundExec
SoundExec is a tool for executing commands, file transfer and clipboard manipulation over-the-air without the need for wires or internet.

It's important to understand the risks, especially if you believe you have an "air-gapped" machine, but it can still send/recv audio. This is a fun little experiment in side channels and awareness for "audio-gapping". Understand that this is a basic script that can be used to demonstrate file transfer, sliding in the copy/paste clipboard buffer and remote control of a machine that has already been compromised, but is without internet access.

# How it works

![soundexec-diagram](https://github.com/rhmaxdotorg/soundexec/assets/100790377/640aa69b-da25-4dd9-8886-cf2d3c4d19e6)

There are **two components**, transmitter (send) and receiver. 

The **transmitter** component sends text OR file to a listening receiver. The **receiver** component then executes it as a command OR puts it in the clipboard buffer. The transmitter can be on one computer across the room from another computer that is running the receiver. This works as long as the receiver has a microphone, the transmitter has a speaker that is loud enough for the receiver to clearly hear and parse the data.

# Why do this research

First, you can't defend against attacks without knowing how they work and their limitations. Intellectual honesty and genuine curosity is important and awesome.

Second, if you understand how this works, you also can see that the risk of anyone actually using it in the field is low. Someone needs compromise your computer and then install the receiver on it, without you noticing AND be physically close enough to the computer for it to listen and catch the audio to even work. Clearly this is for educational purposes, built from example code and it's all using [open source software that](https://github.com/ggerganov/ggwave) has been around for years.

Third, you're much more likely to get hacked by using Windows or an outdated browser, having a false sense of security by assuming that using a VPN secures your PC or clicking on links from DMs. This is just more of a party trick than anything else.

# Use cases
- Put text in the clipboard buffer on the receiver computer
- Execute a command on the receiver computer
- Read the contents of a small file using the transmitter and send it to the receiver computer (140 bytes limit)

# Setup and Dependencies

## Windows
- Install python3 and [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/)
- Install python packages

`$ pip install ggwave pyaudio pyperclip`

Note: it appears now that ggwave is failing to properly build on Windows and it's unclear if we have a solution or workaround. But Linux has still been working fine. Fixes or further guidance welcome via testing and code updates via pull requests!

### Debugging
If you get "Unanticipated host error", it usually means you need to allow microphone access. Settings -> Microphone -> Make sure it's enabled and especially "Allow desktop apps to access your microphone" is On.

If you see "Failed to capture sound data" then move closer to the receiver or play the transmitter loud enough.

## Linux
- Install apt packages (Ubuntu)

`$ sudo apt install -y portaudio19-dev python3-pyaudio xclip xsel`

- Install python packages

`$ pip install ggwave pyaudio pyperclip`

# How to use it
**Step 1**

After installing all the dependencies, put the transmitter (soundexec-send.py) on a computer running Windows or Linux (Mac untested) and the receiver (soundexec-recv.py) on another computer.

Ensure speakers and microphones are working.

**Step 2**

Use command line terminal to run the receiver FIRST.

On Windows, `python soundexec-recv.py` and on Linux `./soundexec-recv.py` and if it started successfully, it will say *listening...* along with some debug messages.

**Step 3**

Edit the transmitter code to pick an option: copy the text/file to clipboard OR execute a command.

```
# receiver config
EXECUTE_CMD = False
CLIPBOARD = True
```

If you want to use the clipboard feature (default), you don't need to change anything. However, if you want to execute a command, change EXECUTE_CMD from False to True and CLIPBOARD from True to False.

**Step 4**

And run the transmitter. On Windows, `python soundexec-send.py test` and on Linux `./soundexec-send.py test` for example.

If you chose to copy send text to the receiver's clipboard, go paste something into notepad or a browser, you should see what the transmitter sent. If you chose to execute a command (and it was a valid OS command), such as "calc" on windows, you should see a calculator pop up on the receiever's screen. Neat huh!

# FAQ

**Is this an exploit?**

No, it's just a way to transmit data over sound waves from one computer to another. Your computer needs to run the receiever and the other computer be physically close enough to hear and interpret the sounds for it to even to work. The result is no different than using any other file or data transfer protocol, but it has even more limitations.

Again, this is educational, not super practical but yes, it still feels like magic.

**Where can I find more information on how this works?**

https://github.com/ggerganov/ggwave#ggwave

# Disclaimer
All the code and info in this repo is for EDUCATIONAL PURPOSES ONLY. Author bears no responsibility or liability for how it is used and do not use it for harm or bad stuff. Use to learn how technology and security works to assess your risk profile and protect yourself.
