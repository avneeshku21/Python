# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


chai_type={
    "Masla":"spicy",
    "Ginger":"Zesty",
    "Green":"Mild"
}

chai_type["Green"]="Fresh"


#*** *******Loops
# for chai in chai_type:
#     print(chai,chai_type[chai])

# basic syntax
# for key, value in chai_type.items():
#     print(key, value)

# if "Masla" in chai_type:
#     print("Present")

# add new one element
chai_type["Earl Grey"]="Citrus"
# print(chai_type)

#*****pop method
# chai_type.popitem()// pop last item
# chai_type.pop("Ginger")
# del chai_types["Green"]

#******Copy
# chai_type_copy=chai_type.copy()
# print(chai_type_copy)


#Sytex {{},{}}
tea_shop={
    "chai":{"Masala":"Spicy"," ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"Strong"}
}

# print(tea_shop)


Squared_num={x:x**2 for x in range(6)}
print(Squared_num)

# delat All
#Squared_num.clear()



