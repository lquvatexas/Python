#  Description: this program you will compute the date of Easter Sunday. Easter Sunday is the first Sunday after the first full moon of Spring.
def main():
    # get user input for year. Let y be the year
    y=int(input("Enter year: "))
    # Divide y by 19 and call the remainder a. Ignore the quotient.
    a=y%19
    # Divide y by 100 to get a quotient b and a remainder c.
    b=y//100
    c=y%100
    # Divide b by 4 to get a quotient d and a remainder e.
    d=b//4
    e=b%4
    # Divide 8 * b + 13 by 25 to get a quotient g. Ignore the remainder.
    g=(8*b+13)//25
    # Divide 19 * a + b - d - g + 15 by 30 to get a remainder h. Ignore the quotient.
    h=(19 * a + b - d - g + 15) %30
    # Divide c by 4 to get a quotient j and a remainder k.
    j=c//4
    k=c%4
    # Divide a + 11 * h by 319 to get a quotient m. Ignore the remainder.
    m= (a + 11 * h)//319
    # Divide 2 * e + 2 * j - k - h + m + 32 by 7 to get a remainder r. Ignore the quotient.
    r=(2 * e + 2 * j - k - h + m + 32) % 7
    # Divide h - m + r + 90 by 25 to get a quotient n. Ignore the remainder.
    n=(h - m + r + 90)//25
    # Divide h - m + r + n + 19 by 32 to get a remainder p. Ignore the quotient.
    p=(h - m + r + n + 19)%32

    #print out the results
    if n==1:
        print("In", y, "Easter Sunday is on", p, "January")
    elif n==2:
        print("In", y, "Easter Sunday is on", p, "February")
    elif n==3:
        print("In", y, "Easter Sunday is on", p, "March")
    elif n==4:
        print("In", y, "Easter Sunday is on", p, "April")
    elif n==5:
        print("In", y, "Easter Sunday is on", p, "May")
    elif n==6:
        print("In", y, "Easter Sunday is on", p, "June")
    elif n==7:
        print("In", y, "Easter Sunday is on", p, "July")
    elif n==8:
        print("In", y, "Easter Sunday is on", p, "August")
    elif n==9:
        print("In", y, "Easter Sunday is on", p, "September")
    elif n==10:
        print("In", y, "Easter Sunday is on", p, "October")
    elif n==11:
        print("In", y, "Easter Sunday is on", p, "November")
    elif n==12:
        print("In", y, "Easter Sunday is on", p, "December")
  main()
    

main()
