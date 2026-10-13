#Refactor this code to use a regular if statement instead.
#def baz():
 #   return ('bar' if foo() else qux())

#solution

def baz():
    if foo():
        print('bar')
    else:
        print(qux())

