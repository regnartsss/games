import numpy as np
from numpy.random import randint as rand
from pprint import pprint

def field_new():
    #    lvl = int(message.text)
    lvl = 5
    k = [4, 2.5, 2, 1.75, 1.6]
    k_k = int(k[lvl - 1] * lvl)
    i = 1
    a = np.ones(k_k*k_k, 'int')
#    print("Размер поля %s" %k_k)
    k = 0
    next = rand(k, k_k)
#    print("Начальная ячейка %s" % next)
    a[next] = 2
    d = [0, k_k]
    stop, r_min, r_max = 10, 1, 10
    while 1 < stop:
#        print(r_min, r_max)
        r = rand(r_min, r_max)
#        print("Следующий ход %s" % r)
#        print("%s --- %s" % (d[0], d[1]))
        if r == 2 or r == 3 or r == 4:
#            print("%s ход на %s" % (d[0],next - 1))
            if d[0] <= next - 1:
                a[next - 1] = 0
#                print("Перешли с %s на ячейку %s" % (next, next - 1))
                next = next - 1
                r_min, r_max = 1, 4
            else:
                r_min, r_max = 5, 6
                pass


        elif r == 5 or r == 6:
            try:
                a[next + k_k] = 0
            except:
                print("Error")
                stop = 1
#            print("Перешли с %s на ячейку %s" % (next, next+k_k))
            next = next + k_k
            d[0] += k_k
            d[1] += k_k
            r_min, r_max = 1, 10

        elif r == 7 or r == 8 or r == 9:
            if d[1] > next + 1:
                a[next + 1] = 0
#                print("Перешли с %s на ячейку %s" % (next, next + 1))
                next = next + 1
                r_min, r_max = 7, 10
            else:
                r_min, r_max = 5, 6
                pass



    #        i+=1

    print(np.count_nonzero(a == 0))
    r = int(np.count_nonzero(a == 0)/lvl-1)
    f = []
    x, y, n = 1, 1, 0
    r_r = r
    print(r)
    s = 0
    while x <= k_k:
        tab = []
        y = 1
        while y <= k_k:
            if a[n] == 0:
                if s == r_r:
                    a[n] = 3
                    tab.append(a[n])
                    r_r += r
                else:
                    tab.append(a[n])

                s+=1
                y += 1
                n += 1
            else:
                tab.append(a[n])
                y +=1
                n +=1

        x +=1
        f.append(tab)
    pprint(f)
    print(s)

field_new()
