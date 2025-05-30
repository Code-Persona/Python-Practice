questions = ("How many cats do I have?: ",
             "What is my favorite color?: ",
             "What is my favorite food?: ",
             "What is my favorite animal?: ",
             "What is my favorite movie?: ",) #tuple of questions we will itterate through

options = (("A. 1", "B. 3", "C. 4", "D. 5"),
           ("A. Blue", "B. Red", "C. Green", "D. Yellow"),
           ("A. Pizza", "B. Sushi", "C. Tacos", "D. Salad"),
           ("A. Dog", "B. Cat", "C. Bird", "D. Fish"),
           ("A. Inception", "B. The Matrix", "C. Interstellar","D. The Godfather"),) #tuple of options we will itterate through

answers = ("A", "A", "A", "B", "C") #tuple of answers we will itterate through
guesses = [] #empty list to store the users guesses
score = 0 #variable to store the score
question_num = 0 #variable to index the current question


for question in questions: #loop through the questions tuple
  print("----------------")
  print(question)
  for option in options[question_num]: #loop through the options tuple and print each option, if we dont itterate +=1 the options wwill stay at 0 index
    print(option) #loop through the options tuple and print each option

  guess = input("Enter A, B, C, or D: ").upper() #get the users guess
  guesses.append(guess) #append the guess to the guesses list
  if guess == answers[question_num]: #check if the guess is correct
    print("Correct!")
    score += 1 #increment the score by 1 if the guess is correct
  else:
    print("Incorrect!") 
    print(f"The correct answer was {answers[question_num]} sorry!") #print the correct answer if the guess is incorrect
  question_num += 1 #increment the question number and stays in the first loop, once second loop is done increments += 1 then goes back to the first loop

print("----------------")
print("Results")
print("----------------")

print("answers: ", end="")
for answer in answers: #loop through the answers tuple and print each answer
    print(answer, end=" ") #print each answer on the same line

print("guess: ", end="")
for guess in guesses: #loop through the answers tuple and print each answer
    print(guess, end=" ") #print each answer on the same line
print()

score = int(score / len(questions) * 100) #calculate the score as a percentage
print(f"Your score is {score}%") #print the score as a percentage