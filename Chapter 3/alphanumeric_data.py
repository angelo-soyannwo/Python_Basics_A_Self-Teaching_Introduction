
alphanumeric_characters = "abcddefghijklmnopqrstuvwxyz1234567890"

digits = "1234567890"

store = [alphanumeric_characters[i] for i in range(0, len(alphanumeric_characters))] 

data = input("Please enter a string of alphanumeric characters: ")

answer = [data[i] for i in range(0, len(data)) if data[i] in store]

StringDigits = [data[i] for i in range(0, len(data)) if data[i] in digits]
non_alphanumeric_data =  [data[i] for i in range(0, len(data)) if data[i] not in alphanumeric_characters]

print(non_alphanumeric_data)
print(answer)
print(StringDigits)

