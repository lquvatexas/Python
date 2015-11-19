# For this program, I will write a function isMagic() that will determine if a 2-D list forms a magic square. The function should be general enough to accept magic squares of any size greater than or equal to 3.
def isMagic(a):
	#check dimension of 2-D list
	n=len(a)

	#check the canonical sum
	canon_sum=n*(n*n+1)//2

	#check sum of each row
	for i in range (len(a)):
		sum_row=0
		for j in range(len(a[i])):
			sum_row+=a[i][j]
			if sum_row!=canon_sum:
				return "invalid"

	#check sum of each column
	for j in range(len(a[0])):
		sum_col=0
		for i in range(len(a)):
			sum_col+=a[i][j]
			if sum_col!=canon_sum:
				return 'invalid'

	#check sum of diagonal left to right
	sum_lr=0
	for i in range (len(a)):
		sum_lr+=a[i][i]
	if sum_lr!=canon_sum:
		return "invalid"

	#check sum of diagonal right to left
	sum_rl=0
	for j in range (len(a[0])):
		sum_lr+=a[n-1-j][j]
	if sum_lr!=canon_sum:
		return "invalid"

	return True

def main():
	#open file for reading
	in_file=open("squares.txt","r")
	#open file for writing
	out_file=open("results.txt","w")
	#read number of squares
	num_squares=in_file.readline()
	num_squares=num_squares.strip()
	

	

	num_squares=int(num_squares)
	out_file.write(str(num_squares)+'\n')

	#process each square separately
	for i in range(num_squares):
		blank=in_file.readline()

		#read the dimension of the square
		dim=in_file.readline()
		dim=dim.strip()
		y=dim
		dim=int(dim)

		#create a 2-D list and check if it is magic
		a=[]
		oldline=''
		for i in range(dim):
			b=in_file.readline()
			oldline=oldline+b
			
			
			b=b.strip()
			
			b=b.split()
			for k in range (len(b)):
				b[k]=int(b[k])
			a.append(b)
		

		
		#check if it is Magicsquares
		if isMagic(a):
			out_file.write(y+' valid'+'\n')
			out_file.write(oldline+'\n')


		#print the result	
		else:
			out_file.write(y+' invalid'+'\n')
			out_file.write(oldline+'\n')
	    
			 
	in_file.close()
	out_file.close()
	print(' The output has been written to results.txt')
main()






