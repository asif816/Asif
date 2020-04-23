import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
urls = ['https://gplinks.co/Zs7Ogkj']
k = PyKeyboard()

while count 100:
       for url in urls:
             webbrowser.open(url, new=0)
             time.sleep(1 0)
             k.press_keys(['Command','W'])
             count = count + 1

else:
        pass
