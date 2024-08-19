'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program removing duplicate values

'''


def remove_duplicates(list_):
    '''
          Description: 
                this function we will get removing duplicate lists
          Parameters:
              list_: list - The list of combination elements
              
          Return :
              returnig the after removing duplicate elements in list
    '''
    
    set_=set()

    list_result=[]
    for i in list_:
        
        k=tuple(i) 
        
        if k not in set_:
            set_.add(k)
            list_result.append(k)
    return list_result


def main():
    list_=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(f"after removing{remove_duplicates(list_)}")


if __name__=="__main__":
    main()