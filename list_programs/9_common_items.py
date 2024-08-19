'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program common items

'''


def common_item(list_1,list_2):
    '''
          Description: 
                this function if in case one item common in that elements return true or else false
          Parameters:
              list1: list - The list of numbers
              list_2:list -the list of members
          Return :
              true if common element in that lists

    '''
    b=False
    for i in list_1:
        if i in list_2:
            b=True
            return b
        
    return b


def main():
    list_1=[3,4,"hi","byr",90,"venky"]
    list_2=["teju","devil","majnu","laila",'venky']
    if common_item(list_1,list_2):
        print("common elements are in two lists")
    else:
        print("no common elements")


if __name__=="__main__":
    main()