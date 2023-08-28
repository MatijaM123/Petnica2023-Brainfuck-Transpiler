f = open("initOutput.txt")
code  = f.readline()
output = [[char, 1] for char in code]
g= open("code.txt", 'w')
for element in output:
  g.write(str(element[0]) + ' ' + str(element[1]) + '\n')
g.close()
