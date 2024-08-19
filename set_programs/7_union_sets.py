'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is union of two sets

'''


def Union_sets(set_1,set_2):
    '''
         Description: 
            The function is intersection of in two set  means common elements
        Parameters: two sets 
             set_1: the first set
             set_2:the second set
        Return :
             not returnign anymthing in  this function
    '''
    set_result=set_1.union(set_2)
    print(set_result)


def main():
    set_1={2,4,5,6,7,9}
    set_2={'a','b','c','d'}
    Union_sets(set_1,set_2)

    
if __name__=="__main__":
    main()