'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is printing items in list

'''


def print_items(list_):
    '''
          Description: 
                this function is printing taken values
          Parameters: 
                list_: list of elements
          Return : 
                this function not returing  any thing
        '''
    _tuple=tuple(list_)
    print(list_)
    print(_tuple)


def main():
    in_put=input("Enter sequence of numbers using :")
    list_=in_put.split(",")
    print_items(list_)


if __name__=="__main__":
    main()