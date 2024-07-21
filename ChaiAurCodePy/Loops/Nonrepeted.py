original_str="teeter"
for char in original_str:
    print(char)
    if original_str.count(char)==1:
        print("char is ", char)
        break