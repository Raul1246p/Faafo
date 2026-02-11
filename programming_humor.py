def main():
    hello_world("print")

    name = input("name? ")
    hello_world(name)
    

def hello_world(name="print"):
    if name == "print":
        print("Hello, World!")

    elif name == "":
        print("Hello, World!")
        
    else:
        print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
