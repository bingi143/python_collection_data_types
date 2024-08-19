'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is number of cpu count

'''


import multiprocessing

def cpu_count():
    '''
          Description: 
                this function is getting number of cpus
          Parameters: 
                 no parameters
          Return : 
                this function returning count
        '''
    return multiprocessing.cpu_count()


def main():
    print(f"Number of CPUs: {cpu_count()}")


if __name__ == "__main__":
    main()
