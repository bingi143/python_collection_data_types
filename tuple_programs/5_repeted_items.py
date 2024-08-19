'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program repeted items in tuple

'''


def repeated_items_tuple(tuple_):
    '''
          Description: 
                this function we will get repeated items in tuple

          Parameters:
              tuple: the set of elements
              
          Return :
              returning after repeted items in list
    '''
    dict_={}
    for i in tuple_:
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]=1
    # now which value is more than one and storing into list
    list_=[item for item,value in dict_.items() if value>1]
    return list_


def main():
    tuple_=(2,5,8,6,8,2,2,80,5)
    print(f"repeted items in tuple:{repeated_items_tuple(tuple_)}")


if __name__=="__main__":
    main()