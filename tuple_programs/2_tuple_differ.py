'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program creating tuple with different data types

'''


def creating_tuple_different_data_types():
    '''
          Description: 
                this function we will creating tuple with different typed data

          Parameters:
              no Parameters
              
          Return :
              returnig the tuple
    '''
    tuple_=(1,3,"hi","venky",3.6,True)
    return tuple_


def main():
    print("tuple with different data types",creating_tuple_different_data_types())


if __name__=="__main__":
    main()