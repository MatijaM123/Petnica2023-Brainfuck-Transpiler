from os import write
import numpy as np
putanja = 'code.txt'


with open(putanja, "r") as rf:
    with open('output.py', "w") as wf:
        linije = rf.readlines()
        linija = [list(map(str, linije[i].split())) for i in range (len(linije))]
        i = 0
        uvlacenje = 0
        wf.write("import numpy as np\nniz = np.zeros(30000, dtype=int)\ni=0\n")
        for komanda in linija:
            match komanda[0]:
                case '>':
                    wf.write(uvlacenje*"\t"+"i +="+komanda[1]+"\n")
                case '<':
                    wf.write(uvlacenje*"\t"+"i -="+komanda[1]+"\n")
                case '+':
                    wf.write(uvlacenje*"\t"+"niz[i] +="+komanda[1]+"\n")
                case '-':
                    wf.write(uvlacenje*"\t"+"niz[i] -="+komanda[1]+"\n")
                case '.':
                    wf.write(uvlacenje*"\t"+"print(chr(niz[i]), end = '')\n")
                case ',':
                    wf.write(uvlacenje*"\t"+"niz[i]=ord(input())\n")
                case '[':
                    wf.write(uvlacenje*"\t"+"t = i\n"+uvlacenje*"\t"+"while niz[t] != 0 :\n")
                    uvlacenje+=1
                case ']':
                    uvlacenje -= 1
        wf.write("print(\n)")            
            

