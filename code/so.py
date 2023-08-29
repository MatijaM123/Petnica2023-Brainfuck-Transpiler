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
i = 0
while i<len(code):
  z = 0
  if(code[i]=='+' or code[i] == '-' or code[i]=='>' or code[i] == '<'):
    p = i
    while i<len(code) and abs(ord(code[p]) - ord(code[i])) <= 2:
      if(code[p]==code[i]):       
        z+=1
      else:       
        z-=1
      i+=1
    if(z>0):
      output.append([code[p],z])
    elif(z<0):
      match code[p]:
        case '>':
          output.append(['<',-z])
        case '<':
          output.append(['>',-z])
        case '+':
          output.append(['-',-z])
        case '-':
          output.append(['+',-z])
  else:
    output.append([code[i], 1])
    i+=1

nule = find_sub_list([['[', 1], ['-', 1], [']', 1]], output)
for indeksi in nule:
    output[indeksi[0]:(indeksi[1]+1)] = [['0', 1]]

g= open("code.txt", 'w')
for element in output:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()
