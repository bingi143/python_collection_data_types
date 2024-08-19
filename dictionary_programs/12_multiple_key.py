'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is multiple keys exist or not

'''


def keys_exist_method(list,dict_):
    '''
          Description: 
                this function is mutliple keys in dictionary exist or not
          Parameters: 
              list: list of elements
              dict_: key paired values
          Return : 
                not returnig any thing
        '''
    b=True
    for key in list:
        if key not in dict_:
            b=False
            return
    return b
   


def main():
    dict_={'a':1,'b':2,'c':3}
    list=['a','c']
    if keys_exist_method(list,dict_):
        print("all keys are present")
    else:
        print("not present")


if __name__=="__main__":
    main()