from driver import *
def main():
    d1 = Driver("Ashok", 4.5, 123, False)
    d2 = Driver("Ashok", 4.5, 123, False)
    d3 = Driver("Ram", driverId = 345, is_Online = True)
    
    print(d1.name)
    print(d3.driverId)
    print(d3.is_Online)


if __name__ == "__main__":
    main()