'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program reverse of string

'''


def Reverse_string(string_):
    '''
          Description: 
                this function is get reverse of string

          Parameters:
              string: set of charecter string
              
          Return :
              returning the reverse string
    '''
    string_result=string_[::-1]
    return string_result


def main():
    string=input("Enter String:")
    print(f"reverse of string is:{Reverse_string(string)}")


if __name__=="__main__":
    main()