import random
import pyperclip
sn = 100000 #(start) min number
fn = 999999 #(finish) max number
alg11 = 50000 #(start) min algorithm number
alg12 = 949999 #(finish) max algorithm number
alg20 = 70000 #alorithm 2 number
alg30 = 20000 #algorithm 3 number

n1 = random.randint(alg11, alg12) #number 1 for algorithm
print("base number =")
print(n1)

n2 = n1 + alg20
print("number algorithm 1 =")
print(n2)

n3 = n2 -  alg30
print("number alghoritm 2 =")
print(n3)

print("Final Password is")
print(n3)
print("Your password was generated! Thank you for use! :)")

