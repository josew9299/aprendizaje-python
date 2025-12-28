#String formating
name = "John"
age = 36
txt = "My name is " + name + "and I am "+ str(age) + "years old"
print(txt)
txt = f"My name is {name} and I am {age} years old"
print(txt)

#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#This function takes the age in years and returns the age in days.
def cal_age(age):
    return age*365

def convert(minutes):
	return minutes*60
convert(60)
print(f"60 minute is {convert(60)} seconds")