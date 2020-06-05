import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	lower_case = word.lower()
	if data.get(lower_case):
		return data[lower_case]
	elif len(get_close_matches(lower_case, data.keys())) > 0:
		 user_input = input(f"Did you mean {get_close_matches(word, data.keys())[0]}, instead? (yes/no): ")
		 if user_input.lower() in ('y', 'yes'):
		 	return data[get_close_matches(lower_case, data.keys())[0]]
		 elif user_input.lower() in ('n', 'no'):
		 	return "The given word does not exist."
		 else:
		 	return "Not an expected input. Thank you!"
	else:
		return "The given word does not exist."
		

output = translate(input("Enter a word: "))

if type(output) == list:
	print("Here's the meaning of the word:")
	for m in output:
		print(m)
else:
	print(output)