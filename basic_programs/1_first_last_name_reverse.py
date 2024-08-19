'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is last and first name reversing

'''


def reverse_method(first_name,last_name):
    '''
          Description: 
                this function is reversing last and first name reverse
          Parameters: 
                first_name: first name
                last_name: last name
          Return : 
                this function not returing  any thing
        '''
    print(first_name[::-1],end=(' '))
    print(last_name[::-1])


def main():
    first_name = str(input("Enter Your first name:"))
    last_name = str(input("Enter Last name:"))
    reverse_method(first_name,last_name)


if __name__=="__main__":
    main()

