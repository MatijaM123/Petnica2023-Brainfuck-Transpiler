import copy

f = open("initOutput.txt")
code  = f.readline()
output = []
operacije = ['+', '-', '<', '>']
suprotni = [['+', '-'], ['<', '>'], ['-', '+'], ['>', '<']]
i = 0
preth = ''
for q in range(2):
    output=[]
    for char in code:
        if char == preth and char in operacije:
            output[-1][1]+=1
        else:
            output.append([char, 1])
            preth = char
    stvar = []
    i=0
    for element in output[1:]:
        stvar = []
        stvar.append(output[output.index(element)-1][0])
        stvar.append(element[0])
        if stvar in suprotni:
            element[1]-=output[output.index(element)-1][1]
            output.pop(i)
        else:
            i+=1  
    
    for element in output:
        if element[1]==0:
            output.remove(element)

    for element in output:
        if element[1]<0:
            element[1]=abs(element[1])
            if element[0] == '<':
                element[0] = '>'
            elif element[0] == '<':
                element[0] = '>'
            elif element[0] == '+':
                element[0] = '-'
            elif element[0] == '-':
                element[0] = '+'
    
    code = ''.join([element[1]*element[0] for element in output])

rep_list = [['[', 1], ['-', 1], [']', 1]
i = 0
while rep_list in output:
        if output[i] == rep_list[0] and output[i+1] == rep_list[1] and output[i+2] == rep_list[2]:
                output.remove[i]
                output.remove[i+1]
                output.remove[i+2]
                output.insert(i, ['0', 1])


f = open("code.txt", 'w')
for element in output:
    f.write(str(element[0])+" "+str(element[1])+'\n')
f.close()
