test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("rest Dictionary:", test_dict)
key = input("enter the word you want to check the frequency of: ")
if key in test_dict:
    print("frequency of", key, ":", test_dict[key])
else:
    print("the word is not found in the dictionary.")