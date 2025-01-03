# get, keys, value ,update
a={"brand":
"bmw",
"model":"L",
"year":1964,
"color":"black"
}
print(a.get("model"))
print(a.keys())  #keys
print(a.values())   #value
a["Engine"]="x23"  #insert
print(a)
a["color"]="red" #update
print(a)
a.update({"year": 2018})
print(a)