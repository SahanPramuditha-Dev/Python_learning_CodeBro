def net_price(list_price,discount,tax):
    return list_price * (1-discount) * (1+tax)

#donot work until we give all 3 values for arguments
print(net_price(100,0.1,0.05))   # 94.5

print("\n-----------------------------\n")

# default arguments
def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1+tax) # list_price * (90/100) * (105/100)

print(net_price(100))   # 105.0
print(net_price(100,0.1))   # 94.5
print(net_price(500,0.1,))   # 472.5