Given an m by n grid of letters, and a list of words, find the location in the grid where the word can be found. A word matches a straight, contiguous line of letters in the grid. The match could either be done horizontally (left or right) or vertically (up or down). We will not consider words that can be matched diagonally.

The input will be in a file called hidden.txt and your output will be written to a file called found.txt. The format of the input file will be as follows:

First line will have two integers - m, the number of lines in the grid and n, the number of characters in each line. The integers m and n will be separated by one or more spaces.
There will be a single blank line.
There will be m lines, where each line will have n characters, all in upper case, separated by a space.
There will be a single blank line.
There will be a single integer k, denoting the number of words that follow.
There will be k lines. Each line will contain a single word in all uppercase.
There will be k lines in your output file. Each line will have the word that you were search for followed by two integers i and j separated by one or more spaces. The numbers will be right justified and aligned. The number i gives the row and the number j the column of the first letter of the word that you were required to find. Rows and columns are numbered conventionally, i.e. the first row is 1 and the first column is 1. If you do not find a word in the grid then the values for i and j will be 0 and 0. Use the full power of the built-in functions associated with strings and lists.

 # design a function to find if two lists have identical components 
def eqallist(a,b):
  list=[]
  # by convention, set two strings as a and b ,assuming a will always be bigger than b
  if len(a)>=len(b):
  # append the same lengh fragment as b from a to a new list 
    for i in range(0,len(a)-len(b)+1):
      list.append(a[i:len(b)+i])
  # confirm if new list have element identical to b  
    if b in list:
  # return two output to indicate the search result and index of b in a 
      return(True,list.index(b))
    else:
      return(False,-1)
  # return false if no match of b in a  
  else:    
    return(False,-1)

  # this function transfer a horizontal list to a vertical list 
def verticallist(a):
  vlist=[]
  for i in range(len(a[0])):
    sub_list=[]
  # attach the first element of each row to become a new row and so the second, third..
    for j in a:
      sub_list.append(j[i])
    vlist.append(sub_list)
  return(vlist)


  # design a function to attach all the diagonal elements in the original list to a list 
def diagonallist(a):
  dlr_list=[]

  # read from left to right, up to down diagonally
  for i in range(len(a)-1,-1,-1):
    sub_list=[]  
    for j in range(len(a)+(-i)):
      sub_list.append(a[i+j][j])
    dlr_list.append(sub_list)

  for i in range(1,len(a)):
    sub_list=[]
    for j in range(len(a)-i):
      sub_list.append(a[j][i+j])
    dlr_list.append(sub_list)
      

  # read fomr right to left, up to down diagonally 
  drl_list=[]
  for i in range(len(a)):
    sublist=[]
    for j in range(i+1):
      sublist.append(a[j][i-j])
    drl_list.append(sublist)
  

  for i in range(1,len(a)):
    sublist=[]
    for j in range(len(a)-1,-1+i,-1):
      sublist.append(a[i+len(a)-1-j][j])
    drl_list.append(sublist)

  # return the two new lists that include all these diagonally read elements 

  return(dlr_list,drl_list)




def main():
  
  # open file hidden.txt and creat input file
  openfile=open("hidden.txt","r")
  outfile=open("found.txt","w")
  
  # read through the content line by line
  read=openfile.readline()

  # read the line untill the first single blank line
  while read.split():
  # record m,n from the grid
    grid=read.split()

    read=openfile.readline()

  # creat a new 2d list that include all the rows and columns of the grid
  matrix=[]
  
  read=openfile.readline()
  # transfer each line of the grid from string to list
  while read.split():
  # attach to create a 2d list
    matrix.append(read.split())

    read=openfile.readline()


  # transfer the rows to column and columns to rows in the grid to create a new one by using the pre-defined function 

  ver_matrix=verticallist(matrix)

  # create two new lists that include all these elements read diagonally in the grid 

  dialr_matrix,diarl_matrix=diagonallist(matrix)

  read=openfile.readline()
  
  # start to read through all these words in the input file anf find them in different created list 
  
  read=openfile.readline()
  while read.split():
  # strip the new line character and transfer the word string to a list 
    word=list(read.rstrip("\n"))

  # use the identical list function defined previously to see if the word can be found horizontally in the grid
    for i in matrix:
      a,b=eqallist(i,word)
  # return True if the word can be found in the grid row
      if a==True:
  # store the index of the word's first letter
        m,n=matrix.index(i)+1,b+1
        break

  # use the identical list function defined previously to see if the word can be found reverse horizontally in the grid
    if a==False:
      for i in matrix:
        a,b=eqallist(i,word[::-1])
        if a==True:
          m,n=matrix.index(i)+1,b+len(word)
          break

  # use the identical list function defined previously to see if the word can be found vertically in the grid
    if a==False:
      for i in ver_matrix:
        a,b=eqallist(i,word)
        if a==True:
          m,n=b+1,ver_matrix.index(i)+1
          break

  # use the identical list function defined previously to see if the word can be found reverse vertically in the grid
    if a==False:
      for i in ver_matrix:
        a,b=eqallist(i,word[::-1])
        if a==True:
          m,n=b+len(word),ver_matrix.index(i)+1
          break


  # use the identical list function defined previously to see if the word can be found diagonally from left to right, up to down in the grid 
    if a==False:
      for i in dialr_matrix:
        a,b=eqallist(i,word)
        if a==True:
          if dialr_matrix.index(i) <=13:
            m,n=13-(dialr_matrix.index(i)-b)+1,b+1
          else:
            m,n=b+1,dialr_matrix.index(i)-13+b+1
          break
  # use the identical list function defined previously to see if the word can be found reverse diagonally from left to right, up to down in the grid    
    if a ==False:
      for i in dialr_matrix:
        a,b=eqallist(i,word[::-1])
        if a==True:
          if dialr_matrix.index(i) <=13:
            m,n=13-(dialr_matrix.index(i)-b)+1+len(word)-1,b+1+len(word)-1
          else:
            m,n=b+1+len(word)-1,dialr_matrix.index(i)-13+b+1+len(word)-1
          break
      
  # use the identical list function defined previously to see if the word can be found diagonally from right to left, up to down in the grid
    if a ==False:
      for i in diarl_matrix:
        a,b=eqallist(i,word)
        if a==True:
          if diarl_matrix.index(i) <=13: 
            m,n=b+1,diarl_matrix.index(i)-b+1
          else:
            m,n=diarl_matrix.index(i)-13+b+1,14-b
          break
        
  # use the identical list function defined previously to see if the word can be found reverse diagonally from right to left, up to down in the grid          
              
    if a ==False:
      for i in diarl_matrix:
        a,b=eqallist(i,word[::-1])
        if a==True:
          if diarl_matrix.index(i) <=13: 
            m,n=b+1+len(word)-1,diarl_matrix.index(i)-b+1-len(word)+1
          else:
            m,n=diarl_matrix.index(i)-13+b+1+len(word)-1,14-b-len(word)+1
          break      
  # if not found, assign 0,0 to the index
    if a ==False:
      m,n=0,0

  # write the index for that word to the output file    
    outfile.write(read.rstrip("\n").ljust(12))
    outfile.write(str(m).rjust(2)+"  "+str(n).rjust(2)+"\n")
  
  # move to next word    
    read=openfile.readline()
    
  
  
  # close both files
  openfile.close()
  outfile.close()

  
main()


