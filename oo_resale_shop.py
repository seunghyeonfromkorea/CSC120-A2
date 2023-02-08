from computer import *

class ResaleShop:

    inventory = []

    def __init__(self, inventory, computer, year_made) -> None:
        self.inventory = inventory
        self.description = computer
        self.year_made = year_made
        

    def buy(self, computer) -> None:
        if self.description == computer:
            self.inventory.append(computer)
            print("Our resale shop added", computer)

    def sell(self, computer) -> None:
        if self.description == computer:
            if computer in self.inventory:
                self.inventory.remove(computer)
                print("Our resale shop sold", computer)
            else:
                print("Sold Out!")

    def refurbish(self, computer, newOS) -> None:
        if computer in self.inventory:
            if int(self.year_made) < 2000:
                Computer.price = 0
                print("The refurbished price is", Computer.price, "\n") 
            elif int(self.year_made) < 2012:
                Computer.price = 250
                print("The refurbished price is", Computer.price, "\n") 
            elif int(self.year_made) < 2018:
                Computer.price = 550
                print("The refurbished price is", Computer.price, "\n") 
            else:
                Computer.price = 1000
                print("The refurbished price is", Computer.price, "\n")

            if newOS is not None:
                Computer.operating_system = newOS
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")

    def print_inventory(self, computer):
        if len(self.inventory) != 0:
            for computer in self.inventory:
                print("Item ID:", computer, "Quantity:", len(self.inventory))
        else:
            print("Sold Out!")

            
def main():
    
    resale = ResaleShop([], "Mac Pro (Late 2013)", 2013)
    
    # buy and sell our computer
    print("\n----- Add & Remove the Computer -----")
    resale.buy("Mac Pro (Late 2013)")
    resale.buy("Mac Pro (Late 2013)")
    resale.buy("Mac Pro (Late 2013)")
    resale.sell("Mac Pro (Late 2013)")
    resale.sell("Mac Pro (Late 2013)")

    print("\n---------------------")
    resale.refurbish("Mac Pro (Late 2013)", "MacOS Monterey")

    print("----- Inventory -----")
    resale.print_inventory("Mac Pro (Late 2013)")
    
main()