import socket
import threading
import Recv
import Send

""" do this in terminal in mac after a reboot "mudo sysctl -w net.inet.udp.maxdgram=65535" """


if __name__ == "__main__":
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Created Socket")
    Port = 8081
    # Socket.bind(("103.99.148.169", Port))
    Socket.bind(("192.168.1.100", Port))
    print("Binded Successfully and now waiting")
    print(Socket.getsockname())
    ClientIP = Socket.recvfrom(256, 0)
    # ClientIP = RecvBuffer[1]
    if ClientIP[0].decode("ascii") == "CALL":
        print(ClientIP)
        Socket.sendto(bytes("ACK", 'ascii'), 0, ClientIP[1])
        ProcessOne = threading.Thread(target=Recv.RecvMsg, args=(Socket,))
        ProcessTwo = threading.Thread(target=Send.SendMsg, args=(ClientIP[1], Socket, ))
        ProcessOne.daemon = True
        ProcessTwo.daemon = True
        ProcessTwo.start()
        ProcessOne.start()
        while True:
            if input("Press 0 to hang up the call : ") == '0':
                exit(0)
    else:
        print("Failed!")
