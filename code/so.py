f = open("initOutput.txt")
code  = f.readline()
fajl = [[k, 1] for k in code]
f.close()
output = []
i = 0
izmenjen = True
while izmenjen:
  izmenjen = False
  output = []
  while i<len(fajl):
    z = 0
    if(fajl[i][0]=='+' or fajl[i][0] == '-' or fajl[i][0]=='>' or fajl[i][0] == '<'):
      p = i
      while i<len(fajl) and abs(ord(fajl[p][0]) - ord(fajl[i][0])) <= 2:
        if(fajl[p][0]==fajl[i][0]):       
          z+=fajl[i][1]
        else:       
          z-=fajl[i][1]
        i+=1
      if(z>0):
        output.append([fajl[p][0],z])
      elif(z<0):
        match fajl[p][0]:
          case '>':
            output.append(['<',-z])
          case '<':
            output.append(['>',-z])
          case '+':
            output.append(['-',-z])
          case '-':
            output.append(['+',-z])
      else:
        izmenjen = True
    else:
      output.append([fajl[i][0], 1])
      i+=1
  fajl = output

rep_list1 = [['[', 1], ['-', 1], [']', 1]]
rep_list2 = [['[', 1], ['+', 1], [']', 1]]
i = 0
while rep_list1 in fajl:
        if fajl[i] == rep_list1[0] and fajl[i+1] == rep_list1[1] and fajl[i+2] == rep_list1[2]:
                fajl.remove[i]
                fajl.remove[i+1]
                fajl.remove[i+2]
                fajl.insert(i, ['0', 1])
i = 0
while rep_list2 in fajl:
        if fajl[i] == rep_list2[0] and fajl[i+1] == rep_list2[1] and fajl[i+2] == rep_list2[2]:
                fajl.remove[i]
                fajl.remove[i+1]
                fajl.remove[i+2]
                fajl.insert(i, ['0', 1])
          
g= open("code.txt", 'w')
for element in fajl:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()
