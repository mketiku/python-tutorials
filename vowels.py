VOWELS = ("a" , "e" , "i" , "o", "u") 

msg = raw_input("Enter your message: ") #var hold raw user message
msg.replace (" ", "")

vowel_msg = "" #new var to hold result of program

consonant_msg = "" #var to hold consonants

for letter in msg:
	if letter not in VOWELS:
		consonant_msg += letter
	elif letter in VOWELS:	
		vowel_msg += letter

print("Vowels in input: " + vowel_msg 
	+ '\n' 
	+ "Consonants in Input: " + consonant_msg) 