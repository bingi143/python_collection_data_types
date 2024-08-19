'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program change string based on first charecter

'''


def changin_string_first_char(string_):
    '''
          Description: 
                this function is changing based on first charecter palce excluding remaing count in string

          Parameters:
              string: string
              
          Return :
              returning the string after changes
    '''
   
    char_first=string_[0]
    result_string=char_first+string_[1:].replace(char_first,'$')
    return result_string


def main():
    string_=input("Enter String:")
    print("after changing",changin_string_first_char(string_))

    
if __name__=="__main__":
    main()