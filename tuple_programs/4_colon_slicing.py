'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program colon slicing 

'''


def colon_tuple(tuple_):
    '''
          Description: 
                this function we will get slicing supporate part

          Parameters:
              tuple: the set of elements
              
          Return :
              returning after slicing tuple
    '''
    tuple_result=tuple_[2:5]
    return tuple_result
    

def main():
    tuple_=(2,5,8,6,80,"venky","monkey")
    print(f"After slicing:{colon_tuple(tuple_)}")

    
if __name__=="__main__":
    main()