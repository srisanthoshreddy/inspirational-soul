weight =int(input("weight :"))
unit =input("(L)bs or (K)g :")
x = weight * 0.45	
y=  weight / 0.45
if unit.upper() == "L":    
 	print(f"You are {x} kilos")
elif unit.upper() == "K":	
 	print( f"You are {y} pounds")
else :
    print("unit must be either L or K") 	
 	