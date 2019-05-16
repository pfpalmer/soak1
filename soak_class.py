from time import sleep
from  datetime import datetime
import pexpect
import os
from selenium import webdriver

#hostname = "192.168.1.254"
# response = os.system("ping -c 3 192.168.1.254")
#response = os.system("ping -c 3 " + hostname)


class SoakClass:
    def __init__(self):
        self.youtube_session = None
        self.telnet_cli_session = None

    def ping_rg(self):
        if response == 0:
            #now1 = datetime.now()%S:%f")
            print("Successfully pinged RG: " + s1)
        else:
            print("Ping to RG failed")        #you_tube_music_url = 'https://172.217.gin_599')

    def soak_login_599(self):
        self.telnet_cli_session = pexpect.spawn("telnet 192.168.1.254",encoding='utf-8')
        self.telnet_cli_session.expect("ogin")
        self.telnet_cli_session.sendline("admin")
        self.telnet_cli_session.expect("ord:")
        self.telnet_cli_session.sendline("<<01%//4&/")
        self.telnet_cli_session.sendline("magic")
        self.telnet_cli_session.expect(">")
        print('leaving login_599')
        # test

    def stn_connect_to_youtube_music(self):
        soak.youtube_session = webdriver.Chrome()
        soak.youtube_session.get("https://www.youtube.com/watch?v=nPJo5uMlV5w")

soak = SoakClass()
while True:
    soak.stn_connect_to_youtube_music()
    sleep(600)
    # soak.session.close()
    #soak.telnet_cli_session = soak.login_599()
    soak.soak_login_599()
    soak.telnet_cli_session.sendline('!')
    soak.telnet_cli_session.expect('#')
    soak.telnet_cli_session.sendline('free')
    soak.telnet_cli_session.expect('#')
    free_str = soak.telnet_cli_session.before
    print('free str:' + free_str)
    now = datetime.today().isoformat()
    soak_file = open('/var/log/soak/soak_file.txt', 'a')
    soak_file.writelines('Memory stats from Free Command Date: '+ now)
    soak_file.writelines(free_str)
    soak_file.writelines('')
    soak_file.close()
    soak.youtube_session.close()
    soak.telnet_cli_session.close()

    sleep(20)

