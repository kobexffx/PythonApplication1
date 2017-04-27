def isleapyear(year,mon,day):
    if ((year%4==0 and year%100!=0) or year%400==0):
        return True
    else:
        return False
    


print isleapyear(1996,1,1)

isleapyear(2000,12,24)

        
