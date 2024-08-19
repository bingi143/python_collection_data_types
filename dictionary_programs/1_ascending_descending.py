'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is ascending and descending order dictionary

'''


import operator

def print_method(dictionary):
    '''
          Description: 
                this function is ascending and descending order
          Parameters: 
               dictionary: paired values
          Return : 
                not returnig any thing
        '''
    ascending=sorted(dictionary,reverse=False)
    print("ascenging arder is",ascending)

    discending=dict(sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True))

    print("discending arder is",discending)


def main():
    dictionary={1:10,2:20,3:5,4:6}
    print_method(dictionary)


if __name__=="__main__":
    main()
