n = int(input("How old are you? "))

if 0 <= n <= 12:
    print("Ohhh hi, child!")

elif 13 <= n <= 17:
    print("Ohh teenager!")

elif 18 <= n <= 64:
    print("Hello, you are an adult!")

elif n >= 65:
    print("Respect for what you did, Senior!")

else:
    print("Invalid age entered!")
