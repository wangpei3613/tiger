import time
from multiprocessing import Process
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
mlist = ['尤馨悦','王佩','顾圆圆']

def work(name):
    print(f'给{name}打电话')
    time.sleep(2)
    print(f'给{name}打完电话了')

if __name__ == '__main__':
    # plist=[]
    # for name in mlist:
        # p = Process(target=work,args=(name,))
        # p = Thread(target=work, args=(name,))
        # p.start()
        # plist.append(p)

    # [item.join() for item in plist]

    pool = ThreadPoolExecutor(max_workers=3)
    [pool.submit(work,name) for name in mlist]

    pool.shutdown()

