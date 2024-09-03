#ac=234
age=int(input("enter your age:"))
if age>=20 and age<=30:
    print(f"updated ac balance:{ac+10000}")
elif age>=35 and age<=45:
    print(f"updated ac balance:{ac+15000}")
elif age>=50 and age<=70:
    print(f"updated ac balance:{ac+5000}")
else:
    print("invalid for scheme")