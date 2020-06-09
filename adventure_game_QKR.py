# The name of this game, is Quest for the Kingdom of Rengekki. (version 2.24)
# I hope you enjoy playing, as much as I enjoyed making!
# -Col
import time
import random

weapons = [
        'Arachnibane, Blade of Extermination',
        'Bangalore, Bow of Piercing',
        'Koros, Staff of Fierce Light',
        'Oren, Hammer of Valor']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)  # 2 sec


def print_pause_2(message_to_print):
    print(message_to_print)
    time.sleep(2.5)    # 2.5 sec


def print_pause_3(message_to_print):
    print(message_to_print)
    time.sleep(3)  # 3 seconds


def print_random(message_to_print):
    print(random.choice(weapons))
    time.sleep(0)  # 3 seconds


def play_again():
    replay = input("You win! Play again?\n" "please enter Yes or No\n").lower()
    if replay == 'yes':
        QKR()
    elif replay == 'no':
        print_pause_2('Ok, Goodbye!')
        exit()
    else:
        play_again()


def intro():
    # Start of intro sequence
    print_pause("You wake up, face down in the grass")
    print_pause_2("You have no possessions, "
                  "and no memory of how you got here.")
    print_pause("In the distance, you see a smoky mountain.")
    print_pause("“That looks formidable”, you think to yourself.")
    print_pause("In the other direction, you see a shimmering city.")
    print_pause("“Doubt they’ll let me in with no money”")
    print_pause_2("Behind you, you see a dark swamp "
                  "swirling with arcane energy.")
    print_pause("“I’ve never been much of a wizard”")
    # End of intro Sequence


def field(items):
    while True:
        print_pause("Please enter the number for the "
                    "location you would like to go:\n")
        location = input("1. Glittering City\n"
                         "2. Smoky Mountain\n"
                         "3. Arcane Swamp\n")
        if location == '1':
            city(items)
        elif location == '2':
            mountain(items)
        elif location == '3':
            swamp(items)
        else:
            field(items)


def city(items):
    print_pause("You make your way toward the city.")
    if "sword" in items:
        print_pause_3('You approach the gates once more. '
                      'Captain Meliodas greets you.')
        print_pause_2('"King? What are you doing here? Go slay the spider'
                      'and restore order to the kingdom."')
        print_pause("You head back into the field.")
    elif "trophy" in items:
        print_pause_2(' Captain Meliodas greets you at the '
                      'gate and ushers you inside the palace')
        print_pause_2('You find Dyathus the Spider King kneeling '
                      'in front of the throne.')
        print_pause("Before you can challenge him for the throne, ")
        print_pause("he looks up at you with fear in his eyes.")
        print_pause_2('"That magic..."')
        print_pause_3('"The magic you used has slain many of my ancestors."')
        print_pause_3('"You have proven yourself worthy", he says, '
                      'nodding to the mountain in the distance')
        print_pause_3('"Please, spare me, and allow both humans '
                      'and spiders to live in harmony."')
        endgame(items)

    else:
        print_pause("As you approach the tall gates, a guard stops you.")
        print_pause_2("You seem to recognize him from somewhere.")
        print_pause("“Captain Meliodas?” you say.")
        print_pause("The guard’s eyes light up as he recognizes you.")
        print_pause('"King. Is that really you?')
        print_pause_3('"So much has happened since the battle, '
                      'we all thought you were dead!')
        print_pause_2('Dyathus the Spider King has taken '
                      'the throne in your absence"')
        print_pause('According to a new law he passed')
        print_pause_3('anyone who wishes to challenge him for the throne '
                      'must first prove himself in combat.”')
        print_pause('He hands you an old, rusty sword.')
        print_pause('“Slay the spider, and you may be granted entry, '
                    'my liege”.')
        print_pause("You head back into the field.")
        items.append("sword")


