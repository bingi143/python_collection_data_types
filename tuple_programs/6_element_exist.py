'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program check element exist in tuple

'''


def element_exist(tuple_,element):
    '''
          Description: 
                this function we will get given element exist or nor

          Parameters:
              tuple: the tuple of elements
              element: given element
              
          Return :
              not returning any thing
    '''
    if element in tuple_:
        print("element exist in tuple")
    else:
        print("element not exist in tuple")


def main():
    tuple_=(2,5,8,6,880)
    element=int(input("enter element:"))
    element_exist(tuple_,element)


if __name__=="__main__":
    main()