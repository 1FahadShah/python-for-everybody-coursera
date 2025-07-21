import json

data = '''{
    "name"   : "fahad",
    "phone"  : {
    "type"   : "int1",
    "number" : 9865412397
    },
    "email"  : {
    "hide"   : "yes"
    }
}'''

info = json.loads(data)
print("Name  ", info["name"])
print("Email ", info["email"]["hide"])