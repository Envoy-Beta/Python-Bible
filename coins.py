class Pound:

    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True


coin1 = Pound()

print(type(coin1))


print(coin1.value)
print(coin1.color)

coin1.color = "bluish"
print(coin1.color)

coin2 = Pound()
print(coin2.color)

coin1.value = 1.50
print(coin1.value)
print(coin2.value)