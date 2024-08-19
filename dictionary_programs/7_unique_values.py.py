'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is unique values

'''


def unique_values(dict_):
      '''
          Description: 
                this function is unique values 
          Parameters: 
              dict_: dictioanary key paired values
          Return : 
                not returnig any thing
        '''
      
      result=set()
      for d in dict_:
           for j in d.values():
               result.add(j)
      print(result)


def main():
     dict_=[{'v':'s001'},{'v':'s002'},{'vi':'s001'},{'vi':'s005'},{'vi':'s005'},{'v':'s009'},{'vii':'s007'}]
     unique_values(dict_)


if __name__=="__main__":
     main()