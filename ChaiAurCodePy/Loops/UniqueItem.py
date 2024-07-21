items =["apple","organe","banana","mango"]
unique_item=set()

for item in items:
    if item in unique_item:
        print("Dulplicate ",item)
        break
unique_item.add(item)