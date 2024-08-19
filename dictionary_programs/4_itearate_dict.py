'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is printing pair values

'''

def print_method(dict_):
    '''
          Description: 
                this function is printing key and pair value
          Parameters: 
              dict_: dictionary
          Return : 
                not returnig any thing
        '''
    for i,j in dict_.items():
        print(i,j)


def main():
    dict_={1:2,2:3,3:4,4:5,5:6}
    print_method(dict_)


if __name__=="__main__":
    main()