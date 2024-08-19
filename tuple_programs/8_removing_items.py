'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program removing items

'''


def removing_item_tuple(tuple_,item_):
    '''
          Description: 
                this function is removing item in tuple

          Parameters:
              tuple: the tuple of elements
              
          Return :
              returning the tuple after removing item
    '''
    list_=list(tuple_)
    list_.remove(item_)
    tuple_result=set(list_)
    return tuple_result

    
def main():
    tuple_=(int(item) for item in input("Enter:").split(","))
    item_=int(input("Enter element to remove:"))

    print(f"After removing tuple is: {removing_item_tuple(tuple_,item_)}")


if __name__=="__main__":
    main()