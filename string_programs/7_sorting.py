'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program sorting words

'''


def sorting_order(strings):
    '''
          Description: 
                this function is sorting a words

          Parameters:
              string: string of wordsd
              
          Return :
              returning the after sorting words
    '''
    spli_=strings.split(",")
    list_=list(sorted(spli_))
    return list_


def main():
    strings=input("enter Stringwords separate coma:")
    print(f"after sorting :{sorting_order(strings)}")


if __name__=="__main__":
    main()