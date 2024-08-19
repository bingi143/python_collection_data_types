'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program convertion tuple to list

'''


def conversion_list_to_tuple(tuple_):
    '''
          Description: 
                this function we are converting tuple to list

          Parameters:
              tuple: the tuple of elements
              
          Return :
              returning list 
    '''
    list_=list(tuple_)
    return list_


def main():
    tuple_=(2,5,8,6,880)
    print(f"After conversion list is: {conversion_list_to_tuple(tuple_)}")


if __name__=="__main__":
    main()