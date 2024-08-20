# Criteria for having the correct email

# The most nearest charester to dectect the email is (g@.com or .in)
# 1 Email must be more then 8 charector
# 6 Upper case must not be avaible
# 2 First letter must be an alphabet
# 3 @ must be used in just one time
# 4 The position of (.) dot is only in 3rd or in 4th position
# 5 Space must not be avabile in the email isspace

email = input("Enter the Email: ")
d,j,k=0,0,0
if len(email)>=8:
    if email[0].isalpha():
        if('@' in email) and (email.count('@')==1):
            if(email[-4]=='.') or (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='@' or i=='.':
                        continue
                    else:
                        d = 1
                print("Currect Email")
                if j == 1 or k == 1 or d == 1:
                    print("Wrong Email: \nMassage: space or uppercase is not alloyed in email")            
            else:
                print("Wrong Email: \nMassage: dot(.) not present in 3rd or 4th possion")
        else:
            print("Wrong Email: \nMassage: @ must in only one time")
    else:
        print("Wrong Email: \nMassage: First letter must be alphabet")
else:
    print("Wrong Email: \nMassage: More then 8 charector")