import threading 
import time
import random
write=threading.Lock()
mutex=threading.Lock()
readcount=0

def reader(n):
    global mutex
    mutex.acquire()
    global readcount
    global write
    readcount=readcount+1
    if readcount==1:
        write.acquire()
    mutex.release()
    print("Reader {} is reading file\n".format(n))
    time.sleep(2)
    mutex.acquire()
    readcount=readcount-1
    if readcount==0:
        print(readcount)
        write.release()
    mutex.release()

def writer(n):
    global write
    write.acquire()
    print("Writer {} is writing into the file\n".format(n))
    print("Writer {} is  closing the file\n".format(n))
    time.sleep(2)
    write.release()

for i in range(0, 20):
        randomNumber = random.randint(0, 100)  
        if(randomNumber > 50):
            Thread1 = threading.Thread(target = reader,args=(i,))
            Thread1.start()
        else:
            Thread2 = threading.Thread(target = writer,args=(i,))
            Thread2.start()

Thread1.join()
Thread2.join()





