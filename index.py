A = int(input("Enter number: "))
p,q = [],[]

for i in range(A+1):
	for j in range (A+1):
		if (i*i + j*j) == A:
			a,b = i,j
			p.append(a)
			q.append(b)
			if b in p and a in q: continue
			print(' (a,b)=({},{})'.format(a,b))
