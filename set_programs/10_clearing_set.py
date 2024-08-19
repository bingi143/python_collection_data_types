'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program clearing set

'''


def clearing_set(set_):
    '''
        Description:
            The function is to clearing a set
        Parameters:two sets 
            set_1: the first set
            set_2:the second set
        Return :
           not returnign anymthing in  this function

    '''
   
    del set_
    print("cleared all elements in set")


def main():
    set_={'kk',"love","pp",20}
    clearing_set(set_)


if __name__=="__main__":
    main()