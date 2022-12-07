from unidecode import unidecode
f=open('input.txt', 'r')
lines = unidecode(f.read().lower())

x = lines.split()
l = list(dict.fromkeys(x))
l = sorted(l)

with open("output.txt", "w") as output:
    for i in range(len(l)):
        if(i+1 == len(l)):
            output.write(l[i])
        else: 
            output.write(l[i] + "\n")

f=open('output.txt', 'r')
lines = unidecode(f.read().lower())
voc = lines.split()

f2=open('input2.txt', 'r')
lines2 = unidecode(f2.read().lower())

x2 = lines2.split()
l2 = list(dict.fromkeys(x2))
l2 = sorted(l2)

bag = []
for i in voc:
    if i in l2:
        bag.append(1)
    else:
        bag.append(0)

with open("output2.txt", "w") as output2:
    for i in range(len(bag)): 
            output2.write(str(bag[i]) + " ")