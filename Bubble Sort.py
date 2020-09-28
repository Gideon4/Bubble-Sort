import random

def sort(listo):
    for i in range(len(listo)):
        for j in range(len(listo)-1-i):
            if listo[j]>listo[j+1]:
                num=listo[j]
                listo.pop(j)
                listo.insert(j+1,num)
    print(listo)

def generatelist(length,rangeo):
    return [random.randint(0,rangeo) for i in range(length)]

sort(generatelist(4096,65536))
