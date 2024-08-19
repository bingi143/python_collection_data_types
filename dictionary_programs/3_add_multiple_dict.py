'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is adding value in item

'''


def adding_multiple_dictionary(dict_1,dict_2,dict_3):
    '''
          Description: 
                this function is adding multiple dictioanries in dictionary
          Parameters: 
               dict_1: paired values
               dict_2: paired values
               dict_1: paired values
          Return : 
                not returnig any thing
        '''
    
    dict_result= {**dict_1,**dict_2,**dict_3}
    print(dict_result)


def main():
    dict_1={1:10,2:20}
    dict_2={3:30,4:40}
    dict_3={5:50,6:60}
    adding_multiple_dictionary(dict_1,dict_2,dict_3)


if __name__=="__main__":
    main()

