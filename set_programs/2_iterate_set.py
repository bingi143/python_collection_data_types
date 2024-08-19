'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is iterate set

'''


def iterate_set(set_):
    '''
          Description: 
                this function is iterate set
          Parameters: 
             set_: set of items
          Return : 
                not returnig any thing
        '''
        
    for i in set_:
        print(i)


def main():
    set_={1,3,"hello","bye",'chello',90}
    iterate_set(set_)


if __name__=="__main__":
    main()