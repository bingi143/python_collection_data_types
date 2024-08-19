'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is printing last and first color

'''


def first_last_color(color_list):
    '''
          Description: 
                this function is printing last and first colors
          Parameters: 
                list_: list of elements
          Return : 
                this function not returing  any thing
        '''
    print(color_list[0],color_list[-1])


def main():
    color_list=["Red","Green","White","Black"]
    first_last_color(color_list)


if __name__=="__main__":
    main()