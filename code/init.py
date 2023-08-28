operators = ['<', '>', '+', '-', '[', ']', '.', ',']
code = ''

with open('Brainfuck.bf') as file:
  line = file.readline()
  for char in line:
    if char in operators:
      code += char

f = open('initOutput.txt', 'w')
f.write(code)
f.close()
