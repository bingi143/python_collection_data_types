'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is create a set

'''


def create_set():
    '''
          Description: 
                this function is creating set
          Parameters: 
             no parameters
          Return : 
                not returnig any thing
        '''
    set_=set()
    set_.add(1)
    set_.add(3)
    set_.add(9)
    print(set_)


def main():
    create_set()


if __name__=="__main__":
    main()