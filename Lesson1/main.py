from pathlib import Path
#from pathlib module import Path
path = Path("Lesson1/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string)
num_digits = f"digits: {len(pi_string) - 1}"
num_decimals = f"decimals: {len(pi_string) - 2}"
print (num_digits)
print (num_decimals)

path2 = Path("Lesson1/pi_million_digits.txt")
contents = path2.read_text()
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(len(pi_string))
user_bday = input("What is your birthday? (mmddyy no slashes or dashes)")
try: 
    pi_string.index(user_bday)
    print("Your birthday is in the first million digits of pi!")
    print(f"It starts at the {pi_string.index(user_bday) - 2} decimal place")
except ValueError:
    print("Your birthday is not in the first million digits of pi...")