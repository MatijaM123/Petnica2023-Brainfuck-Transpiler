def find_sub_list(sl,l):
    results=[]
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            results.append((ind,ind+sll-1))

    return results

f = open("initOutput.txt")
code  = f.readline()
output = []
operacije = ['+', '-', '<', '>']
suprotni = [['+', '-'], ['<', '>']]
i = 0
preth = ''
for komanda in code:
    if [komanda, preth] in suprotni or [komanda,preth][::-1] in suprotni:
        output[-1][1] -=1
    elif komanda == preth and komanda in operacije:
        output[-1][1] +=1
    else:
        output.append([komanda, 1])
        preth = komanda
        
nule = find_sub_list([['[', 1], ['-', 1], [']', 1]], output)
for indeksi in nule:
    output[indeksi[0]:(indeksi[1]+1)] = [['0', 1]]

g= open("code.txt", 'w')
for element in output:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()
