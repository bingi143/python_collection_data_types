'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is dispalying pretty table

'''


from prettytable import PrettyTable

def table_method(dict_):
    '''
          Description: 
                this function is displaying pretty table
          Parameters: 
              dict_: items
          Return : 
                not returnig any thing
        '''
    table=PrettyTable()
    table.field_names=['keys','values']
    for i,j in dict_.items():
        table.add_row([i,j])
    print(table)


def main():
    dict_={'name':'Venky','age':24,'group':'mca'}
    table_method(dict_)


if __name__=="__main__":
    main()