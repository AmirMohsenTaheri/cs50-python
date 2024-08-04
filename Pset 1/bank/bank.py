customer = input(": ").lower()
if "hello" in customer:
    print("$0")
elif customer[0] == "h":
    print("$20")
else:
    print("$100")
