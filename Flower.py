# Robert Bradford
# 12/15/24
# This code defines a Flower class with methods to grow and bloom, and creates three flower objects.

class Flower:
    # Initialize the Flower class with a name attribute
    def __init__(self, name):
        self.name = name  # Attribute: name of the flower

    # Method to simulate the flower blooming
    def bloom(self):
        print(f"{self.name} is blooming!")

    # Method to simulate the flower growing
    def grow(self):
        print(f"{self.name} is growing!")

# Create two instances of the Flower class
rose = Flower("Rose")  # Object: rose, Attribute: "Rose"
daisy = Flower("Daisy")  # Object: daisy, Attribute: "Daisy"

# Call the bloom and grow methods on the rose object
rose.bloom()
rose.grow()

# Call the bloom and grow methods on the daisy object
daisy.bloom()
daisy.grow()

# Another flower object
tulip = Flower("Tulip")  # Object: tulip, Attribute: "Tulip"
tulip.bloom()
tulip.grow()
