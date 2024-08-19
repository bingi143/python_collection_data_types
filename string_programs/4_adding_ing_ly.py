'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program adding ing and ly in last of the string

'''


def changing_string(string_):
     '''
          Description: 
                this function is changing the string last adding ing or ly if string lenght is more than 3

          Parameters:
              string: string
              
          Return :
              returning the string after changes
    '''
     if len(string_)<3:
         return string_
     if string_[-3:]=='ing':
         string_+='ly'
         return string_
     string_=string_+'ing'
     return string_         


def main():
    string_=input("Enter String:")
    print("after changing",changing_string(string_))

    
if __name__=="__main__":
    main()