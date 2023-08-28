from os import write
import numpy as np
putanja = input()


with open(putanja, "r") as rf:
    with open(putanja, "w") as wf:
        linija = rf.readline()
        i = 0
        uvlacenje = 0
        wf.write("import numpy as np\nniz = np.zeros(30000, dtype=chr)\n")
        for komanda in linija:
            match komanda:
                case '>':
                    wf.write(uvlacenje*"\t"+"i += 1\n")
                case '<':
                    wf.write(uvlacenje*"\t"+"i -= 1\n")
                case '+':
                    wf.write(uvlacenje*"\t"+"niz[i] += 1\n")
                case '-':
                    wf.write(uvlacenje*"\t"+"niz[i] -= 1\n")
                case '.':
                    wf.write(uvlacenje*"\t"+"print(niz[i])\n")
                case ',':
                    wf.write(uvlacenje*"\t"+"niz[i]=ord(input())\n")
                case '[':
                    wf.write(uvlacenje*"\t"+"t = i\n"+uvlacenje*"\t"+"while niz[t] != 0 :\n")
                    uvlacenje+=1
                case ']':
                    uvlacenje -= 1
                    
            


