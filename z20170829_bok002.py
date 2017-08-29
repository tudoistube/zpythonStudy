#...네트워크.
import socketserver
import sys
#...socketserver.BaseRequestHandler 상속받음.
#   클라이언트 접속 요청을 처리함.
class MyTcp(socketserver.BaseRequestHandler):
    def handle(self): #...오버라이딩된 콜백.
        print('클라이언트 접속 : {0}'.format(self.client_address[0]))


#...main 에서 실행되면...
#   파이참 터미널 실행해서 이 파일이 있는 폴더에서 python 파일명.py
#   D:\JoyWins\WS_Python\zbasicMore>python z20170829_bok002.py 127.0.0.1
if __name__ == '__main__':
    if len(sys.argv) < 2: #...파일명만 들어올 경우, 서버ip를 안썼다고 알려주고 종료함.
        print('{0}<Bind IP>'.format(sys.argv[0])) #D:/JoyWins/WS_Python/zbasicMore/z20170829_bok002.py<Bind IP>
        sys.exit()
    bindIp = sys.argv[1]
    bindPort = 8888

    #...튜플형태로 들어감.
    server = socketserver.TCPServer((bindIp, bindPort), MyTcp)
    print('Server starts...')
    #...접속대기 : 클라이언트 요청을 기다림.
    server.serve_forever()

"""
실행방법 : server.py [서버ip] #...매개변수 2개.
실행방법 : client.py [서버ip] [클라이언트ip] [내용] #...매개변수 4개.
내가 나에게 나라고 얘기함(ping 해보면 다 됨).
localhost : 대명사.
127.0.0.1 : 대명사.
192.168.0.51 : 내 이름(고유명사).
"""