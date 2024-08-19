'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program longer list more than n

'''


def Longer_lists_(list_,n):
    '''
          Description: 
                this function longer list more than n
          Parameters:
              list1: list - The list of numbers
              n : number 
          Return :
              it returns the after longer than n elements

    '''
    list=[]
    for i in list_:
        if len(i)>n:
            list.append(i)
    return list


def main():
    list=['hello','chello','venkatesh',"Bridge","hsr","bb"]
    n=4
    print(f"longer than {n} list are {Longer_lists_(list,n)}")


if __name__=="__main__":
    main()