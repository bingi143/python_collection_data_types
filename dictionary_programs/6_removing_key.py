'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is removing key from the dictionary

'''


def remove_key(dict_):
      '''
          Description: 
                this function is remove key from dictionary
          Parameters: 
              dict_: dictioanary key paired values
          Return : 
                not returnig any thing
        '''
        
      dict_.pop('age')
      print(dict_)


def main():
      dict_={'name':'venky','age':23,'gender':'male'}
      remove_key(dict_)


if __name__=="__main__":
      main()

