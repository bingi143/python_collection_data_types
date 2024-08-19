'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program symentric difference of two sets

'''


def Symetric_difference(set_1,set_2):
    '''
       Description: 
           The function is symentric difference of in two set  means not common ellements in two sets
       Parameters:two sets 
           set_1: the first set
           set_2:the second set
       Return :
       not returnign anymthing in  this function

    '''
    set_result=set_1.symmetric_difference(set_2)
    print(set_result)


def main():
    set_1={1,'a','j','k','m'}
    set_2={1,"venky","monkey",'m',"pinkey"}
    Symetric_difference(set_1,set_2)

    
if __name__=="__main__":
    main()