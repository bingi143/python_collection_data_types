'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program upper lower case conversion

'''


def upper_lower_convertion(string_):
    '''
          Description: 
                this function is converting lower and upper case

          Parameters:
              string: string
              
          Return :
              returning the strings after conversion
    '''
    string_lower=string_.lower()
    string_upper=string_.upper()
    return string_lower,string_upper


def main():
    string_=input("Enter string:")
    string_lower,string_upper=upper_lower_convertion(string_)
    print("lower convertion",string_lower)
    print('upper convertion',string_upper)


if __name__=="__main__":
    main()