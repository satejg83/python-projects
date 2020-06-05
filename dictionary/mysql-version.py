import mysql.connector
from difflib import get_close_matches

conn = mysql.connector.connect(
	user = "ardit700_student",
	password = "ardit700_student",
	host = "108.167.140.122",
	database = "ardit700_pm1database",
) 
def get_cursor():
	cursor = conn.cursor()
	return cursor

def fetch_meaning(word):
	lower_case_word = word.lower()
	query = "SELECT * FROM Dictionary WHERE Expression = %s"
	cursor = get_cursor()
	cursor.execute(query, (lower_case_word,))
	results = cursor.fetchall()
	if results:
		close_connection(cursor)
		return results
	else:
		return "No word found."

def close_connection(cursor):
	cursor.close()
	conn.close()

def test_fetch(word):
	q = "SELECT * FROM Dictionary WHERE Expression LIKE %s"
	cursor = get_cursor()
	cursor.execute(q, (word.lower() + '%',))
	results = cursor.fetchall()
	close_connection(cursor)
	return results

user_input = input("Please enter a word: ")
# output = fetch_meaning(user_input)
output = test_fetch(user_input)
print(output)