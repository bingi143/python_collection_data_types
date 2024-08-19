'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is uncomon items in twom lists

'''


def uncomon_items(color_list_1,color_list_2):
    '''
          Description: 
                this function is identify un comon items
          Parameters: 
                 color_list_1: set of color items in list
                 color_list_2: set of color items in list
          Return : 
                this function not returning any thing
        '''
    result=[]
    for i in color_list_1:
        if i not in color_list_2:
            result.append(i)
    print(result)


def main():
    color_list_1=set(["white","black","red"])
    color_list_2=set(["red","green"])
    uncomon_items(color_list_1,color_list_2)


if __name__=="__main__":
    main()
