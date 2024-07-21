#kwargs
# def print_kwagrs(name,power):
#     print("Name ",name, "Power ",power)
# print_kwagrs(power='lazer', name='shaktiman')

def print_kwagrs(**kwagrs):
    for key, value in kwagrs.items():
        print(f"{key}:{value}")

print_kwagrs(power='lazer', name='shaktiman')
print_kwagrs(power='lazer', name='shaktiman',enmeny="Dr jackal")