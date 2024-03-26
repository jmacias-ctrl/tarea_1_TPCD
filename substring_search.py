import sys
import os

root = "input/En_El_Mar_Remoto.txt"
with open(root, "r", encoding="UTF-8") as file:
    i = 0
    sub = input()
    print(sub)
    count =0
    counts=0
    start=0;
    for line in file:
        
        # Busqueda substring con mayuscula y minuscula

        for i in range(len(line)):
            j = line.find(sub,start)
            if(j!=-1):
                start+= j+1
                count+=1;

        start = 0

        # Busqueda substring sin mayuscula o minuscula

        for i in range(len(line)):
            k = line.lower().find(sub.lower(),start)
            if(k!=-1):
                start+= k+1
                counts +=1;
        
    print(count)
    print(counts)
    