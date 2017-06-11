# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:02:49 2017

@author: Quasar
"""
import matplotlib.pyplot as plt
def threenplusone(n):
    cycles = 0
    while n > 1:
        if n%2 == 0:
            n = n / 2
            cycles += 1
        else:
            n = n * 3 + 1
            cycles += 1
    return cycles

print("Please enter start number")
start_n = int(input())
print("Please enter end number")
end_n = int(input())
vals = []
for i in range(start_n,end_n):
    vals.append(threenplusone(i))
plt.figure(figsize=(15,10))
plt.plot(vals)
plt.title("# of iterations of 3n+1 it takes to reach 1 from " + str(start_n) + " to " + str(end_n))
plt.xlabel("Value of n")
plt.ylabel("# of iterations of 3n+1")
plt.savefig("plot.png")
plt.show()
