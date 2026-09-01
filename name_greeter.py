# we need to greet by first name, then we test as such: 
#  1. i the user having 2 or more names? greet by first name else prompt for second name


name=input('Input your name:')

processed_name = name.split()

if len(processed_name) > 1 :
    #greeting by first name
    print(f'Greetings : {processed_name[0]}')
    
else :
    corrected_name=input('Please input more than one name:')


        
