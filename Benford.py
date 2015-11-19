In 1881, Simon Newcomb had noticed that in tables of logarithms, the first pages were much more worn and smudged than later pages. In 1938, Frank Benford published a paper showing the distribution of the leading digit in many disparate sources of data. In all these sets of data, the number 1 was the leading digit about 30% of the time.

Benford's law has been found to apply to population numbers, death rates, lengths of rivers, mathematical distributions given by some power law, and physical constants like atomic weights and specific heats. This law is now used to detect fraud in lists of socio-economic data submitted in support of public planning decisions and as an indicator of accounting and expenses fraud.

In this programming assignment you will verify Benford's law for the US Census data of 2009. The file Census_2009 gives the population distribution in the US. Each line of data has the name of the state, the town or village, and its population. The linked Python code reads the file and stores all the population data into a list.

You will create a dictionary that create a frequency distribution of the the first digit of the population numbers. You will print out the actual frequency and the relative frequency of each digit. The sample output will look like:

Digit	Count	%
1	18	30.0
2	8	13.3
3	8	13.3
4	6	10.0
5	10	16.7
6	5	8.3
7	2	3.3
8	1	1.7
9	2	3.3

def main():
  # create an empty list pop_num[]
  pop_num = []
  # read file in and store the last element(number) into this list
  inFile = open('Census_2009.txt','r')
  total_num = 0
  for line in inFile:
    if (total_num == 0):
      total_num += 1
      continue
    else:
      total_num += 1
      line = line.rstrip('\n')
      word_list = line.split()
      pop_num.append(word_list[-1])
  inFile.close()
  # print first line 
  print('Digit' + '\t' + 'Count' + '\t' + '%')
  # create a list to contain all the first digits of the data
  firstDigit=[]
  length = len(pop_num)
  for i in range (length):
    num = pop_num[i]
    digitlist = list(num)
    leadingdigit = digitlist[0]
    firstDigit.append(leadingdigit)
  # create an empty dictionary for population frequency distribution called pop_dic
  pop_dic = {}
  # make the frequency distribution dictionary
  for j in range (length):
    first_num = firstDigit[j]
    if first_num in pop_dic:
      pop_dic[first_num] += 1
    else:
      pop_dic[first_num] = 1
  for key in range(1,10):
    key=str(key)
    percent = (pop_dic[key]/len(firstDigit))*100
    print(key,'     ','%-4i'%pop_dic[key],'  ','%.1f'%percent)
main()

