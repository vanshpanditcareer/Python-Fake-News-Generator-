#1- Import the random module
import random

#create subjects
subjects = [
    "Shahruk Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "MS Dhoni",
    "A group of monkeys",
    "Prime Minister Modi",
]

actions = [
    "launches",
    "cancels",
    "eats",
    "scored century",
    "passed bill",
    "declares war on",
    "celebrates",
]

places_or_things = [
    "at red fort",
    "mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga ghat",
    "during IPL Match",
]

#start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" Breaking News: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    userinput = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if userinput == "no":
        break

#goodbye message
print("\nThanks for using, Have a fun day!")
