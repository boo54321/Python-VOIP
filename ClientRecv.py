import threading
import pyaudio


def Recv(Socket):
    while True:
        RecvBuff.append(Socket.recvfrom(65535, 0))
        # print(len(RecvBuff[-1][0]))


 
def Player():
    """New Method"""
    PortToListen = pyaudio.PyAudio()
    Play = PortToListen.open(rate=fs,
                             channels=Channels,
                             format=Format,
                             input=False,
                             frames_per_buffer=Chunk,
                             output=True)
    while True:
        if len(RecvBuff) == 0:
            continue
        else:

            RecvTemp = RecvBuff.pop(0)[0]
            # print(len(RecvTemp))
            Play.write(RecvTemp)


def RecvMsg(Socket):
    T1 = threading.Thread(target=Recv, args=(Socket, ))
    T2 = threading.Thread(target=Player, args=())
    T1.start()
    T2.start()
    T1.join()
    T2.join()


fs = 14400
# Sec = 0.85
RecvBuff = []
Chunk = 1024
Channels = pyaudio.PyAudio().get_default_output_device_info()["maxOutputChannels"]
Format = pyaudio.paInt16
