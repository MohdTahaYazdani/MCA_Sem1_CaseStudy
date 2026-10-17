# Experiment 5: University Student Feedback / String Dashboard

# Taking Feedback
feedback = input("Please enter your feedback: ")
search = input("Please enter your search word: ")
rep = input("Please enter your replace word: ")

# character = feedback.count("")
character = len(feedback)
word = feedback.split(" ")

# Display Dashboard
print("="*50)
print(f"{'UNIVERSITY FEEDBACK DASHBOARD':^50}")
print("="*50)
print(f"{'Characters: '} {character}")
print(f"{'Words: '} {len(word)}")
print(f"{'Uppercase: '} {feedback.upper()}")
print(f"{'Lowercase: '} {feedback.lower()}")
print(f"{'First Word: '} {word[0]}")
print(f"{'Last Word: '} {word[-1]}")
print(f"{'Search Count: '} {feedback.lower().strip().count(search.lower().strip())}")
print(f"{'Updated: '} {(feedback.lower().strip().replace(search.lower().strip(), rep.strip())).capitalize()}")
print("="*50)

