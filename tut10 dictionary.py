d2={"harun":"python","indu":"matlab","jinia":"c++","anikt":{"B":"roti","D":"rice"}}
d2["aniket"]="java"
print(d2['jinia'])
print(d2["anikt"]["B"])
del d2["jinia"]
print(d2)
d3=d2
del d3["indu"]
d3.update({"xyz":"kebab"})
print(d3)
print(d2.keys())
d2.popitem()
print(d2)