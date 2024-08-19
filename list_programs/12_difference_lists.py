'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program difference in two lists

'''


def Difference_two_lists(list_1,list_2):
    '''
          Description: 
                this function get different elements 
          Parameters:
              list_1: list - The list of combination elements
              list_2: list -the list of combination elements
          Return :
              After identify the difference list is returned
    '''
    list_result=[]
    for i in list_1:
        if i not in list_2:
            list_result.append(i)
    return list_result


def main():
    list_1=[3,5,6,"hi","venky",43]
    list_2=["chelo",3,5,90]
    print(f"difference {Difference_two_lists(list_1,list_2)}")


if __name__=="__main__":
    main()