'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is displaying array items in reverse

'''


import array

def count_occurrences(array, element):

     '''
          Description: 
                this function is occurence of specific item
          Parameters: 
                array: array of items
                element: specified item
          Return : 
                returing the count occurence of item
        '''
     count = array.count(element)
     return count
    
   
def main():
    array_=[1,2,3,4,5,3,3,8]
    item=int(input("enter:"))
    print(f"count is:{count_occurrences(array_,item)}")


if __name__=="__main__":
    main()