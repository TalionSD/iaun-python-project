num_str = input("Enter a two-digit number: ")

if len(num_str) != 2:
    print("Please enter a valid two-digit number.")
else:
    num = int(num_str)
    tens = num // 10
    ones = num % 10
    result1 = tens ** ones
    result2 = ones ** tens
    print(f"{tens}^{ones} = {result1}")
    print(f"{ones}^{tens} = {result2}")