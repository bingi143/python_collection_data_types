'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program split string accordig to special char

'''


def specified_char_string(string_):
    '''
          Description: 
                this function is split the strig accordign special char

          Parameters:
              string: string of words
              
          Return :
              returning the after cut the part of string
    '''
    result=string_.rsplit('-',1)[0]
    return result


def main():
    string_='https://www.w3resource.com/python-exercises'
    print("after removing:",specified_char_string(string_))

    
if __name__=="__main__":
    main()