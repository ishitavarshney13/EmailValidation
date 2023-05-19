#Email validation in python (Using string function)
email=str(input("Enter your email: "))  #e@g.in
k,j,d=0,0,0
if len(email)>=6:   #1
    if email[0].isalpha():   #2
        if ("@" in email) and (email.count("@")==1):   #3
            if (email[-4]==".") ^ (email[-3]=="."):    #4
                for i in email:
                    if(i==i.isspace()):   #5
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): 
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Your email is not correct.")
                else:
                    print("\n !! email entered successfully !!")
            else:
                print(".extension is incorrect.")
        else:
            print("@ is either missing or more than one.")
    else:
        print("email must be start from alphabet.")
else:
    print("Your email length is too short.")
