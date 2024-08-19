'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is removing items in set if present

'''


def removing_item_set(set_,item):
     '''
          Description: 
                this function is removing item if it present
          Parameters: 
             set_: set of items
             item: item to remove
          Return : 
                not returnig any thing
      '''
     if item in set_:
         set_.remove(item)
         print("item is removed",set_)
     else:
         print("item not present in set")



def main():
    set_={1,2,3,4,5,6,7}
    item=6
    removing_item_set(set_,item)


if __name__=="__main__":
    main()