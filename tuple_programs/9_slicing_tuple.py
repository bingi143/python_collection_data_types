'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program slicing

'''


def Slicing_tuple_(tuple_):
    '''
          Description: 
                this function is slicing

          Parameters:
              tuple: the tuple of elements
              
          Return :
              returning the tuple after slicng
    '''
    
    return tuple_[2:4]


def main():
#    tuple_=(int(item_) for item_ in input("Enter Elements:").split(","))
#    print(f"After slicing tuple is: {Slicing_tuple_(tuple_)}")
    tup=(1,2,3,4,5,6)
    print(tup[1:4])


if __name__=="__main__":
    main()