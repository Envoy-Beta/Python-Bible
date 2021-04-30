import random

# Parent Class

class Coin:
#   Constructor
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            #Set Attributes
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    #   Rust the Coin
    def rust(self):
        self.color = self.rusty_color

    #   Clean the Coin
    def clean(self):
        self.color = self.clean_color
        #   Flip the Coin
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    # Destructuctor Method
    def __del__(self):
        print("Coin spent!")



# Class Inheritance Methods

class Pound(Coin):
    # Create a Constructor
    def __init__(self):
        # Dictionary of Data about a pound
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5

        }
        super().__init__(**data)


one_pound_coin = Pound()



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