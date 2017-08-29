import socket #...클라이언트는 socket 필요.

if __name__ == '__main__':
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #...인터넷통신, TCP 통신.
    #...클라이언트에 답을 하기 위해 필요함.
    # ...0번 포트는 없으나, 운영체제가 임의로 할당해줌.
    sc.bind(('192.168.0.51', 0))#...튜플형태임.클라이언트자신의 ip, 0번 포트.

    try:
        sc.connect(('192.168.0.24', 9900)) #...튜플형태임.서버IP, Port.
    finally:
        sc.close()


