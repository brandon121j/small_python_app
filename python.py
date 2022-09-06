from pick import pick
from os import system, name

def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Other OS
    else:
        _ = system('clear')


state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
beers = ["Coors", "Miller Lite", "Bud Light", "Some gross IPA"]
choice = ["Yes", "No"]

userData = {
    "name": "",
    "age" : 0,
    "state": "",
    "city": "",
    "state": "",
    "beer": False,
}

def prompt(var, val):
    print()
    userData["{0}".format(var)] = input(val)

def select_menu(category, prompt_title, data):
    title = prompt_title
    options = data
    option, index = pick(options, title, indicator='=>', default_index=0)
    try:
        userData["{0}".format(category)] = option
    except:
        pass

clear()

print("Welcome to my app, uh... I'm not so good with names. what\'s your name again?")
prompt("name", "Please enter your name: ")

clear()

print("{0}, that\'s right and you\'re from...".format(userData["name"]))
prompt("city", "Please enter the city you're from: ")
select_menu("state", "Please choose which state you're from: ", state_names)

clear()

print("Oh so you're from {0}, {1}. That's dope".format(userData["city"], userData["state"]))
print("I'm about to grab a beer, you wa- wait a second. How old are you?")
prompt("age", "Please enter your age: ")

clear()

if int(userData["age"]) >= 21:
    title = "sick dude, what can I get you to drink?"

    options = beers

    option, index = pick(options, title, indicator='=>', default_index=0)

    userData["beer"] = option

    if option == "Some gross IPA":
        print("Can't say that'd be my first option, but here you go")
    else:
        print("ah... a man of culture I see")
else:
    print("Alright I guess I'll go grab you a caprisun or something...")

over_21_summary = f"You're {userData['name']} from {userData['city']},{userData['state']}. You're {userData['age']} and drink {userData['beer']}"
under_21_summary = f"You're {userData['name']} from {userData['city']},{userData['state']}. You're {userData['age']} and drink Capri Sun or something, I don't know"

if userData["beer"] != False:

    title = ("Alright I think I got it down this time " f"{over_21_summary}")
    options = choice
    option, index = pick(options, title, indicator='=>', default_index=0)

    if option == "Yes":
        clear()
        print("I knew i'd get it this time, cheers")
    else:
        clear()
        print("oh... so those Steelers, huh")
else:

    title = ("Alright I think I got it down this time " f"{under_21_summary}")
    options = choice
    option, index = pick(options, title, indicator='=>', default_index=0)

    if option == "Yes":
        clear()
        years_left = 21 - int(userData["age"])
        years_left_message = "a year" if years_left == 1 else f"{years_left} years"

        print(f"Sick dude, I'm gonna have to take you out for drinks in {years_left_message}")
    else:
        clear()
        print("Oh ok, you like water instead. My bad")
    