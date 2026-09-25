#Without running the following code, what does it print? Why?
#def bar_code_scanner(serial): match serial: case '123': print('Product1') case '113': print('Product2') case '142': print('Product3') case _: print('Product not found!') bar_code_scanner('113') bar_code_scanner(142)

#solution
def bar_code_scanner(serial): 
    match serial: 
       case '123': 
        print('Product1') 
       case '113': 
        print('Product2') 
       case '142': 
        print('Product3') 
       case _: 
        print('Product not found!') 

bar_code_scanner('113')
bar_code_scanner(142)

#it prints 'product2' cause the '113' was passed into the functon
#and prints 'product not found' cause its passin integer into the function so when python checks '142' the match fails

