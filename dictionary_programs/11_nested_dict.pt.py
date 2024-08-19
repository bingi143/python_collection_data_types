'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is convert list into nested dictioanry

'''


def conversion(data):
    '''
          Description: 
                this function is converting list into nested dictionary
          Parameters: 
              data: items
          Return : 
                not returnig any thing
        '''
    nested_dict={}
    dict_=nested_dict
    for i in data:
        dict_[i]={}
        dict_=dict_[i]
    print(nested_dict)


def main():
    data=['a','b','c','d']
    conversion(data)


if __name__=="__main__":
    main()