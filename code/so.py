f = open("initOutput.txt")
code  = f.readline()
output = []
for i in range(len(code())):
  if(code[i]=='+' or code[i] == '-' or code[i]=='>' or code[i] == '<'):
    z = 1
    p = i
    while abs(code[p] - code [i]) == 2:
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

    
    

output = [[char, 1] for char in code]
g= open("code.txt", 'w')
for element in output:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()