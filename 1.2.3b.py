

 # imports defined function from lib
import sys

file_in = open("sourcecode.txt")
bl = 8

bitlist = map(int,''.join(file_in.read().split()))

i = ''.join([chr(sum(bit<<abs(idx-bl)-1 
                     for idx,bit in enumerate(y)))
             for y in zip(*[bitlist[x::bl] 
                            for x in range(bl)])
             ])
print(i)