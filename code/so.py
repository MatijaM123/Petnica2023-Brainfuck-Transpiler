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

g= open("code.txt", 'w')
for element in output:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()
