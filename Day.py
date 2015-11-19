# In this program you will prompt the user to enter the day, month, and year. Your program will print out the day of the week for that date
def main():
   # prompt the user to enter the number of year
   year = eval(input('Enter year:'))
   # check if the number of year is between 1900 and 2100
   while (year < 1900) or (year > 2100):
      year = eval(input('Enter year:'))
   # prompt the user to enter the month
   month = eval(input('Enter month:'))
   # check if the number of the month is between 1 and 12
   while (month < 1) or (month > 12):
      month = eval(input('Enter month:'))
   # prompt the user to enter the day of the month
   day = eval(input('Enter day:'))
   if month == 1:
     while (day < 1) or (day > 31):
       day = eval(input('Enter day:'))
   # check if the month is February 
   elif month == 2:
   # check if the year is leap year
      if ( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   # if the year is leap year February has 29 days
        while (day < 1) or (day > 29):
          day = eval(input('Enter day:'))
   # if the year is not leap year February has 28 days
      else:
        while (day < 1) or (day > 28):
          day = eval(input('Enter day:'))
   elif month == 3:
        while (day < 1) or (day > 31):
          day = eval(input('Enter day:'))
   elif month == 4:
        while (day < 1) or (day > 30):
          day = eval(input('Enter day:'))
   elif month == 5:
        while (day < 1) or (day > 31):
          day = eval(input('Enter day:'))
   elif month == 6:
        while (day < 1) or (day > 30):
          day = eval(input('Enter day:'))
   elif month == 7:
        while (day < 1) or (day > 31):
          day = eval(input('Enter day:'))
   elif month == 8:
        while (day < 1) or (day > 30):
          day = eval(input('Enter day:'))
   elif month == 9:
        while (day < 1) or (day > 31):
          day = eval(input('Enter day:'))
   elif month == 10:
        while (day < 1) or (day > 30):
          day = eval(input('Enter day:'))
   elif month == 11:
        while (day < 1) or (day > 31):
          day = eval(input('Enter day:'))
   elif month == 12:
        while (day < 1) or (day > 30):
          day = eval(input('Enter day:'))
   # if the number of month is less than or equal to 2 we have to add 10 to the number of the month to adjust it to the calendar 
   if month <= 2:
       month = month + 10
   # if the number of month is less than or equal to 10 we have to subtract 2 of the number of the month to adjust it to the calendar 
   else:
       month = month - 2
   a = month
   b = day
   # if the number of month is more or equal to 11 we have to subtract 1 of the number of the year to adjust it to the calendar
   if a >= 11:
        year = year - 1
        c = year % 100
   else:
        c = year % 100
   # compute the values of d,w,x,y,z,r
   d = year // 100 
   w = (13 * a - 1) // 5
   x = c // 4
   y = d // 4
   z = w + x + y + b + c - 2 * d
   r = z % 7
   r = (r + 7) % 7
   # print the result depending on r
   if r == 0:
       print('The day is Sunday')
   elif r == 1:
       print('The day is Monday')
   elif r == 2:
       print('The day is Tuesday')
   elif r == 3:
       print('The day is Wednesday')
   elif r == 4:
       print('The day is Thursday')
   elif r == 5:
       print('The day is Friday')
   elif r == 6:
       print('The day is Saturday')
main()
