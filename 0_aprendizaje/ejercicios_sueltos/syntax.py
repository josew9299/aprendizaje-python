import time
import datetime as dt

today = dt.date.today()
print(today)

dt.date(2027, 7,12)
today = dt.date.fromtimestamp(time.time())
print (today)


archiv = open("mi_file.txt", "w")
archiv.write("Hola, Camila")
archiv.close()

print("My favorite colors are", "blue","green", "red")

account_balance = 12
isinstance(account_balance, (int, float)) # True