
participants = ["Alli", "Austin", "William", "Ty", "Karma"]

def make_email(first_name):
    text = f"Dear {first_name},"
    text += "Thank you for signing up for the Lobster vs Crawfish"
    text += "Showdown of 2025. The event will be located in the"
    text += "IESB lobby on March 32, 2025.\n"
    text += "See you then, \n"
    text += "Mr. Crawfish"
    return text

emails = list(map(make_email, participants))
print(*emails)

# with a lambda function
greetings = list(map( lambda name: f"Hi, {name}", participants))
print(greetings)