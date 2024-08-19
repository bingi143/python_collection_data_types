'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program sorted order based on second value

'''


def Sorted_order_based_on_last_element(list_):
    '''
          Description: 
              this function sorted order based on second value in list  
          Parameters:
              list1: list - The list of numbers
          Return :
              returning list

    '''
    length=len(list_)
    for i in range(length-1):
        for j in range(length-1-i):
            if list_[j][1]>list_[j+1][1]:
                list_[j],list_[j+1]=list_[j+1],list_[j]
    return list_


def main():
    list=[(1,4),(4,6),(7,9),(4,9),(1,2)]
    print("order is:",Sorted_order_based_on_last_element(list))


if __name__=="__main__":
    main()

