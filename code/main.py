from os import write
import numpy as np
putanja = 'code.txt'


with open(putanja, "r") as rf:
    with open('output.py', "w") as wf:
        linije = rf.readlines()
        linija = [list(map(str, linije[i].split())) for i in range (len(linije))]
        i = 0
        uvlacenje = 0
        wf.write("import numpy as np\nniz = np.zeros(100000, dtype=int)\ni=0\n")
        for komanda in linija:
            match komanda[0]:
                case '>':
                    wf.write(uvlacenje*"\t"+"i +="+komanda[1]+"\n")
                case '<':
                    wf.write(uvlacenje*"\t"+"i -="+komanda[1]+"\n")
                case '+':
                    wf.write(uvlacenje*"\t"+"niz[i] = (niz[i]+"+komanda[1]+")%256\n")
                case '-':
                    wf.write(uvlacenje*"\t"+"niz[i] = (niz[i]-"+komanda[1]+")%256\n")
                case '.':
                    wf.write(uvlacenje*"\t"+"print(chr(niz[i]), end = '')\n")
                case ',':
                    wf.write(uvlacenje*"\t"+"niz[i]=ord(str(input(\"Unos:\")))\n")
                case '[':
                    wf.write(uvlacenje*"\t"+"while niz[i] != 0 :\n")
                    uvlacenje+=1
                case ']':
                    uvlacenje -= 1
                case '0':
                    wf.write(uvlacenje*"\t"+"niz[i]=0\n")
        wf.write("print(\n)")            
            
