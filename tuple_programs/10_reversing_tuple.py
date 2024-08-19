'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program reversing tuple 

'''


def reversing_tuple(tuple_):
    '''
          Description: 
                this function is reversing tuple

          Parameters:
              tuple: the tuple of elements
              
          Return :
              returning the tuple after reversing
    '''
    reverse_tuple=tuple_[::-1]
    return reverse_tuple
    return tuple_[2:4]


def main():
    tuple_=(1,2,3,4,5,6)
    print(f"After reversing:{reversing_tuple(tuple_)}")

    
if __name__=="__main__":
    main()