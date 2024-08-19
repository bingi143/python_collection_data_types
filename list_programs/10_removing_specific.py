'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program removing specific items

'''


def removing_specific_items(list,index_list):
     '''
          Description: 
                this function removing the specific items based on index
          Parameters:
              list: list - The list of numbers
              index_list: index to remove
          Return :
              After removing specific items we returning list
    '''
     index=sorted(index_list,reverse=True)
     for i in index:
         item=list[i]
         list.remove(item)
     return list


def main():
    list=['red','green',"white",'black',"pink","yellow"]
    index_list=[0,4,5]
    print(f"after removing specific indexes:{removing_specific_items(list,index_list)}")


if __name__=="__main__":
    main()