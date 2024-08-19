'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program each charecter count in string

'''


def each_char_count(string_):
    '''
          Description: 
                this function is getting each charecter count in string

          Parameters:
              string: string
              
          Return :
              returning the dictionary of each charecter count of string
    '''
    dict_=dict()
    for i in string_:
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]=1
    return dict_


def main():
    string_=input("Enter String:")
    print("Each charecter count in dictionary",each_char_count(string_))


if __name__=="__main__":
    main()