def mountain(items):
    print_pause("You start walking to the distant mountain.")
    if "trophy" in items:
        print_pause("Nothing more to do here.")
        print_pause("Take back your kingdom!")
    elif "sword" in items:
        print_pause_2('You begin to ascend until you see a dark cave, '
                      'where the giant spider guards the way')
        if "bane" in items:
            print_pause("You unsheathe your new weapon,")
            print_pause('and deliver a powerful blow to the spider before it '
                        'can react')
            print_pause_3("Victory!")
            print_pause('The monster releases a massive plume of red smoke '
                        'high into the air, signifying its defeat.')
            items.clear()
            items.append("trophy")
            # adding spider defeat to items list to access endgame
        else:
            print_pause('You unsheathe your new weapon, '
                        'and attack the monster!')
            print_pause("But your sword bounces off, doing no damage!")
            print_pause("The spider begins to glow with red magic")
            print_pause("We aren't ready for this fight yet, better "
                        'get out of here.')
    else:
        print_pause_2('As you begin to climb you see a big creature '
                      'in a dark cave.')
        print_pause("It's a giant spider! Thankfully it's asleep.")
        print_pause("Better not risk it.")
    print_pause('You head back to the field')


def swamp(items):
    print_pause('You walk to the swamp.')
    print_pause_2('As you enter, the trees overhead '
                  'seem to block out the sun,')
    print_pause('causing it to be dark and difficult to navigate.')
    if 'trophy' in items:
        print_pause('You wade back into the dark swamp, '
                    'but Ragulus does not greet you')
        print_pause('Nothing more to do here.')

    elif 'sword' in items:
        if 'bane' in items:
            print_pause('You wade back into the dark swamp, '
                        'but Ragulus does not greet you')
            print_pause('Nothing more to do here.')
        else:
            print_pause('Suddenly, a deep, echoing voice calls out:')
            print_pause('“Who goes there?”')
            print_pause('“It is I" You respond boldly')
            print_pause_2('"King ? I hardly recognized you."')
            print_pause_3('"What do you need from the Great Wizard Ragulus?”,'
                          ' the voice replies.')
            print_pause_2('“I seek the power to defeat the great spider '
                          'on the mountain”, you call out.')
            print_pause('"Very well."')
            print_pause('Cast your weapon into the bubbling swamp')
            print_pause_3('and I shall replace it with the power you desire."'
                          ', says Ragulus')
            print_pause_3('You cast your old sword into the swamp')
            print_pause_2('A few seconds later a chest emerges '
                          'and hovers before you.')
            print_pause('You open it, and examine your new weapon.')
            print_pause('“Behold, the legendary weapon"')
            print_random('')
            print_pause_3('"Forged by your ancestors many years ago, '
                          'to defeat the great spiders.”, bellows Ragulus')
            print_pause_3('“Thank you, Wizard Ragulus. I will not forget this '
                          'kindness", you say as you stride confidently out '
                          'of the swamp.')
            items.append("bane")
    else:
        print_pause('Suddenly, a deep, echoing voice calls out')
        print_pause('“Who goes there?”')
        print_pause_2('“I’m not sure where I am. Can you help?” you reply')
        print_pause('The voice chuckled')
        print_pause('“The Great Wizard Ragulus does not '
                    'offer help to lost fools."')
        print_pause('"You have no business here. Begone!”')
        print_pause_2('The trees began to sway, and the water began to swirl.')
        print_pause('You sprint out of the swamp in a hurry.')
        print_pause('You head back to the field')


def endgame(items):
    mercy = input("Spare Dyathus? Please enter Y or N\n").lower()
    if mercy == 'y':
        print_pause("You lower your sword.")
        print_pause_3('"Very well Dyathus", you bellow. '
                      '"This kingdom could use some peace and quiet".')
        print_pause_3('You take your rightful place at the throne, '
                      'and work tirelessly to make your kingdom a safe'
                      ' place for both humans and spiders')
        print_pause_3('Congratulations! You’ve reclaimed your throne…'
                      'for now.')
        play_again()
    elif mercy == 'n':
        print_pause('“I will not be fooled” you utter, grimacing.')
        print_pause_3('You raise your weapon to deliver the fatal blow,'
                      'but at the last second Dyathus leaps to the side,'
                      ' dodging the strike. ')
        print_pause('“You will rue this day, King!')
        print_pause('Our vengeance will be swift and definitive.')
        print_pause_3('Spiderkind will rule once more and I, Dyathus '
                      'the Spider King, will have your throne.”')
        print_pause_3('Dyathus scaled the wall and escaped through'
                      ' the window in the blink of an eye.')
        print_pause_2('“He’ll be back, you know”, '
                      'utters Captain Meliodas.')
        print_pause('“And we’ll be waiting for him”, you respond.')
        print_pause_3('Congratulations! You’ve reclaimed your throne… '
                      'for now.')
        play_again()
    else:
        endgame(items)


def QKR():
    items = []
    intro()
    field(items)


QKR()
