'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is print histogram

'''


import matplotlib.pyplot as plt

def create_histogram(data, bins=10, title='Histogram', x_label='Value', y_label='Frequency'):
    '''
          Description: 
                this function is printining histogram
          Parameters: 
                 data: list of data
                 bins: how many bin
                 title: title of histogram
                 x_label: x-axis
                 y_label: y-axis
          Return : 
                this function not  returnting any thing
        '''
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()


def main():
    data=[3,4,5,7,7,8,9,7,1,4,5,6,8,9]
    create_histogram(data, bins=5, title='Sample Histogram', x_label='Integers', y_label='Count')


if __name__=="__main__":
    main()