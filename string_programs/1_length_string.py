'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program length of string

'''


def Length_string(string_):
    '''
          Description: 
                this function is getting length of string

          Parameters:
              string: string
              
          Return :
              returning the length of string
    '''
    return len(string_)


def main():
    string_=input("Enter String:")
    print(f"length of string is:{Length_string(string_)}")

    
if __name__=="__main__":
    main()

