x = input("Enter Your Name :")
if len(x)<3:
    print("Name must be atleast three characters")
elif len(x)>50:
	print("Name can be a maximum of 50 characters")
else :
    print("Name looks good!")