f = open("initOutput.txt")
code  = f.readline()
output = [[char, 1] for char in code]
for element in output:
  f.write(element[0] + ' ' + element[1] + '\n')
f.close()
