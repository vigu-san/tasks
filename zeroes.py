input = "John000Doe000123"

r = input.replace("000", ", ")
print(r)
s = r.split()
print(s)
dict1 = {"first_name": " ", "last_name": " ",  "id" : " "}

for item in s:
    dict1["first_name"] = s[0].replace(",", "")
    dict1["last_name"] = s[1].replace(",", "")
    dict1["id"] = s[2]

print(dict1)