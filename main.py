import os




print('''\033[95m
                                       ##                        ###
                                       ##                         ##
  #####    ######  ##  ##             #####    ####     ####      ##
 ##       ##  ##   ##  ##              ##     ##  ##   ##  ##     ##
  #####   ##  ##   ##  ##              ##     ##  ##   ##  ##     ##
      ##   #####    #####              ## ##  ##  ##   ##  ##     ##
 ######       ##       ##               ###    ####     ####     ####
          #####    #####
\033[0m''')
print(' Por favor ative o modo administrador pra executar esta ferramenta.')
print("")
print("""\033[1;36m
1-hacker ético
2-security
3-coding  \033[1;m""")
print("")
input1 = input(">")
if input1 == 1:
    os.system('apt install nmap')
    os.system('apt install metasploit-framework')    
    os.system('apt-get install hydra-gtk')
    os.system('snap install john-the-ripper')
    os.system('apt-get install aircrack-ng')
    os.system('apt install wireshark-qt')
    os.system('apt-get install git')


if input1 == 2:
    os.system('git clone https://github.com/isaachackandprogramer/SGY-TOOL-security')


if input1 == 3:
   os.system('git clone https://github.com/isaachackandprogramer/SGY-TOOL-CODING')
