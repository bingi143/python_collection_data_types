'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program assigning tuple values  to several variables 

'''


def unpack_tuple_several_var(tuple_):
    '''
          Description: 
                this function we will assigning tuple values  to several variables 

          Parameters:
              tuple: the set of elements
              
          Return :
              not returning any thing
    '''
    a,b,c=tuple_
    print("a value:",a)
    print("b value:",b)
    print("c value:",c)


def main():
    tuple_=(2,5,8)
    unpack_tuple_several_var(tuple_)


if __name__=="__main__":
    main()