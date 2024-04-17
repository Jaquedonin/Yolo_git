from threading import Thread
import time
# import win32process

arquivo = open('speed3.text' , 'a')
#define thread
class Th(Thread):
    def __init__ (self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        for i in range(3):
            print("hellow")
            # aux_inserir = str(soma)+ "\n"
            # arquivo.write(aux_inserir)
            time.sleep(3)


#create and call a thread
a = Th(1)
a.start()