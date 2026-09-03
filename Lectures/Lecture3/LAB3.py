
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
print("original list:")
print(Programs)
#append()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.append('Mechanical')
print("append")
print(Programs)

#clear()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.clear()
print("clear")
print(Programs)
#copy()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
NextPrograms = Programs.copy()
print("copy")
print(NextPrograms)

#count()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero', 'Electrical']
total = Programs.count('Electrical')
print("count")
print(total)
#extend()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
newPrograms = ['BioMed', 'Industral', 'Design']
Programs.extend(newPrograms)
print("extend")
print(Programs)
#index()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
currSpot = Programs.index('Computer')
print("index")
print(currSpot)
#insert()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.insert(3, 'Business')
print("insert")
print(Programs)
#pop()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
print(Programs.pop())
print("pop")
print(Programs)

#remove()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.remove('Computer')
print("remove")
print(Programs)

#reverse()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.reverse()
print("reverse")
print(Programs)

#sort()
Programs = ['Electrical', 'Computer', 'Civil', 'Aero']
Programs.sort()
print("sort")
print(Programs)

#generate a random list L of length N compare the performance of the following 
#operations by measuring times with increasing N: N, 2N, 4N, 8N

import random

import time



N = 1000000

while N <= 8000000:
    print("")
    print("Next iteration of N*2")
    L = [random.random () for _ in range(N)]


    start1 = time.perf_counter()

    L.pop()

    end1 = time.perf_counter()
    #Pop takes 0(1) time because it removes the last element of the list
    print("")
    print("pop()")
    print(end1-start1)

    L = [random.random() for _ in range(N)]

    start2 = time.perf_counter()

    L.pop(0)

    end2 = time.perf_counter()
    #Pop takes roughly 0(N) because it has to remove the first element and
    #shift every element to the front of the list
    print("")
    print("pop(0)")
    print(end2-start2 )

    L = [random.random() for _ in range(N)]

    start3 = time.perf_counter()

    L.reverse()

    end3 = time.perf_counter()
    #reverse takes roughly O(N) because it has to interact with every element
    print("")
    print("reverse()")
    print(end3-start3 )

    L = [random.random() for _ in range(N)]

    start4 = time.perf_counter()

    R = L[::-1]

    end4 = time.perf_counter()
    #reverse takes roughly O(N) but this is slightly longer because
    #it has to create a new List as well
    print("")
    print("R list")
    print( end4-start4 )
    N = 2*N

