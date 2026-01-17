from threading import Thread
def raqam_yigindi(n):
    s = 0
    while n > 0:
        raqam = n % 10
        s += raqam
        n = n // 10
    print(s)
th = Thread(target=raqam_yigindi,args=(108,))
th.start()
th.join()

def katta_q(names):
    lists = []
    for i in names:
        lists.append(i.capitalize())
    print(lists)
th = Thread(target=katta_q,args=(['alfred', 'tabitha', 'william', 'arla'],))
th.start()
th.join()


def baholar(scores):
    print(list(filter(lambda i: i > 75, scores)))
th = Thread(target=baholar,args=([66, 90, 68, 59, 76, 60, 88, 74, 81, 65],))
th.start()
th.join()

def palindromlar(words):
    x = []
    for word in words:
        lo_wor = word.lower()
        if lo_wor == lo_wor[::-1]:
            x.append(word)
    print(x)
th = Thread(target=palindromlar,args=(['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom'],))
th.start()
th.join()

def matn_n(matn):
    i,x = 0,""
    while i < len(matn):
        if matn[i].lower() == 'e':
            x += "3"
        else:
            x += matn[i]
            i += 1
    print(x)
th = Thread(target=matn_n,args=(["salom aleeeee  00 eee "],))
th.start()
th.join()
def matns_n(matn):
    x,i = "" , 0
    while i < len(matn):
        if matn[i] != ' ':
           x += matn[i]
           i += 1
    print(f"matn {x}")
th=Thread(target=matns_n,args=(["matn eee akiaddd djddd dddd "],))
th.start()
th.join()
def raqamlar(raqamlar):
     kara = []
     for i in raqamlar:
         kara.append(i * 2)
     print(kara)
th = Thread(target=raqamlar,args=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],))
th.start()
th.join()
