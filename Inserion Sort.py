# Insertion Sort 
a=[6,5,3,1,8,7,2,4]

print("Actual Array "+str(a))
for j in range(1,len(a)):
	print(" ")
	print("Iteration "+str(j))
	print("*"*10)
	key=a[j]
	print("Key "+str(key))
	print("current array " + str(a))
	i=j-1
	while key<a[i] and i>-1:
		a[i+1]=a[i]
		i-=1
	a[i+1]=key
	print("After insertion "+str(a))

	j+=1
print(" ")
print("Final Array "+ str(a))