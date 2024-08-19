'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program set width to text to display

'''


import textwrap

def display_method(text,width=50):
    '''
          Description: 
                this function is setting width of text in multile lines

          Parameters:
              text: text of multiple lines
              width: size of width
              
          Return :
              returning afterm setting width of code
    '''
    text_result=textwrap.fill(text,width=width)
    return text_result


def main():
   text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     Sed do eiusmod tempor incididunt ut labore et
       dolore magna aliqua."""
   print(display_method(text))


if __name__=="__main__":
    main()