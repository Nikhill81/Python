# Password Strength Checker

password = "Sec43@198"
password_length = len(password)

if len(password) < 6:
    strength = "Week"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Password strength is: ", strength)        
