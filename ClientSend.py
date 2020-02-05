
import threading

import pyaudio


def Record():
    """New Method"""
    PortToListen = pyaudio.PyAudio()
    Listen = PortToListen.open(rate=fs,
                               channels=Channels,
                               format=Format,
                               input=True,
                               frames_per_buffer=Chunk,
                               output=False)
    while True:
        RecordBuff.append(Listen.read(Chunk, exception_on_overflow=False))


def Send(IP, Socket):
    while True:
        if len(RecordBuff) == 0:
            continue
        else:
            # print(len(RecordBuff[-1]))
            Socket.sendto(RecordBuff.pop(0), 0, IP)


def SendMsg(IP, Socket):
    T1 = threading.Thread(target=Send, args=(IP, Socket, ))
    T2 = threading.Thread(target=Record, args=())
    T2.start()
    T1.start()
    T1.join()
    T2.join()


fs = 14400
# Sec = 0.85
RecordBuff = []
Chunk = 1024
Channels = pyaudio.PyAudio().get_default_input_device_info()["maxInputChannels"]
Format = pyaudio.paInt16
