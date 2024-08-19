'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program maximum minimum in set

'''


def maximum_minimum_set(set_):
    '''
          Description: 
                this function is maximum minimum in set
          Parameters: 
             set_: set of items
          Return : 
                not returnig any thing
      '''
    max_value=max(set_)
    min_value=min(set_)
    print(max_value)
    print(min_value)


def main():
    set_={2,4,40,454,65.6,780}
    maximum_minimum_set(set_)


if __name__=="__main__":
    main()