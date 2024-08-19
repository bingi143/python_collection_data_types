'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program largest string in list

'''


def longest_length(list_string):
    '''
          Description: 
                this function is finding the largest length of string in list

          Parameters:
              string: string
              
          Return :
              returning the string after finding large one
    '''
    max_length=0
    string_result='hi'
    for i in list_string:
        if len(i)>max_length:
            max_length=len(i)
            string_result=i
    return string_result



def main():
    list_string=['venky',"monkey",'donkey','ponkey','chunkey']
    print("longest String is",longest_length(list_string))


if __name__=="__main__":
    main()