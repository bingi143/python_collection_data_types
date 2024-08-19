'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program occurence of sub string

'''


def occurance_sub_string(string_,sub_string):
    '''
          Description: 
                this function is occurence of substrigs in count

          Parameters:
              string: set of charecter string
              
          Return :
              returning the count of substring occurence
    '''
    count=string_.count(sub_string)
    return count
    

def main():
    string_=input("Enter String:")
    sub_string=input("Enter substring:")
    print("count of substring:",occurance_sub_string(string_,sub_string))


if __name__=="__main__":
    main()