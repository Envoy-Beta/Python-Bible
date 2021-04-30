import random

class Pound:

# Constructor for Class Methods
    def __init__(self, rare=False):
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

#   Rust the Coin
    def rust(self):
        self.color = "greenish"

#   Clean the Coin
    def clean(self):
        self.color = "gold"

#   Flip the Coin
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

# Destructuctor Method
    def __del__(self):
        print("Coin spent!")


# Create Coins
coin1 = Pound()
coin2 = Pound()

coin1.rust()

print(coin1.color)
coin1.clean()
print(coin1.color)

def coin_flip():
    coin1.flip()
    print(coin1.heads)

coin_flip()
coin_flip()
coin_flip()
coin_flip()

del coin1
del coin2