password = input("Enter your password: ")


results = {}


if len(password) < 8:
    results["length"] = False
else:
    results["length"] = True


results["digit"] = False

for i in password:
    if i.isdigit():
        results["digit"] = True
        break

results["uppercase"] = False

for i in password:
    if i.isupper():
        results["uppercase"] = True
        break



for k,v in results.items():
    print(f"{k}: {v}")


if all(results.values()):
    print("Password is strong.")
else:
    print("Password is weak.")