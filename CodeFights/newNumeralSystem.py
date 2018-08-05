def newNumeralSystem(number):
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXY'

ind=alphabet.index(number)+1
ind1=alphabet.index(number)+1
if ind%2==0:
    ind=ind/2
else:
    ind=ind/2+1 
lista=[]

for i in alphabet[:ind]:
    lista.append(i+" + "+alphabet[ind1-1])
    ind=ind-1
    ind1=ind1-1

return lista

