'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is adding items in set

'''


def adding_items_set(set_):
    '''
          Description: 
                this function is adding items in set
          Parameters: 
             set_: set of items
          Return : 
                not returnig any thing
        '''
    set_.add(232)
    set_.add(434)
    set_.add("hi")
    set_.add('Bye')
    print(set_)


def main():
    set_={12,23,"hi","venky","goal",'hard'}
    adding_items_set(set_)


if __name__=="__main__":
    main()
