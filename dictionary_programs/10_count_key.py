'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is count key values

'''


def count_value(data_):
   '''
          Description: 
                this function is count key
          Parameters: 
              data_: items
          Return : 
                not returnig any thing
        '''
   count=0
   for dict_ in data_:
       if dict_.get('success') is True:
          count+=1
   print(count)


def main():
   data_ = [
    {'id':1,'success':True,'name':'lary'}
    ,{'id':2,'success':False,'name':'robi'}
    ,{'id':3,'success':True,'name':'venky'}]
   count_value(data_)


if __name__=="__main__":
   main()