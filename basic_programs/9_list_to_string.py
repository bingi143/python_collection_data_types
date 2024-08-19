'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is list of items into string

'''


def concronate(list_):
    '''
          Description: 
                this function is adding list items into string
          Parameters: 
                 list_: list of elements
          Return : 
                this function returnting string
        '''

    string_result=str()
    for i in list_:
        string_result+=(str(i))
    return string_result


def main():
    list=[1,2,34,5,'hello']
    print(concronate(list))


if __name__=="__main__":
    main()