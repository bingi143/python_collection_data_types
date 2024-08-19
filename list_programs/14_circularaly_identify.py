'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program circular identify

'''


def circularly_identify(list_1,list_2):
    '''
          Description: 
                this function we will get both are circularly identified return True
          Parameters:
              list_1: list - The list of combination elements
              list_2: list -the list of combination elements
          Return :
              it returned True if it circular
    '''
    b=False
    if len(list_1)!=len(list_2):
        return False
    for item in list_1:
        if list_1[item:]+list_1[:item]==list_2:
            return True
    return False


def main():
    list_1=[1,2,3,4]
    list_2=[3,4,1,2]
    if circularly_identify(list_1,list_2):
        print("both lists are circularly identified")
    else:
        print("not circularly identified lists")


if __name__=="__main__":
    main()