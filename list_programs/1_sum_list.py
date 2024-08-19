'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program sum of all items

'''


def sum_of_list(list_):
    '''
          Description: 
              The function to sum all the items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              sum: int - The sum of all the items in the list 
        '''
    sum=0
    for i in list_:
        sum+=i
    return sum


def main():
    list_=[1,2,3,4,45,64]
    print(sum_of_list(list_))


if __name__=="__main__":
    main()