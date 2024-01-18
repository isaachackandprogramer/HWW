import os

print('''
###                                   ##                        ###
 ##                                   ##                         ##
  ##      ##   ##  ##   ##            #####    ####     ####      ##
  #####   ## # ##  ## # ##             ##     ##  ##   ##  ##     ##
  ##  ##  #######  #######             ##     ##  ##   ##  ##     ##
  ##  ##  #######  #######             ## ##  ##  ##   ##  ##     ##
 ###  ##   ## ##    ## ##               ###    ####     ####     ####''')
print('Por favor ative o modo administrador pra executar esta ferramenta.')

um = input('1-')

if um == "1":
    print('instalando')
os.system('apt-get update && sudo apt-get upgrade')
os.system('apt install nmap')
os.system('apt-get install nikto -y')

print("obrigado por usar só usei pra passar tempo kk")
