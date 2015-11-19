Here are two sample files - dickens.txt and hardy.txt taken from the two novels. Your output for these two sample files should be of the following form:

Enter name of first book: dickens.txt
Enter name of second book: hardy.txt

Enter last name of first author: Dickens
Enter last name of second author: Hardy

Dickens
Total distinct words = 58
Total words (including duplicates) = 119
Ratio (% of total distinct words to total words) = 48.7394957983

Hardy
Total distinct words = 93
Total words (including duplicates) = 123
Ratio(% of total distinct words to total words) = 75.6097560976

Dickens used 50 words that Hardy did not use.
Relative frequency of words used by Dickens not in common with Hardy = 63.8655462185 

Hardy used 85 words that Dickens did not use.
Relative frequency of words used by Hardy not in common with Dickens = 77.2357723577 
# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():

  wordfile=open("words.txt",'r')
  for line in wordfile:
    line=line.strip()
    linestr=str(line)
    word_dict[linestr]=1
  
  wordfile.close()
  return word_dict


# Removes punctuation marks from a string
def parseString (st):
  s = ''
  for ch in st:
    if (ch >= 'a' and ch <= 'z'):
      s += ch
    elif (ch == '\'') and (st[-2] != ch) and (st[-1] != ch):
      s += ch
    else:
      s += ' '
  return s


# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  afile=open(file,'r')
  nword_dict={}
  for line in afile:
    line=line.strip()
    line=line.lower()
    line=parseString(line)
    line=line.split()

    for voc in line:
      s=voc
      lowvoc=s.lower()
      if lowvoc in word_dict:
        if lowvoc in nword_dict:
          nword_dict[lowvoc]+=1
        else:
          nword_dict[lowvoc]=1
  afile.close()
  return nword_dict
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
  
  
  distin1=len(freq1)
  #get the total
  total1=0
  for key in freq1:
    total1+=freq1[key]

  print(author1)
  print("Total distinct words = ", distin1)
  print("Total words (including duplicates) = ", total1)
  print("Ratio (percent of total distinct words to total words) = ", distin1/total1*100)
  print()

  
  distin2=len(freq2)
  #get the total
  total2=0
  for key in freq2:
    total2+=freq2[key]

  print(author2)
  print("Total distinct words = ", distin2)
  print("Total words (including duplicates) = ", total2)
  print("Ratio (percent of total distinct words to total words) = ", distin2/total2*100)
  print()

  #find set difference
  set1=[]
  set2=[]
  for key in freq1:
    set1.append(key)
  for key in freq2:
    set2.append(key)
  nset1=set(set1)
  nset2=set(set2)
  diff1=nset1.difference(nset2)
  diff2=nset2.difference(nset1)
  #get relative total frequencies
  relatotal1=0
  for i in diff1:
    relatotal1+=freq1[i]
  relatotal2=0
  for j in diff2:
    relatotal2+=freq2[j]


  print("Dickens used", len(diff1), "words that Hardy did not use.")
  print("Relative frequency of words used by Dickens not in common with Hardy = ", relatotal1/total1*100)
  print()

  print("Dickens used", len(diff2), "words that Hardy did not use.")
  print("Relative frequency of words used by Dickens not in common with Hardy = ", relatotal2/total2*100)
  print()




def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)


main()
