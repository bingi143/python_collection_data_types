'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program first char is lower 

'''


def First_char_lower_case(string_,n):
    '''
          Description: 
                this function is geeting lower fiest n charecters

          Parameters:
              string: set of charecter string
              n : number of charecters want to lower conversion
              
          Return :
              returning the reverse string
    '''
    string_result=string_[:n].lower()
    string_result+=string_[n:]
    return string_result


def main():
    string_=input("enter string giving pace to enter: ")
    n=int(input("enter number of string to convert to lower case:"))
    print(First_char_lower_case(string_,n))


if __name__=="__main__":
    main()