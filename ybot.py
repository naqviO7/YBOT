import os
import time
import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.system('cls')

baner=pyfiglet.figlet_format('YB0T')
print(baner,end=' ')
print('\t\tby naqviO7')


def agreement():
    print('====================================================================================')
    print('\n\t\t [=] Terms of Service [=]')
    print("""
    [!] YOU ARE USING THIS BOT ON YOUR OWN RISK.
    [!] IF YOUR CHANNEL GET BANNED OR DEMONITIZE, YOU WILL BE RESPONSIBLE FOR IT!

    ================================================================================
    
    [!] YOUTUBE TERMS AND CONDITIONS.
        [!] You Are NOT Allowed To:
            Access the Service using any automated means (such as robots, botnets or scrapers) 
            Except !
                [a] In the case of public search engines, in accordance with YouTube’s robots.txt file. 
                [b] With YouTube’s prior written permission. """)


def automate():
    time.sleep(3)
    print('====================================================================================')
    no_of_driver=int(input('[!] Enter Number of Tabs (You Want to OPEN): '))
    url=input('[!] Enter URL of Video: ')
    time_to_refresh=int(input('[!] Enter REFRESH Time (in Seconds): '))

    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('--disable-infobars')

    drivers=[]

    for i in range(no_of_driver):
        drivers.append(webdriver.Chrome(chrome_options=options,executable_path='chromedriver'))
        drivers[i].get(url)

    while True:
        time.sleep(time_to_refresh)
        for i in range(no_of_driver):
            drivers[i].refresh()


if __name__=='__main__':
    time.sleep(4)
    #calling agreement fucntion
    agreement()

    time.sleep(2)
    print('====================================================================================\n')
    risk=input('[!] Do you accept Terms of Service [Yes/No]: ')
    if risk=='yes' or risk=='Yes':
        automate()
    
    elif risk=='no' or risk=='No':
        print('[!] Accept Terms of Service to Continue.')
        
        time.sleep(2)
        print('[!] Quitting.')
        os.system('exit')
    
    else:
        print('[!] Accept Terms of Service to Continue.')
        
        time.sleep(2)
        print('[!] Quitting.')
        os.system('exit')
#ENDOFCODE
