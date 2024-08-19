'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program multiple of all items

'''


def multiplies_all_list(list_):
    '''
          Description: 
              The function to multipies all the items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              multiplies: int - The multiplication of all the items in the list 
    '''
    result=1
    for i in list_:
        result=result*i
    return result


def main():
    list_=[2,4,5,6,9]
    print("multiplicatoin of all items in list is:",multiplies_all_list(list_))


if __name__=="__main__":
    main()


