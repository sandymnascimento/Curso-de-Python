import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com')
except:
    print('\033[31mO site Facebook não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Facebook com sucesso.\033[m')