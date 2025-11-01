num_str = input("Enter a two-digit number: ")

if len(num_str) != 2:
    print("Please enter a valid two-digit number.")
else:
    num = int(num_str)
    ones = num % 10
    tens = num // 10
    reversed_num = ones * 10 + tens
    print("Reversed number:", reversed_num)