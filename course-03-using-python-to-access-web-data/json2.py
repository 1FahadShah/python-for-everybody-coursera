import json

data = '''[
    {
     "id"   : "001",
     "x"    : "2",
     "name" : "fahad"
    },
    {
     "id"   : "002",
     "x"    : "3",
     "name" : "eren"
    }
]'''
info = json.loads(data)
print("User Count: ",len(info))
for item in info:
    print("\n")
    print("Name: ", item["name"])
    print("ID: ", item["id"])
    print("Attribue: ", item["x"])