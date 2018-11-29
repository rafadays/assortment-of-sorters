import random



def sort(a):
    unlist = a   #unlist -> unsorted list
    slist = []  #slist -> sorted list

    slist.append(unlist[0])
    del unlist[0]
    
    max = len(unlist)
    
    for i in range(0 , max):
        t = False
        count = max - len(a) + 1
        for j in range(0 , count):
            if unlist[0] >= slist[count - j - 1]:
                slist.insert(count - j , unlist[0])
                t = True
                break
        if t == False:
            slist.insert(0 , unlist[0])
        del unlist[0]
    print(slist)



def reversesort(a):
    unlist = a   #unlist -> unsorted list
    slist = []  #slist -> sorted list

    slist.append(unlist[0])
    del unlist[0]
    
    max = len(unlist)
    
    for i in range(0 , max):
        t = False
        count = max - len(a) + 1
        for j in range(0 , count):
            if unlist[0] <= slist[count - j - 1]:
                slist.insert(count - j , unlist[0])
                t = True
                break
        if t == False:
            slist.insert(0 , unlist[0])
        del unlist[0]
    print(slist)


def communistsort(a):
    unlist = a   #unlist -> unsorted list
    slist = []  #slist -> sorted list
    gulag = []
    slist.append(unlist[0])
    del unlist[0]
    
    max = len(unlist)
    
    for i in range(0 , max):
        t = False
        count = len(slist)
        for j in range(0 , count):
            if unlist[0] >= slist[count - j - 1]:
                slist.insert(count - j , unlist[0])
                t = True
                break
        if t == False:
            gulag.append(unlist[0])
        del unlist[0]
    slist.append("Stalin")
    print("Good and organized comrades -> " , slist)
    print("Unorganized traitor in the Gulag -> " , gulag)

def unsorter(a):
    unlist = a   #unlist -> unsorted list
    slist = []  #slist -> sorted list

    
    max = len(unlist)
    
    for i in range(0 , max):
        slist.insert(random.randint(0 , len(slist)) , unlist[0])
        del unlist[0]
    print(slist)


my_list = []
for k in range(1 , 20):
    my_list.append(random.randint(-100,100))

print(my_list)
communistsort(my_list)
