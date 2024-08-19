'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program permitation

'''


import itertools

def permitation_lists(list_):
    '''
          Description: 
                this function get all posible ways of arranging permutation
          Parameters:
              list: list - The list of numbers
          Return :
              After arranging permutation return those lists
    '''
    return list(itertools.permutations(list_))


def main():
    list_=[3,5,9]
    print(permitation_lists(list_))

    
if __name__=="__main__":
    main()