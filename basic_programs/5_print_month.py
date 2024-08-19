'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is print entire month

'''


import calendar

def print_month(year,month):
    '''
          Description: 
                this function is printing entire month
          Parameters: 
                year: enter the year
                month: month
          Return : 
                this function not returing  any thing
        '''
    print(calendar.month(year,month))



def main():
    year = int(input("Enter year last two digits:"))
    month = int(input("Enter month: "))
    print_month(year,month)


if __name__=="__main__":
    main()