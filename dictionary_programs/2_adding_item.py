'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is adding value in item

'''


def adding_items(dictionary):
    '''
          Description: 
                this function is adding items in dictionary
          Parameters: 
               dictionary: paired values
          Return : 
                not returnig any thing
        '''
    dictionary[2]=30
    print(dictionary)


def main():
   dictionary={0:10,1:20}
   adding_items(dictionary)


if __name__=="__main__":
    main()
