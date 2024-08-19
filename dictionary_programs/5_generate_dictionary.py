'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is printing pair values

'''


def generate_dict(number):
    '''
          Description: 
                this function is generate dictionary upto number n:n*n
          Parameters: 
              number: number
          Return : 
                not returnig any thing
        '''
    sample={}
    for i in range(1,number+1):
        j=i
        sample[i]=j*j
    print(sample)


def main():
    number=int(input("enter number:"))
    generate_dict(number)


if __name__=="__main__":
    main()