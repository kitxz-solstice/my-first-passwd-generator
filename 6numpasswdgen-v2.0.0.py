import random
import sys
import time

sn = 100000 #(start) min number
fn = 999999 #(finish) max number
alg11 = 50000 #(start) min algorithm number
alg12 = 949999 #(finish) max algorithm number
alg20 = 70000 #alorithm 2
alg30 = 20000 #algorithm 3
alg40 = 1100 #alghoritm 4
alg50 = 9999 #algoritm 5
alg60 = 100 #a

print("type 1 for generate new 6 numbers passwords")
print("type 2 for generate new 4 numbers passwords")
print("type 3 for exit")
print("Thank you for using my program")

while True:
    choice = input("> ").strip()

    if choice == '1': #6 numbers password
 
        time.sleep (0.5)

        n1 = random.randint(alg11, alg12) #number 1 for algorithm
        n2 = n1 + alg20
        n3 = n2 -  alg30
        n4 = random.randint(sn, fn) #password 2

        print("Your passwords:", n1, n2, n3, n4)
    if choice == '2': #4 numbers password

        time.sleep(0.5)

        n5 = random.randint(alg40, alg50)
        n6 = n5 - alg60
        n7 = random.randint(alg40, alg50)

        print("Your passwords: ", n5, n6, n7)

    if choice == '3': #exit
        sys.exit()
