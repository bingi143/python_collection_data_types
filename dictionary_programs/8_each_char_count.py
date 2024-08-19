'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is each char count

'''


def count_char(string):
      '''
          Description: 
                this function is count each char count
          Parameters: 
              string: set of charectes
          Return : 
                not returnig any thing
        '''
      
      result=dict()
      j=0
      for i in string:
        if i in result:
             result[i]+=1
        else:
            result[i]=1
      print(result)


def main():
    string='w3resource'
    count_char(string)


if __name__=="__main__":
    main()