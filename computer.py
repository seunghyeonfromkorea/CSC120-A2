class Computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, computer, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        self.description = computer
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_os(self, newOS) :
        self.operating_system = newOS
        print("The OS is updated to", self.operating_system)

    def update_price(self, newPrice) :
        self.price = newPrice
        print("The price is updated to", self.price)

def main():

    print("\n----- Computer Info. -----")

    comp = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    comp.update_price(2000)
    comp.update_os("MacOS Monterey") 

main()