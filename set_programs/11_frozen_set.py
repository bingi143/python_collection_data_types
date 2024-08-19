'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program frozen set

'''


def demonstrate_frozenset_operations():
    '''
          Description: 
                this function is frozen set
          Parameters: 
             no parameters
          Return : 
                not returnig any thing
      '''
    # Creating a frozenset
    frozenset_a = frozenset([1, 2, 3, 4, 5])
    frozenset_b = frozenset([4, 5, 6, 7, 8])

    print("Frozenset A:", frozenset_a)
    print("Frozenset B:", frozenset_b)

    # Union of two frozensets
    union_set = frozenset_a.union(frozenset_b)
    print("Union of A and B:", union_set)

    # Intersection of two frozensets
    intersection_set = frozenset_a.intersection(frozenset_b)
    print("Intersection of A and B:", intersection_set)

    # Difference between two frozensets
    difference_set = frozenset_a.difference(frozenset_b)
    print("Difference between A and B (A - B):", difference_set)

    # Symmetric difference between two frozensets
    symmetric_difference_set = frozenset_a.symmetric_difference(frozenset_b)
    print("Symmetric Difference between A and B:", symmetric_difference_set)

    # Checking if an element is in the frozenset
    element = 3
    if element in frozenset_a:
        print(f"Element {element} is in Frozenset A")
    else:
        print(f"Element {element} is not in Frozenset A")



def main():
    demonstrate_frozenset_operations()


if __name__=="__main__":
    main()