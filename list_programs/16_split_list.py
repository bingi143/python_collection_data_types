'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program split list based on first charecter

'''


def split_list_based_first_char(list_):
     '''
          Description: 
                this function we get supporate lists in based on first charecter
          Parameters:
              list_: list - The list of combination elements
              
          Return :
              it returns the splitted lists according to first charecter
    '''
     
     split=dict()
     for word in list_:
         first_char=word[0]
         if first_char not in split:
             split[first_char]=[]
         split[first_char].append(word)
     return split


def main():
    list_=["apple", "banana", "apricot", "blueberry", "cherry", "avocado", "blackberry"]
    result=split_list_based_first_char(list_)
    for i,j in result.items():
        print(f"{i}:{j}")

        
if __name__=="__main__":
    main()