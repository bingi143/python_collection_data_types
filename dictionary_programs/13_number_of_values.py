'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is multiple keys exist or not

'''


def items_count(dict_):
    '''
          Description: 
                this function is counting number of items in dictionary
          Parameters: 
             dict_: key paired values
          Return : 
                not returnig any thing
        '''
    c=0
    for i,j in dict_.items():
        if isinstance(j,list):
            c=c+1
        
    print(c)


def main():
    dict_= {1:[1,2,3],2:'aa',3:[1,12,34],4:'sds',5:[3,45,76,767]}
    items_count(dict_)


if __name__=="__main__":
    main()