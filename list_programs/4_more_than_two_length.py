'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program more than two length string

'''


def identify_string_in_list(list_):
    '''
          Description: 
              The function is string length is more than two and last one, 
              first elements having same string count  items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              multiplies: int - it returns the s count of string is more 
              than 2 length and last and first element is same

    '''
    count=0
    for i in list_:
        if len(i)>=2:
            if i[0]==i[-1]:
                count+=1
    return count


def main():
    list_=["amma","daddy",'aba','abc','1211']
    print("the count of String having more than 2 length and last,first elements same is:",identify_string_in_list(list_))


if __name__=="__main__":
    main()