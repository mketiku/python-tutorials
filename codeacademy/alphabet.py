VOWELS = ("a" , "e" , "i" , "o", "u")

msg = raw_input("Enter your message: ") #var for holding user message
msg.replace (" ", "")

vowel_msg = ""
vowel_count = 0 #new var to hold result of program

con_msg = ""
con_count =  0 #var to hold cons 

for letter in msg:
	if letter not in VOWELS:
		con_msg += letter
		con_count += 1
	elif letter in VOWELS:	
		vowel_msg += letter
		vowel_count += 1

print(str(vowel_count) "Vowels in input: " ,vowel_msg)
print (str(con_count) "con in Input: "  , con_msg) 
