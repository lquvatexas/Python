# This assignment is used to check whether an ISBN for a book is valid or not by using the given algorithm.

#Creating a function to calculate the partial sum
def partial_sum(s):
    for i in range (len(s)):
        if i==0:
           s[i]=int(s[i])
        else:
          if s[i]=='X' or s[i]=='x':
            s[i] = 10
          s[i] = int(s[i-1]) + int(s[i])
    return s

def main():
# open the file for reading
  in_file = open ("isbn.txt", "r")
  out_file = open ("isbnOut.txt","w")

#count the number of the isbns in the file
  for line in in_file:
    line=line.strip()
    old_line = line
    line=line.replace('-','')

#to calculate the isbn by partial_sum function
    s=list(line)
    s1 = partial_sum(s)
    s2 = partial_sum(s1)
    div=s2[-1]
        
#check isbn vaild or not      
   
    if div%11==0:
      out_file.write(old_line + '   Valid\n')
			
    else:
      out_file.write(old_line + '   Invalid\n')
			
# close file
  in_file.close()
  out_file.close()

main()

