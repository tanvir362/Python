import time
import threading

def funa(q, a):
    for i in range(5):
        time.sleep(1)
        q.append(('a', i))
        print(('a', i), file=a, flush=True)
    a.close()

def funb(q, b):
    for i in range(5):
        time.sleep(1)
        q.append(('b', i))
        print(('b', i), file=b, flush=True)
    b.close()


if __name__ == '__main__':
    a = open('ato.txt', 'w')
    b = open('bto.txt', 'w')


    q = []
    # funa(q)
    # funb(q)
    t1 = threading.Thread(target=funa, args=[q, a])
    t1.setDaemon(True)
    t2 = threading.Thread(target=funb, args=[q, b])
    t2.setDaemon(True)

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()

    print(q)
