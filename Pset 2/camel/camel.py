camel_case = input("camelCase:")
snake_case = ""
for i in camel_case:
    if i.isupper():
        snake_case += "_" + i.lower()
    else:
        snake_case += i

print(f"snake_case: {snake_case}")
