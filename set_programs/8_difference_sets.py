'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program difference of two sets

'''


def set_deference(set_1,set_2):
    ''' 
        Description: 
             The function is difference of in two set  means set_1 which are not present in set_2 
        Parameters:two sets 
             set_1: the first set
             set_2:the second set
        Return :
             not returnign anymthing in  this function

    '''
    set_result=set_1.difference(set_2)
    print(set_result)


def main():
    set_1={1,2,'a','dd','sss'}
    set_2={'ss','pp',2,'a'}
    set_deference(set_1,set_2)


if __name__=="__main__":
    main()