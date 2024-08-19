'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is printing day between dates

'''


from datetime import date

def days_between(date_1,date_2):
    '''
          Description: 
                this function is printing days between two dates
          Parameters: 
                date_1: date year month date
                date_2:  date year month date
          Return : 
                this function returnting days
        '''
    d1=date(*date_1)
    d2=date(*date_2)
    date_result=d2-d1
    return date_result.days


def main():
    date_1=2014,7,2
    date_2=2014,7,21
    between_days=days_between(date_1,date_2)
    print(between_days)


if __name__=="__main__":
    main()