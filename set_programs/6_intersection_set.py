'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is intersection of two items

'''


def intercection(set_1,set_2):
    '''
          Description: 
                this function is intersection of two sets
          Parameters: 
             set_1: set of items
             set_2: set of items
          Return : 
                not returnig any thing
      '''
    set_result=set_1.intersection(set_2)
    print(set_result)


def main():
    set_1={1,2,3,4,6}
    set_2={4,6,8,9,10}
    intercection(set_1,set_2)


if __name__=="__main__":
    main()