# Dylan Temple


def show_instructions():
    # print main menu and instructions.
    print("You awake in a dark victorian manor.")
    print("The last thing you remember is running through a forest from ominous laughter.")
    print("Try to find a way out!")
    print("Valid commands: 'go North', 'go West', 'go East', 'go South', get [item name]")


def show_winning_text():
    # print the text the player receives if he/she wins.
    print("\n----------------------------")
    print("Congratulations! You have collected all items!")
    print("You confront the Ghoul with your weapons and slay him!")
    print("You use the rest of your supplies to break out of the manor and escape!")
    print("Thanks for playing the game. Hope you enjoyed it.")


def show_losing_text():
    # print the text the player receives if he/she loses.
    print("\n----------------------------")
    print("You enter the dimly lit stairway and suddenly the door behind you shuts.")
    print("You try to open it, but it won’t budge.")
    print("You turn around only for your final sight to be a terrible and hunched Ghoul.")
    print("You have met you fate. Game Over.")
    print("Thanks for playing the game. Hope you enjoyed it.")


def print_player_status():
    print("\n----------------------------")
    print("You are in the", location)
    print("Inventory:", inventory)
    # only displays items in the room if they are not in your inventory already.
    if 'item' in rooms[location].keys() and rooms[location]['item'] not in inventory:
        print('You see a', rooms[location]['item'])
    print("----------------------------")


rooms = {
    'Lounge': {'West': 'Library'},
    'Library': {'South': 'Great Hall', 'East': 'Lounge', 'item': 'Lantern'},
    'Great Hall': {'North': 'Library', 'West': 'Cellar', 'East': 'Bedroom', 'South': 'Kitchen', 'item': 'Parchment'},
    'Cellar': {'East': 'Great Hall', 'South': 'Dungeon', 'item': 'Fire-poker'},
    'Dungeon': {'North': 'Cellar'},
    'Bedroom': {'West': 'Great Hall', 'North': 'Study', 'item': 'Key'},
    'Study': {'South': 'Bedroom', 'item': 'Pen'},
    'Kitchen': {'North': 'Great Hall', 'East': 'Storeroom', 'item': 'Lighter'},
    'Storeroom': {'West': 'Kitchen', 'item': 'Hatchet'}
}

commands = ["go North", "go West", "go East", "go South"]

inventory = []
inPlay = True
location = 'Lounge'
show_instructions()
while inPlay:
    if location == 'Dungeon' and len(inventory) < 7:
        show_losing_text()
        break
    if len(inventory) == 7 and location == 'Dungeon':
        show_winning_text()
        break
    print_player_status()
    user_action = input('Enter your move:')
    # checks if it is a valid action.
    if user_action in commands or user_action[:3] == 'get':
        # checks if user can move that direction or can get said item.
        if user_action[3:] in rooms[location].keys() and user_action in commands:
            location = rooms[location][user_action[3:]]
            print("You move {0} into the {1}".format(user_action[3:], location))
        elif user_action[:3] == 'get':
            # checks if item is actually present.
            if 'item' in rooms[location].keys():
                if user_action[4:] == rooms[location]['item'] and user_action[4:] not in inventory:
                    print("You grab the", rooms[location]['item'])
                    inventory.append(rooms[location]['item'])
                else:
                    print("That item is not here.")
            else:
                print("That item is not here.")
        else:
            print("There is no {0} entry".format(user_action[3:]))
    else:
        print("Please enter a valid command.")




