
score = 0

print("Welcome to the European Capitals Quiz!")
print("You will be asked 10 questions. Let's begin!\n")

questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Greece": "Athens"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()

    if answer == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.\n")

print("Quiz Complete!")
print(f"You got {score} out of {len(questions)} questions correct.")
