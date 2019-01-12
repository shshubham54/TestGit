
print("how many miles did you run today?")

miles = float(input())
kms=miles*1.6
if kms>=10:
	print(f"you are a hard worker you ran {kms} today")
elif 5<kms<10:
	print(f"you are a worker you ran {kms} today")
else:
	print(f"you are lazy af you ran {kms} today")