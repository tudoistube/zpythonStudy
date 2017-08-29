import socket
if __name__ =='__main__':
    sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #sc.bind(('192.168.219.111',0))

    try:
        sc.connect(('192.168.0.24',9900))
    finally:
        sc.close()