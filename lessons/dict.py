"""Practicing Dictionaries."""

#name: dict<[key typee>, <value type>]
icecream:dict[str,int] = {"chocolate" : 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(icecream)

#Adding a key, vlaue pair to dictionary 
icecream["mint"] = 3
print("Mint add:")
print(icecream)
#accessing value
print("Choc orders: ")
print(icecream["chocolate"])
#adjusting value
icecream["vanilla"]=10
print(f"After adding vanilla: {icecream}")

print (len(icecream))

print ("butter" in icecream)

for key in icecream:
    #print flavour has <number> orders>
    print( f"we have {icecream[key]} orders of {[key]}")