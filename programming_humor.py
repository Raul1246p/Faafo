def main():
    hello_world("print")

    name = input("Name? ")
    hello_world(name)




def hello_world(name="print"):
    if name == "print":
        print("Hello, World!")
        
    else:
        print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
