def adjacentElementsProduct(inputArray):
# Code with a cycle for that returns the max element with p
#p=[]
#for i in range(len(inputArray)-1):
# p.append(inputArray[i]*inputArray[i+1])

#return max(p)

# The same results but the code with list comprehension
return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)])

