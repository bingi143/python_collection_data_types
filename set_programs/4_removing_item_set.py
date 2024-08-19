'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is removing items in set

'''


def removing_items_set(set_):
    '''
          Description: 
                this function is removing items in set
          Parameters: 
             set_: set of items
          Return : 
                not returnig any thing
        '''
    set_.remove(2)
    set_.remove("bam")
    set_.remove(78.9)
    print("after removing remaing set are",set_)


def main():
    set_={2,"mam","bam","thum","gum",78,78.9,90}
    removing_items_set(set_)


if __name__=="__main__":
    main()
