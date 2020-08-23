input_score = int(input('Your socre: '))
if input_score <= 100:
    print('Your information is correct')
    if input_score <=49:
        print('Grade: F')
    elif input_score <=59:
        print('Grage: D')
    elif input_score <=69:
        print('Grage: C')
    elif input_score <=79:
        print('Grage: B')
    elif input_score >=80:
        print('Grage: A')
else: 
    print('Your informaton is wrong')




