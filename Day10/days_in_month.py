def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #month = month_days  
    if is_leap(year) == True and month == 2:
        return 29
    else:
       return  month_days[month -1]
    
    # check_days = is_leap(year)
    
    # if check_days  == True:
    #     if month == 2:
    #         return 29
    #     elif month in [1,3,5,7,8,10,12]:
    #         return 31
    #     elif month in [4,6,9,11]:
    #         return 30
    # else:
    #    if month == 2:
    #         return 29
    #    elif month in [1,3,5,7,8,10,12]:
    #         return 31
    #    elif month in [4,6,9,11]:
    #         return 30 
        

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




