import socket
import threading
import ClientSend
import ClientRecv


if __name__ == "__main__":
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
    # Port = 8080
    Socket.bind(("192.168.0.166", 4444))
    ServerIP = "192.168.0.159"
    # ClientIP = RecvBuffer[1]
    Socket.sendto(bytes("CALL", 'ascii'), 0, (ServerIP, 8080))
    print(Socket.getsockname(), Socket.getsockname())
    print("Waiting for ACK")
    Server = Socket.recvfrom(256, 0)
    if Server[0].decode("ascii") == "ACK":
        print("ACK-ed")
        ProcessOne = threading.Thread(target=ClientRecv.RecvMsg, args=(Socket, ))
        ProcessTwo = threading.Thread(target=ClientSend.SendMsg, args=((ServerIP, 8080), Socket, ))
        ProcessOne.daemon = True
        ProcessTwo.daemon = True
        ProcessTwo.start()
        ProcessOne.start()
        while True:
            if '0' == input("Press 0 to hang up the call : "):
                exit(0)
    else:
        print("Failed!")

