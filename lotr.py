#It's a choose your own adventure game!

#I have included plenty of spaces in the output of my program with print() functions as well as spaces in my code for ease of reading on both ends.

#Welcome the player to the game with a simple greeting statement.

#initialize an empty list to store the player's answers for later use

#I used time and sleep to create a typewriter effect for ease of reading

#I also used colored text to indicate when some piece of information is important to remember or will be immediately pertinenent. As the game progresses, some information that wasn't relevant before will become important text and will be colored and others will become irrelevant and turn back to white text.

import sys

from time import sleep 

#creates a list of choices to store for later use in the game

list_of_choices = {

"gender": 0,
"race": 0,
"name": 0,
"first steps": 0,
"weapon choice": 0,

}

#creates a list of traits that will be used to make automatic decisions for the player later in the game 

#will store a number based on how many times a character makes a choice in a certain direction. For instance, if he or she chooses to lie three times, the dictionary will store '3' as the value for the 'dishonesty' key. The character will officially have become dishonest if they choose a certain path five times.

character_traits = {

  "honesty": 0,
  "dishonesty": 0,
  "courageous": 0,
  "cowardice": 0,
  "pride": 0,
  "humility": 0,
  "sneakiness": 0,
  "loyalty": 0,
}

def greet_user():

  #prints a opening greeting to the user

  greeting = "Welcome to \x1b[0;32;40mMiddle Earth\x1b[0m. Your grand journey is about to begin."

  for char in greeting:

    sleep(0.06)

    sys.stdout.write(char)

    sys.stdout.flush()


  print()

#Ask player to choose their gender. 

#Ask the user to input their gender, giving three options

#if the player's gender is one of the options,

  #print something to confirm their choice

#if the player enters something outside of the options,
  #print something telling them that they can't choose that option

def choose_gender():

  #gets the player's gender and saves it as a variable

  while True:

    print()

    gender_choice = "Please enter what gender your character will be. You can choose from \x1b[1;34;40mmale\x1b[0m or \x1b[1;31;40mfemale\x1b[0m. You can also enter \x1b[1;35;40m'neither'\x1b[0m if you want."

    for char in gender_choice:

      sleep(0.06)

      sys.stdout.write(char)

      sys.stdout.flush()

    player_gender = input()

    print()

    if player_gender.lower()== "female":

      female = "You're playing as a \x1b[1;31;40mfemale\x1b[0m character."
      
      #prints out an affirmation of the character's choice of gender in typewriter fashion for ease of reading

      for char in female:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      #adds the player's choice of gender to the dictionary for later use 

      list_of_choices["gender"] = player_gender.lower()

      print()

      break

    elif player_gender.lower()== "male":

      male = "You're playing as a \x1b[1;34;40mmale\x1b[0m character."

      #prints out an affirmation of the player's gender in typewrite fashion for ease of reading

      for char in male:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      #adds the player's choice of gender to the list for later use 

      list_of_choices["gender"] = player_gender.lower()

      print()

      break

    elif player_gender.lower()== "neither":

      #I wanted to include a non-binary option for people who might not want to choose a gender

      nonbinary= "You're playing as a \x1b[1;35;40mgender non-conforming\x1b[0m character."

      #prints out the character's gender in a typewriter fashion for ease of reading

      for char in nonbinary:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      #adds the player's choice of gender to the list for later use 

      list_of_choices["gender"] = "gender non-conforming"

      print()

      break

    else:

      #prints out an error statement in typewriter fashion for ease of reading and restarts the loop

      wrong = "Sorry, please pick again."

      for char in wrong:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

print()

#In case the user doesn't know about the races, givet an option to learn before they choose.

#Have the option to input all races to learn about them, or skip.

#Restart the loop if the person enters an invalid option

def info_about_race():

  i = 0

  while i == 0:

    print()
    
    the_races = "It's time to learn about the races of Middle-Earth. If you already know this information, feel free to type \x1b[1;31;40m'skip'\x1b[0m. Otherwise, please enter \x1b[1;32;40m'elf'\x1b[0m, \x1b[1;33;40m'dwarf'\x1b[0m, \x1b[1;34;40m'human'\x1b[0m, or \x1b[1;35;40m'hobbit'\x1b[0m to find out more about each race."

    for char in the_races:

      sleep(0.06)

      sys.stdout.write(char)

      sys.stdout.flush()

    race_info = input()

    if race_info.lower() == "human" or race_info.lower() == "humans":

      print()

      men_info = "\x1b[1;34;40mMen\x1b[0m are the most common race in Middle-Earth now that the \x1b[1;32;40mElves\x1b[0m are beginning their great journey over the seas and the \x1b[1;33;40mdwarves\x1b[0m seldom come out of their mountains. Many of them have very noble roots in the blood of the royal High Men, or Dunedain, but most have the blood of Lower Men. All \x1b[1;34;40mmen\x1b[0m are mortal, even those with extended lifespans like the Dunedain, which is considered to be the 'gift of men', particularly by immortal beings. \x1b[1;34;40mMen\x1b[0m have the ability to be skilled in many different fighting styles, but are especially good with \x1b[1;36;40mone- and two-handed melee weapons\x1b[0m. The most prominent \x1b[1;34;40mmen\x1b[0m of the West of this age (the Third Age) include Denethor II, the great Steward of Gondor, who rules in the King's place until his return, and his sons, \x1b[1;37;40mBoromir\x1b[0m and \x1b[1;37;40mFaramir\x1b[0m."
  
      for char in men_info:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      i = i + 1

    elif race_info.lower() == "elf" or race_info.lower() == "elves":

      print()

      elf_info = "The immortal and elusive \x1b[1;32;40mElves\x1b[0m are commonplace objects of wonder for those who consider them to be creatures of myth. They are very tall and agile; most of them are incredibly beautiful. Indeed, as the Third Age begins and many of them travel overseas to the Undying Lands, the ones who remain seem less of this world and more ethereal. They are considered the wisest and fairest of the races. Many of them devote themselves solely to the study of life and peace, such as most of the \x1b[1;32;40mElves\x1b[0m that dwell in the peaceful province of Lorien, but they can be great warriors as well. They prefer to fight with \x1b[1;36;40mranged weapons like bows\x1b[0m, but can also be handy with \x1b[1;36;40mlighter swords and most daggers\x1b[0m. Prominent \x1b[1;32;40mElves\x1b[0m of the Third Age include Elrond, lord of the great city of Rivendell, and Galadriel of Lorien."

      for char in elf_info:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      i = i + 1

    print()

    if race_info.lower() == "dwarf" or race_info.lower() == "dwarves":

      print()

      dwarf_info = "\x1b[1;33;40mDwarves\x1b[0m are the little-seen 'stunted men' who dwell underground in caves and mountains. Since the beginning of time, \x1b[1;33;40mdwarves\x1b[0m have loved the deep parts of the earth and the beauty and riches they find there. All of them, even the women, have beards: the longer, the better. They are usually around 4'6 and rarely are taller than 5 feet. \x1b[1;33;40mDwarves\x1b[0m have an uneasy alliance with \x1b[1;32;40mElves\x1b[0m due to a long-forgotten war but many manage to put aside their differences to find great friendships. \x1b[1;33;40mDwarves\x1b[0m tend to prefer mining over fighting, but are excellent and hearty warriors by necessity: in the deep places of the world, fearsome and ancient things often slumber. They are very handy with \x1b[1;36;40mtwo-handed weapons and prefer heavy war-axes\x1b[0m. Prominent \x1b[1;33;40mdwarves\x1b[0m of the current Third Age include the twelve \x1b[1;33;40mdwarves\x1b[0m who traveled to defeat Smaug with the hobbit Bilbo Baggins, chiefly Thorin and Gloin, father of \x1b[1;37;40mGimli\x1b[0m."

      for char in dwarf_info:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      i = i + 1

    elif race_info.lower() == "hobbit" or race_info.lower() == "hobbits":

      print()

      hobbit_info = "\x1b[1;35;40mHobbits\x1b[0m, or Halflings, are considered to be distant relatives of \x1b[1;34;40mmen\x1b[0m but their true origins are unknown. They are very short, hardly ever breaching four feet tall, and prefer to go barefoot most places because of their hairy and leathery feet. They are mortal beings, but have been known to live until about one-hundred and forty years. To those who know of them (many do not), they are assumed to be a simple folk who want very little beyond plentiful food and beer (six times a day when they can get it) and to grow their crops in peace. Whenever pressed, however, they are a remarkably hardy race with more skill and courage in battle than to be expected. As little \x1b[1;34;40mmen\x1b[0m, they prefer\x1b[1;36;40msmall swords and daggers as weapons\x1b[0m. The most famous \x1b[1;35;40mhobbits\x1b[0m  include the Old Took, the most prominent \x1b[1;35;40mhobbit\x1b[0m  ever born, and Bilbo Baggins, famous for his adventures with \x1b[1;33;40mdwarves\x1b[0m and friendships with \x1b[1;32;40mElves\x1b[0m."

      for char in hobbit_info:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      i = i + 1

    print()

    if race_info.lower() == "skip":

      print()

      nope = "No info needed."

      for char in nope:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      break

    elif race_info.lower() != "elf" and race_info.lower() != "elves" and race_info.lower() != "dwarf" and race_info.lower() != "dwarves" and race_info.lower() != "elf" and race_info.lower() != "elves" and race_info.lower() != "hobbit" and race_info.lower() != "hobbits" and race_info.lower() != "skip" and race_info.lower() != "human":

      print()

      oops = "Sorry, you can't play as that race. Please pick again."

      for char in oops:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      i = i + 1

  while i > 0:
    
    print()

    more_info = "Would you like to learn about another race? Type \x1b[1;32;40m'elf'\x1b[0m, \x1b[1;33;40m'dwarf'\x1b[0m, \x1b[1;34;40m'human'\x1b[0m, or \x1b[1;35;40m'hobbit'\x1b[0m to find out more about each race. If you have enough information, type \x1b[1;31;40m'exit'\x1b[0m."

    for char in more_info:

      sleep(0.06)

      sys.stdout.write(char)

      sys.stdout.flush()
    
    race_info1 = input()

    if race_info1.lower() == "human" or race_info1.lower() == "humans":

      print()

      men_info1 = "\x1b[1;34;40mMen\x1b[0m are the most common race in Middle-Earth now that the \x1b[1;32;40mElves\x1b[0m are beginning their great journey over the seas and the \x1b[1;33;40mdwarves\x1b[0m seldom come out of their mountains. Many of them have very noble roots in the blood of the royal High Men, or Dunedain, but most have the blood of Lower Men. All \x1b[1;34;40mmen\x1b[0m are mortal, even those with extended lifespans like the Dunedain, which is considered to be the 'gift of men', particularly by immortal beings. \x1b[1;34;40mMen\x1b[0m have the ability to be skilled in many different fighting styles, but are especially good with \x1b[1;36;40mone- and two-handed melee weapons\x1b[0m. The most prominent \x1b[1;34;40mmen\x1b[0m of the West of this age (the Third Age) include Denethor II, the great Steward of Gondor, who rules in the King's place until his return, and his sons, \x1b[1;37;40mBoromir\x1b[0m and \x1b[1;37;40mFaramir\x1b[0m."

      for char in men_info1:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

    elif race_info1.lower() == "elf" or race_info1.lower() == "elves":

      print()

      elf_info1 = "The immortal and elusive \x1b[1;32;40mElves\x1b[0m are commonplace objects of wonder for those who consider them to be creatures of myth. They are very tall and agile; most of them are incredibly beautiful. Indeed, as the Third Age begins and many of them travel overseas to the Undying Lands, the ones who remain seem less of this world and more ethereal. They are considered the wisest and fairest of the races. Many of them devote themselves solely to the study of life and peace, such as most of the \x1b[1;32;40mElves\x1b[0m that dwell in the peaceful province of Lorien, but they can be great warriors as well. They prefer to fight with \x1b[1;36;40mranged weapons like bows\x1b[0m, but can also be handy with \x1b[1;36;40mlighter swords and most daggers\x1b[0m. Prominent \x1b[1;32;40mElves\x1b[0m of the Third Age include Elrond, lord of the great city of \x1b[1;37;40mRivendell\x1b[0m, and Galadriel of Lorien."

      for char in elf_info1:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

    elif race_info1.lower() == "dwarf" or race_info1.lower() == "dwarves":

      print()

      dwarf_info1 = "\x1b[1;33;40mDwarves\x1b[0m are the little-seen 'stunted men' who dwell underground in caves and mountains. Since the beginning of time, \x1b[1;33;40mdwarves\x1b[0m have loved the deep parts of the earth and the beauty and riches they find there. All of them, even the women, have beards: the longer, the better. They are usually around 4'6 and rarely are taller than 5 feet. \x1b[1;33;40mDwarves\x1b[0m have an uneasy alliance with \x1b[1;32;40mElves\x1b[0m due to a long-forgotten war but many manage to put aside their differences to find great friendships. \x1b[1;33;40mDwarves\x1b[0m tend to prefer mining over fighting, but are excellent and hearty warriors by necessity: in the deep places of the world, fearsome and ancient things often slumber. They are very handy with \x1b[1;36;40mtwo-handed weapons and prefer heavy war-axes\x1b[0m. Prominent \x1b[1;33;40mdwarves\x1b[0m of the current Third Age include the twelve \x1b[1;33;40mdwarves\x1b[0m who traveled to defeat Smaug with the hobbit Bilbo Baggins, chiefly Thorin and Gloin, father of \x1b[1;37;40mGimli\x1b[0m."


      for char in dwarf_info1:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

    elif race_info1.lower() == "hobbit" or race_info1.lower() == "hobbits":

      print()

      hobbit_info1 = "\x1b[1;35;40mHobbits\x1b[0m, or Halflings, are considered to be distant relatives of \x1b[1;34;40mmen\x1b[0m but their true origins are unknown. They are very short, hardly ever breaching four feet tall, and prefer to go barefoot most places because of their hairy and leathery feet. They are mortal beings, but have been known to live until about one-hundred and forty years. To those who know of them (many do not), they are assumed to be a simple folk who want very little beyond plentiful food and beer (six times a day when they can get it) and to grow their crops in peace. Whenever pressed, however, they are a remarkably hardy race with more skill and courage in battle than to be expected. As little \x1b[1;34;40mmen\x1b[0m, they prefer \x1b[1;36;40msmall swords and daggers as weapons\x1b[0m. The most famous \x1b[1;35;40mhobbits\x1b[0m  include the Old Took, the most prominent \x1b[1;35;40mhobbit\x1b[0m  ever born, and Bilbo Baggins, famous for his adventures with \x1b[1;33;40mdwarves\x1b[0m and friendships with \x1b[1;32;40mElves\x1b[0m."

      for char in hobbit_info1:

        sleep(0.05)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

    elif race_info1.lower() == "exit":

      print()

      nope1 = "Ok, no more info needed."

      for char in nope1:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      break 

    else:

      print()

      oops1 = "Sorry, you can't play as that race. Please pick again."

      for char in oops1:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

print()

#gets user input for what race they would like to play as, now that they've had the option to learn about the different races

#appends the list with the player's choice of race

#takes proper grammar into account (an elf vs a elf)

def choose_race():

  while True:

    print()

    choosing_race = "Now that you have information about all the races, please choose what race you would like to play as: \x1b[1;32;40m'elf'\x1b[0m, \x1b[1;33;40m'dwarf'\x1b[0m, \x1b[1;34;40m'human'\x1b[0m, or \x1b[1;35;40m'hobbit'\x1b[0m ."

    for char in choosing_race:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    #gets user input for race choice

    race_choice = input()

    print()

    if race_choice.lower() == "human":

      print()

      #confirms the player's entry and adds it to the dictionary for later use

      human = "You'll be playing as a \x1b[1;34;40mhuman\x1b[0m, most versatile of all the races."

      for char in human:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      list_of_choices["race"] = race_choice.lower()

      print()

      break

    elif race_choice.lower() == "hobbit" or race_choice.lower() == "hobbits":

      print()

      hobbit = "You have chosen to play as a \x1b[1;35;40mhobbit\x1b[0m, most unsuspecting of all the races."

      for char in hobbit:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      list_of_choices["race"] = race_choice.lower()

      print()

      break

    elif race_choice.lower() == "dwarves" or race_choice.lower() == "dwarf":
      
      print()

      dwarf = "You'll be playing as a \x1b[1;33;40mdwarf\x1b[0m, most elusive and prideful of the races."

      for char in dwarf:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      list_of_choices["race"] = race_choice.lower()

      print()

      break

    if race_choice.lower() == "elf" or race_choice.lower() == "elves":

      print()

      elf = "You'll be playing as an \x1b[1;32;40melf\x1b[0m, wisest and fairest of all the races."
    
      for char in elf:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      print()

      list_of_choices["race"] = race_choice.lower()

      print()

      break

    else:

      print()

      print("Sorry, you can't play as that race. Please choose again.")

      print()

print()

#choose a character's name and adds it to the dictionary for later use

def choose_name():

  print()

  name = "Please choose a name for your character."

  for char in name:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

  user_name = input()

  print()

  list_of_choices["name"] = user_name

  if list_of_choices["race"] == "hobbit" or list_of_choices["race"] == "elf" or list_of_choices["race"] == "dwarf" or list_of_choices["race"] == "human":

    sentence = "You are playing as {} the {} {}.".format(user_name, list_of_choices["gender"], list_of_choices ["race"])
    
    for char in sentence:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    print()

def origin_place():

#defines where the character starts the game depending on what race they chose. establishes basic knowledge about what will happen in the game

  if list_of_choices['race'] == "human":

    print()

    human_origin = "You begin your journey at the greatest city of Western Men, \x1b[1;37;40mMinas Tirith\x1b[0m. You accompany \x1b[1;37;40mBoromir\x1b[0m and his company to \x1b[1;37;40mRivendell\x1b[0m, as you have been summoned on urgent business to attend an important council. You've heard vague rumors that this concerns the fabled \x1b[1;31;40m'Isildur's Bane'\x1b[0m, though no one is really sure what this is. You are eager to find out more about these strange events."
    
    print()

    for char in human_origin:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    print()

  elif list_of_choices["race"] == "elf":

    print()

    elf_origin = "You begin your journey at the Elven city of \x1b[1;37;40mRivendell\x1b[0m. \x1b[1;36;40mElrond\x1b[0m, lord of the city, has alerted you that there are some very important visitors coming to visit to hold a high-level council. You've heard rumors of something about hobbits and the \x1b[1;31;40mRings of Power\x1b[0m, but are unsure about specifics. You're anxious for the council to occur."

    print()

    for char in elf_origin:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    print()

  elif list_of_choices["race"] == "dwarf":

    print()

    dwarf_origin = "You begin your journey at the great Dwarven city of the Lonely Mountain. Your lord has instructed you to travel to the Elven city of \x1b[1;37;40mRivendell\x1b[0m to attend an extremely important council. You are unsure of what will occur or what this council will concern, but you've sensed an uneasiness about your traveling kinsmen of late. You know something important will be discussed."

    print()

    for char in dwarf_origin:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    print()
    
  elif list_of_choices["race"] == "hobbit":

    print()

    hobbit_origin = "You begin your journey at the peaceful province of \x1b[1;37;40mHobbiton in the Shire\x1b[0m. As a good friend of \x1b[1;36;40mFrodo Baggins\x1b[0m, you are attending him on his journey to \x1b[1;37;40mBree\x1b[0m and then to the Elven city of \x1b[1;37;40mRivendell\x1b[0m. He hasn't told you exactly why you're taking the journey, but you know that it concerns his \x1b[1;31;40mgolden ring\x1b[0m. You are entirely out of your element and unsure of what you will face on the journey, but you're sure it's nothing you can't handle."

    for char in hobbit_origin:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    print()


def direction_choice():

# gives the player an initial two choices of paths to take to Rivendell based on their race choice. Because the elf character starts in Rivendell, their story doesn't actually initialize until a little later on

#gives the player an option to learn about their two paths in order to choose the one they think will be best. Also gives the option to skip in case the player thinks they don't need the information

  if list_of_choices["race"] == "human":

    i = 0

    #Note: this is not canonically correct. In the books, Boromir set off alone and armed with only the directions of an ancient riddle to help him find Rivendell. For simplicity's sake, we will forgo this difficulty and include the two main routes one can take to reach Rivendell from Gondor. 

    #Prompts the player to choose a route. Offers an input to find out more information about each route (possible dangers, how long, etc.)

    print()

    direction_prompt = "You must now choose which direction to go. In order to reach \x1b[1;37;40mRivendell\x1b[0m, you must decide which way to go. You can choose either the way through the \x1b[1;33;40mGap of Rohan\x1b[0m or journey towards the  \x1b[1;33;40mMines of Moria\x1b[0m. To learn more about each route, type either \x1b[1;33;40m'mines'\x1b[0m or  \x1b[1;33;40m'gap'\x1b[0m. If you are confident in your choice, you may type \x1b[1;31;40m'skip'\x1b[0m to reach the next part of your decision."

    for char in direction_prompt:

      sleep(0.06)

      sys.stdout.write(char)

      sys.stdout.flush()

    direction = input()

    print()

    while i == 0:

      if direction.lower() == "mines":

        print()

        mines_choice = "The \x1b[1;33;40mMines of Moria\x1b[0m are the ancient dwellings of the old dwarves of the Misty Mountains. The name of \x1b[1;33;40mMoria\x1b[0m itself is associated with fear-- there's dark rumors that the dwarves dug too deep and awakened an ancient evil. Luckily, you won't be going through the mines-- just over the Misty Mountains through the High Pass. The journey is \x1b[1;34;40mlong and difficult\x1b[0m, for the mountains have become treacherous as of late with orcs and goblins, but \x1b[1;37;40mRivendell\x1b[0m lies directly on the High Pass, making access easy. This path will be about \x1b[1;35;40mone thousand miles\x1b[0m."

        for char in mines_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        i = i + 1

      elif direction.lower() == "gap":
        
        print()

        gap_choice = "The \x1b[1;33;40mGap of Rohan\x1b[0m is the gap between the Misty Mountains and the White Mountains. This would appear to be the easier path but for the murmurings of a unsuspected darkness in the wizard \x1b[1;31;40mSaruman\x1b[0m, who resides in Isengard close to the \x1b[1;33;40mGap of Rohan\x1b[0m. You are unsure why, but the idea of passing this way makes you uneasy though your captain, \x1b[1;37;40mBoromir\x1b[0m, thinks it the best way to go. This way will make the journey about \x1b[1;35;40mnine hundred miles\x1b[0m, making it the shorter route."

        for char in gap_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        i = i + 1

      elif direction.lower() == "skip":

        pass

        break

      else:

        print("Invalid response.")
  
    while i > 0:

      direction_choice_2ndit = "Would you like to know about the other path you can take? Enter \x1b[1;31;40m'yes'\x1b[0m to see the other option or \x1b[1;34;40m'no'\x1b[0m to exit."

      for char in direction_choice_2ndit:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()
      
      yes_or_no = input()

      if direction.lower() == "gap" and yes_or_no == "yes":

        print()

        mines_2ndit = "The \x1b[1;33;40mMines of Moria\x1b[0m are the ancient dwellings of the old dwarves of the Misty Mountains. The name of \x1b[1;33;40mMoria\x1b[0m itself is associated with fear-- there's dark rumors that the dwarves dug too deep and awakened an ancient evil. Luckily, you won't be going through the mines-- just over the Misty Mountains through the High Pass. The journey is \x1b[1;34;40mlong and difficult\x1b[0m, for the mountains have become treacherous as of late with orcs and goblins, but \x1b[1;37;40mRivendell\x1b[0m lies directly on the High Pass, making access easy. This path will be about \x1b[1;35;40mone thousand miles\x1b[0m."

        for char in mines_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        break
      
      elif direction.lower() == "mines" and yes_or_no == "yes":
        
        print()

        gap_2ndit = "The \x1b[1;33;40mGap of Rohan\x1b[0m is the gap between the Misty Mountains and the White Mountains. This would appear to be the easier path but for the murmurings of a unsuspected darkness in the wizard \x1b[1;31;40mSaruman\x1b[0m, who resides in Isengard close to the \x1b[1;33;40mGap of Rohan\x1b[0m. You are unsure why, but the idea of passing this way makes you uneasy though your captain, \x1b[1;37;40mBoromir\x1b[0m. thinks it the best way to go. This way will make the journey about \x1b[1;35;40mnine hundred miles\x1b[0m, making it the shorter route."

        for char in gap_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        break
      
      elif yes_or_no == "no":

        print()

        break

  if list_of_choices["race"] == "dwarf":

    i = 0 

    direction_choice1 = "Your journey from the Lonely Mountain will be long no matter which route one takes. \x1b[1;37;40mGimli\x1b[0m, captain of your division, has narrowed the paths down to two: through the infamous \x1b[1;33;40mMirkwood\x1b[0m or via the \x1b[1;33;40mMisty Mountains\x1b[0m. Being a tried and true dwarf, \x1b[1;37;40mGimli\x1b[0m favors the \x1b[1;33;40mMisty Mountains\x1b[0m but leaves the decision up to you. Enter \x1b[1;33;40m'forest'\x1b[0m to see more about the \x1b[1;33;40mMirkwood\x1b[0m, \x1b[1;33;40m'mountains'\x1b[0m to learn more about the \x1b[1;33;40mMisty Mountains\x1b[0m route, or \x1b[1;31;40m'skip'\x1b[0m if you're confident about your choice."

    for char in direction_choice1:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    direction1 = input()

    while i == 0:

      if direction1.lower() == "forest":

        print()

        mirkwood_choice = "The \x1b[1;33;40mMirkwood\x1b[0m is inhabited by the dwarves' lesser trusted allies, the \x1b[1;32;40mElves\x1b[0m. Of the three largest remaining elven cities, including Lorien and \x1b[1;37;40mRivendell\x1b[0m, the inhabitants of \x1b[1;33;40mMirkwood\x1b[0m are known for being less trusting and hardier in battle. Running into them might be unpleasant, though most likely not deadly, considering a delegation of \x1b[1;32;40melves\x1b[0m is rumored to be setting out from \x1b[1;33;40mMirkwood\x1b[0m for the same council. This route is much shorter than that of the \x1b[1;33;40mMisty Mountains\x1b[0m-- about \x1b[1;35;40mfour hundred miles\x1b[0m --which is why \x1b[1;37;40mGimli\x1b[0m even considers it. It is also the far easier route in terms of terrain."

        for char in mirkwood_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        i = i + 1

      elif direction1.lower() == "mountains":

        print()

        mountains_choice = "The \x1b[1;33;40mMisty Mountains\x1b[0m are the ancient dwelling place of the dwarven lords of old, and are well-loved and revered by dwarves across Middle-Earth. \x1b[1;33;40mMoria\x1b[0m, the great dwarven city in the depths of the mountains, is rumored to be filled with darkness despite its rich depths filled with precious mithril, the most expensive of all metals. It is not, however, necessary to go through \x1b[1;33;40mMoria\x1b[0m to get to \x1b[1;37;40mRivendell\x1b[0m: the difficult climb up the High Pass is the easier way to reach \x1b[1;37;40mRivendell\x1b[0m. It's a rough journey up a steep mountain, rumored to be swarmed with goblins due to its proximity to Goblin City, and about \x1b[1;35;40msix hundred miles\x1b[0m."

        for char in mountains_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        i = i + 1

      elif direction1.lower() == "skip":

        pass

        break

      else:

        print()

        wrong1 = "This is an invalid response."

        for char in wrong1:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

    while i > 0:

      print()

      direction_choice_2ndit = "Would you like to know about the other path you can take? Enter \x1b[1;31;40m'yes'\x1b[0m to see the other option or \x1b[1;34;40m'no'\x1b[0m to exit."

      for char in direction_choice_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()
      
      yes_or_no1 = input()

      if yes_or_no1.lower() == "yes" and direction1 == "mountains":

        print()

        mirk_2ndit = "The \x1b[1;33;40mMirkwood\x1b[0m is inhabited by the dwarves' lesser trusted allies, the \x1b[1;32;40mElves\x1b[0m. Of the three largest remaining elven cities, including Lorien and \x1b[1;37;40mRivendell\x1b[0m, the inhabitants of \x1b[1;33;40mMirkwood\x1b[0m are known for being less trusting and hardier in battle. Running into them might be unpleasant, though most likely not deadly, considering a delegation of \x1b[1;32;40melves\x1b[0m is rumored to be setting out from \x1b[1;33;40mMirkwood\x1b[0m for the same council. This route is much shorter than that of the \x1b[1;33;40mMisty Mountains\x1b[0m-- about \x1b[1;35;40mfour hundred miles\x1b[0m --which is why \x1b[1;37;40mGimli\x1b[0m even considers it. It is also the far easier route in terms of terrain."
      
        print()

        for char in mirk_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()
      
        break
      
      elif yes_or_no1.lower() == "yes" and direction1== "forest":
        
        print()

        forest_2ndit = "The \x1b[1;33;40mMisty Mountains\x1b[0m are the ancient dwelling place of the dwarven lords of old, and are well-loved and revered by dwarves across Middle-Earth. \x1b[1;33;40mMoria\x1b[0m, the great dwarven city in the depths of the mountains, is rumored to be filled with darkness despite its rich depths filled with precious mithril, the most expensive of all metals. It is not, however, necessary to go through \x1b[1;33;40mMoria\x1b[0m to get to \x1b[1;37;40mRivendell\x1b[0m: the difficult climb up the High Pass is the easier way to reach \x1b[1;37;40mRivendell\x1b[0m. It's a difficult journey up a steep mountain, rumored to be swarmed with goblins due to its proximity to Goblin City, and about \x1b[1;35;40msix hundred miles\x1b[0m."

        print()

        for char in forest_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()
        
        break
      
      elif yes_or_no1 == "no":
        
        print()

        break

      
  if list_of_choices["race"] == "hobbit":

    i = 0

    print()

    direction_choice2 = "There are three other hobbits joining \x1b[1;36;40mFrodo\x1b[0m, on his journey to \x1b[1;37;40mRivendell\x1b[0m: \x1b[1;36;40mSamwise Gamgee, Peregrin Took (also known as Pippin), and Meriadoc Brandybuck (also known as Merry)\x1b[0m. The five of you have narrowed your paths down to two, but the drawing of straws has left you with the responsibility of choosing which one is best. You have communally decided that heading for the small hillside town of \x1b[1;33;40mBree\x1b[0m is the best plan, but getting there is dependent on you. You can either head to \x1b[1;36;40mFrodo's\x1b[0m second house at  \x1b[1;33;40mCrickhollow\x1b[0m to give your small party a little break or head straight on to \x1b[1;33;40mBree\x1b[0m. To find out more about each option, type \x1b[1;33;40m'crick'\x1b[0m, \x1b[1;33;40m'Bree'\x1b[0m, or \x1b[1;31;40m'skip'\x1b[0m if you're confident about your choice."

    for char in direction_choice2:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    direction2 = input()

    print()
    
    while i == 0:

      if direction2.lower() == "crick":

        print()

        crick_choice = "\x1b[1;33;40mCrickhollow\x1b[0m is \x1b[1;36;40mFrodo's\x1b[0m second house in the Shire, in addition to his beloved Bag End. The leisure-loving \x1b[1;36;40mPippin\x1b[0m enjoys the idea of scheduling a break from travel and enjoying a day or two of rest and good meals before setting out for weeks of sleeping on the ground and eating cold food. But \x1b[1;36;40mFrodo\x1b[0m and the others seem uneasy, and you understand why: \x1b[1;31;40mdark figures riding on huge black horses\x1b[0m have been seen terrorizing inhabitants of the Shire. You're unsure of what you're frightened of, but you feel as if you should avoid this way. Going to \x1b[1;33;40mCrickhollow\x1b[0m will shorten the journey by a \x1b[1;35;40msmall amount of fifty miles to about seventy-five miles but will increase the journey time by at least two days\x1b[0m."

        for char in crick_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        i = i + 1

        print()
    
      elif direction2.lower() == "bree":

        print()

        bree_choice = "\x1b[1;33;40mBree\x1b[0m is a small town about one hundred and thirty-five miles from the door of Bag End. \x1b[1;36;40mFrodo's\x1b[0m dear friend, the wizard \x1b[1;36;40mGandalf the Grey\x1b[0m, recommended going towards \x1b[1;33;40mBree\x1b[0m immediately instead of detouring to \x1b[1;33;40mCrickhollow\x1b[0m, since he will be waiting there to assist the party in their journey to \x1b[1;37;40mRivendell\x1b[0m. He also has a friend who runs an inn who will be expecting your friends. Because of the fact that \x1b[1;33;40mBree\x1b[0m is further away than \x1b[1;33;40mCrickhollow\x1b[0m by about \x1b[1;35;40mfifty miles\x1b[0m, there's a risk associated with being on the road longer. It's undeniable that this will put the party at a greater risk."

        for char in bree_choice:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        i = i + 1

        print()
    
      elif direction2.lower() == "skip":

        print()

        pass

        break
    
      else:

        wrong = "Invalid response. Please enter again."

        for char in wrong:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

    while i > 0 :

      print()

      direction_choice_2ndit = "Would you like to know about the other path you can take? Enter \x1b[1;31;40m'yes'\x1b[0m to see the other option or \x1b[1;34;40m'no'\x1b[0m to exit."

      for char in direction_choice_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()
      
      yes_or_no = input()

      if yes_or_no.lower() == "yes" and direction2.lower() == "bree":

        print()

        crick_2ndit = "\x1b[1;33;40mCrickhollow\x1b[0m is \x1b[1;36;40mFrodo's\x1b[0m second house in the Shire, in addition to his beloved Bag End. The leisure-loving \x1b[1;36;40mPippin\x1b[0m enjoys the idea of scheduling a break from travel and enjoying a day or two of rest and good meals before setting out for weeks of sleeping on the ground and eating cold food. But \x1b[1;36;40mFrodo\x1b[0m and the others seem uneasy, and you understand why: \x1b[1;31;40mdark figures riding on huge black horses\x1b[0m have been seen terrorizing inhabitants of the Shire. You're unsure of what you're frightened of, but you feel as if you should avoid this way. Going to \x1b[1;33;40mCrickhollow\x1b[0m will shorten the journey by a \x1b[1;35;40msmall amount of fifty miles to about seventy-five miles but will increase the journey time by at least two days\x1b[0m."

        for char in crick_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()
        
        break

      if yes_or_no.lower() == "yes" and direction2.lower() == "crick":

        print()

        bree_2ndit = "\x1b[1;33;40mBree\x1b[0m is a small town about one hundred and thirty-five miles from the door of Bag End. \x1b[1;36;40mFrodo's\x1b[0m dear friend, the wizard \x1b[1;36;40mGandalf the Grey\x1b[0m, recommended going towards \x1b[1;33;40mBree\x1b[0m immediately instead of detouring to \x1b[1;33;40mCrickhollow\x1b[0m, since he will be waiting there to assist the party in their journey to \x1b[1;37;40mRivendell\x1b[0m. He also has a friend who runs an inn who will be expecting your friends. Because of the fact that \x1b[1;33;40mBree\x1b[0m is further away than \x1b[1;33;40mCrickhollow\x1b[0m by about \x1b[1;35;40mfifty miles\x1b[0m, there's a risk associated with being on the road longer. It's undeniable that this will put the party at a greater risk."

        for char in bree_2ndit:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        break

      elif yes_or_no == "no":

        print()

        pass

        break

def first_steps():

#the first real decision the player makes in the game. now that the player has information about their choice of paths to Rivendell, they must choose which one they want to follow based on their race

#also has an invalid choice if the player accidentally enters the wrong keyword

#stores the player's "first steps" in the dictionary for later use

  if list_of_choices["race"] == "human":

    print()

    first_steps_choice = "Now that you know more about the paths you can take, it's time to choose which path you'll take. Please type either \x1b[1;33;40m'mines'\x1b[0m or \x1b[1;33;40m'gap'\x1b[0m."

    for char in first_steps_choice:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    first_steps1 = input()

    while True:

      if first_steps1.lower() == "gap":

        print()

        gap_route = "You have chosen to go through the \x1b[1;33;40mGap of Rohan\x1b[0m, close to both the wizard \x1b[1;31;40mSaruman\x1b[0m and your allies in Rohan."

        for char in gap_route:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        list_of_choices["first steps"] = first_steps1.lower()

        break

      elif first_steps1.lower() == "mines":

        print()

        mines_route = "You have chosen to go through \x1b[1;33;40mthe High Pass over the dwarven city of Moria\x1b[0m, close to \x1b[1;37;40mRivendell\x1b[0m and the dreaded Goblin City."
        
        for char in mines_route:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()
         
        list_of_choices["first steps"] = first_steps1.lower()

        break
        
      else:

        wrong = "Invalid choice. Please choose again."

        for char in wrong:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

  if list_of_choices["race"] == "dwarf":

    print()

    first_steps_choice2 = "Now that you know your options, it's time to choose which route you would like to take. Please choose from the \x1b[1;33;40mforest of Mirkwood\x1b[0m or the \x1b[1;33;40mHigh Pass\x1b[0m, typing \x1b[1;33;40m'forest'\x1b[0m or \x1b[1;33;40m'pass'\x1b[0m."

    for char in first_steps_choice2:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    first_steps2 = input()

    while True:

      if first_steps2.lower() == "forest":

        print()

        forest_route = "You have chosen to enter the \x1b[1;33;40mMirkwood\x1b[0m, home of your tentative allies, \x1b[1;31;40mthe Elves of Mirkwood\x1b[0m. You are lucky that you are at least relatively friendly towards these Elves. You've heard they can be deadly with a bow."

        for char in forest_route:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        list_of_choices["first steps"] = first_steps2.lower()

        print()

        break

      elif first_steps2 == "pass":

        print()

        pass_route = "You have chosen to take the traditional journey over the \x1b[1;33;40mMisty Mountains and close to the great ancient city of Moria\x1b[0m. You'll have to be careful to stay away from the goblins that tend to prowl the area due to the Pass's proximity to the Goblin City."

        for char in pass_route:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        list_of_choices["first steps"] = first_steps2.lower()

        break

      else:

        wrong = "Invalid choice. Please choose again."

        for char in wrong:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

  if list_of_choices["race"] == "hobbit":

    print()

    first_steps_choice3 = "Now that you know about the journey options you have, it's time to choose which way to take to get to \x1b[1;33;40mBree\x1b[0m. Please type \x1b[1;33;40m'Crickhollow'\x1b[0m if you'd like to take the detour to rest at \x1b[1;33;40mCrickhollow\x1b[0m or \x1b[1;33;40m'Bree'\x1b[0m if you'd like to go directly to the little town of \x1b[1;33;40mBree\x1b[0m."

    for char in first_steps_choice3:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

    first_steps3 = input()

    while True:

      if first_steps3.lower() == "bree":

        print()

        bree_route = "You have chosen to take the path directly to the town of \x1b[1;33;40mBree\x1b[0m, where \x1b[1;36;40mGandalf\x1b[0m and his friend \x1b[1;36;40mBarliman Butterbur\x1b[0m, who runs \x1b[1;33;40mBree's\x1b[0m very successful pub and inn, the Prancing Pony, will be waiting. \x1b[1;36;40mPippin\x1b[0m is rather disappointed that there won't be a bed to sleep on for a few hundred miles but it might actually be safer on the road than in the towns that the \x1b[1;31;40mdark riders\x1b[0m have been frequenting."

        for char in first_steps_choice3:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        list_of_choices["first steps"] = "bree"

        print()

        break
      
      elif first_steps3.lower() == "crickhollow":

        print()

        crick_route = "You have made the decision to travel to the comfortable house, \x1b[1;33;40m'Crickhollow'\x1b[0m, to give the party well-deserved time to rest and gather supplies. \x1b[1;36;40mPippin\x1b[0m is sure to be thrilled at the opportunity to eat a few more hot meals. The other members of the party, though are nervous about the idea of going to a place where one of the \x1b[1;31;40mblack riders\x1b[0m has been seen in the past week."

        for char in crick_route:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

        list_of_choices["first steps"] = "crickhollow"
        
        break

      else:
        
        print()

        wrong = "Invalid choice. Please choose again."

        for char in wrong:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        print()

def second_steps():

#the player's "second steps": the second part of their much larger journey to Rivendell. 

#depending on the first choice the player made, this decision will lead the player into the next unique choice of the game

#has an option for an invalid choice in case of an incorrect input

#one of the main decisions made in this function will involve the weapon the player wants to use until they reach Rivendell, where they will have a greater range of choices

  if list_of_choices["race"] == "human":

    if list_of_choices["first steps"] == "gap":

      print()

      gap_beginning = "You and your small party head off for the \x1b[1;33;40mGap of Rohan\x1b[0m. About fifty miles in, you run into a roving gang of orcs bearing the \x1b[1;31;40mmark of a white hand\x1b[0m painted on their shields. You are near the Firen Woods, without help, and are forced to attack. Since this is likely to happen often on this well-traveled route, you must choose a weapon to use for the remainder of the journey, of which you have two choices: a \x1b[1;33;40mone-handed sword with less attack but with the ability to use a shield\x1b[0m or a \x1b[1;33;40mtwo handed sword with a large amount of attack but no ability to block\x1b[0m. Enter \x1b[1;33;40m'one'\x1b[0m for the \x1b[1;33;40mone-handed sword and shield\x1b[0m and \x1b[1;33;40m'two'\x1b[0m for the \x1b[1;33;40mtwo-handed sword\x1b[0m. Hurry! Your company needs you!"

      for char in gap_beginning:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      second_steps_gap = input()

      while True:

        if second_steps_gap.lower() == "one":

          print()

          one_handed_sword = "You have chosen the \x1b[1;33;40mone-handed sword and shield\x1b[0m to use during the journey. With your fast and frequent attacks, you make quick work of the orcs and successfully prevent your party from being harmed in any major way."

          for char in one_handed_sword:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "one-handed sword"

          break

        elif second_steps_gap.lower() == "two":
        
          print()

          two_handed_sword = "You have chosen the \x1b[1;33;40mtwo-handed broadsword\x1b[0m to use during the journey. With your devastating and brutal attacks, you make quick work of the orcs and successfully prevent your party from being harmed in any major way."

          for char in two_handed_sword:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()

          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "two-handed sword"

          break

        elif second_steps_gap != "two" or second_steps_gap != "one":

          print()

          oops = "That is not a valid choice. Please try again."
    

    elif list_of_choices["first steps"] == "mines":
    
      mines_beginning = "You and your small party set off on the long journey to the \x1b[1;33;40mMisty Mountains\x1b[0m and \x1b[1;37;40mRivendell\x1b[0m. Along the way, you pass by the infamous Dead Marshes, where you are beset by a roving goblin gang. Since this is likely to happen often on this rarely-traveled but dangerous route, you must choose a weapon to use for the remainder of the journey, of which you have two choices: a \x1b[1;33;40mone-handed sword with less attack but with the ability to use a shield\x1b[0m or \x1b[1;33;40mtwo handed sword with a large amount of attack but no ability to block\x1b[0m. Enter \x1b[1;33;40m'one'\x1b[0m for the \x1b[1;33;40mone-handed sword and shield\x1b[0m and \x1b[1;33;40m'two'\x1b[0m for the \x1b[1;33;40mtwo-handed sword\x1b[0m. Hurry! Your company needs you!" 

      for char in mines_beginning:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      second_steps_mines = input()

      while True:

        if second_steps_mines.lower() == "one":

          print()

          one_handed_sword1 = "You have chosen the \x1b[1;33;40mone-handed sword and shield\x1b[0m to use during the journey. With your fast and frequent attacks, you make quick work of the orcs and successfully prevent your party from being harmed in any major way."

          for char in one_handed_sword1:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "one-handed sword"

          break

        elif second_steps_gap.lower() == "two":
        
          print()

          two_handed_sword1 = "You have chosen the \x1b[1;33;40mtwo-handed broadsword\x1b[0m to use during the journey. With your devastating and brutal attacks, you make quick work of the orcs and successfully prevent your party from being harmed in any major way."

          for char in two_handed_sword1:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "two-handed sword"

          break

        elif second_steps_gap != "two" or second_steps_gap != "one":

          print()

          oops = "That is not a valid choice. Please try again."

  elif list_of_choices["race"] == "hobbit":

    if list_of_choices["first steps"] == "crickhollow":
      
      print()
      
      second_steps_house = "Your small party makes it about fifty miles before the sight of the dreaded \x1b[1;31;40mBlack Rider\x1b[0m who has apparently been riding on the main roads around Hobbiton. \x1b[1;36;40mFrodo\x1b[0m seemed to be aware of it even before you heard its hunting cries behind you, which is part of why it didn't catch anyone. You manage to get your small party out of sight before the \x1b[1;31;40mRider\x1b[0m reaches you. Many tense minutes pass before the \x1b[1;31;40mRider\x1b[0m moves on and after your party feels safe enough to move again, you decide it's time to distribute weapons in order to prepare for the worst. You're sure this is not the last danger you will enounter. \x1b[1;36;40mFrodo\x1b[0m, who has brought along a bag of weapons for these sorts of situations, offers you the choice of a \x1b[1;33;40msmall two-handed sword\x1b[0m or a \x1b[1;33;40mdagger with a small shield\x1b[0m. Enter \x1b[1;33;40m'sword'\x1b[0m if you want to choose the \x1b[1;33;40msword\x1b[0m or \x1b[1;33;40m'dagger'\x1b[0m if you'd prefer to use the \x1b[1;33;40mlighter dagger and shield combination\x1b[0m."
      
      for char in second_steps_house:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

      second_steps_crick = input()

      while True:

        if second_steps_crick == "sword":
        
          print()

          hobbit_sword = "You have chosen the \x1b[1;33;40msmall sword\x1b[0m as a weapon in case of emergencies. Since the sword is relatively large compared to your size and strength, you will be using it as a two-handed sword despite the fact that it's relatively small. You have never wielded a weapon like this before, but how hard can it be?"

          for char in hobbit_sword:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "hobbit two-handed sword"

          break

        elif second_steps_crick == "dagger":
        
          print()

          hobbit_dagger = "You have chosen the \x1b[1;33;40mdagger\x1b[0m a weapon in case of emergencies. Despite the dagger's small size, it's relatively large as a \x1b[1;35;40m'hobbit'\x1b[0m weapon, which means you will likely be using it more as a very short one-handed sword and will be able to protect yourself with a \x1b[1;33;40msmall Dwarven metal shield\x1b[0m \x1b[1;36;40mFrodo\x1b[0m happens to have. You have never wielded weapons like this before, but how hard can it be?"

          for char in hobbit_dagger:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "hobbit one-handed sword"

          break

        else:

          print()

          oops = "Sorry, that is an incorrect choice. Please choose \x1b[1;33;40m'sword'\x1b[0m or \x1b[1;33;40m'dagger'\x1b[0m."

          for char in oops:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

    elif list_of_choices["first steps"] == "bree":

      print()

      second_steps_town = "You are about fifty miles on the main road leading to the Brandywine Bridge, which you will pass over to enter \x1b[1;33;40mBree\x1b[0m, when you hear a horrible and inhuman sound a ways behind you. It curdles your blood and seems to turn it to ice, but \x1b[1;36;40mFrodo\x1b[0m manages to get the small party off the road in time before a \x1b[1;31;40mBlack Rider\x1b[0m on a dark horse appears on the road. It seems to have been making loops on the main roads around Hobbiton, most likely searching for \x1b[1;36;40mFrodo\x1b[0m based on his reaction. Laying still and quiet for what seems like forever seems to work very well to avoid the creature, for after a while it seems to give up and rides on again down the road. Many tense minutes pass before the \x1b[1;31;40mRider\x1b[0m moves on and after your party feels safe enough to move again, you decide it's time to distribute weapons in order to prepare for the worst. You're sure this is not the last danger you will enounter. \x1b[1;36;40mFrodo\x1b[0m, who has brought along a bag of weapons for these sorts of situations, offers you the choice of a small two-handed sword or a dagger with a shield. Enter \x1b[1;33;40m'sword'\x1b[0m if you want to choose the \x1b[1;33;40msword\x1b[0m and \x1b[1;33;40m'dagger'\x1b[0m if you'd prefer to use the \x1b[1;33;40mlighter dagger and shield combination\x1b[0m."

      for char in second_steps_town:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

      second_steps_bree = input()

      while True:

        if second_steps_bree == "sword":
        
          print()
          
          bree_sword = "You have chosen the \x1b[1;33;40msmall sword\x1b[0m as a weapon in case of emergencies. Since the sword is relatively large compared to your size and strength, you will be using it as a two-handed sword despite the fact that it's relatively small. You have never wielded a weapon like this before, but how hard can it be?"

          for char in bree_sword:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()

          #assigns the player's choice of weapon to the dictionary for later use

          list_of_choices["weapon choice"] = "hobbit two-handed sword"

          break

        elif second_steps_bree == "dagger":
        
          print()

          hobbit_dagger = "You have chosen the \x1b[1;33;40mdagger\x1b[0m a weapon in case of emergencies. Despite the dagger's small size, it's relatively large as a \x1b[1;35;40m'hobbit'\x1b[0m weapon, which means you will likely be using it more as a very short one-handed sword and will be able to protect yourself with a \x1b[1;33;40msmall Dwarven metal shield\x1b[0m \x1b[1;36;40mFrodo\x1b[0m happens to have. You have never wielded weapons like this before, but how hard can it be?"

          for char in hobbit_dagger:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "hobbit one-handed sword"

          break

        else:

          print()

          oops = "Sorry, that is an incorrect choice. Please choose \x1b[1;33;40m'sword'\x1b[0m or \x1b[1;33;40m'dagger'\x1b[0m."

          for char in oops:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

  elif list_of_choices["race"] == "dwarf":

    if list_of_choices["first steps"] == "forest":
      
      second_steps_mirk = "You and your small party begin your long journey to and through \x1b[1;33;40mMirkwood\x1b[0m. After about fifty miles, you reach the small city known as Lake-Town, which serves as a trading city between the Dwarves of the Lonely Mountain and the \x1b[1;34;40mMen of the Wets\x1b[0m. You decide to stop here to have a good meal and divy up the weapons \x1b[1;37;40mGimli\x1b[0m recieved from his father's armory. You are offered the option of a great \x1b[1;33;40mbattleaxe\x1b[0m or a \x1b[1;33;40mwar pick\x1b[0m, more commonly known as a \x1b[1;33;40mmattock\x1b[0m. Dwarves typically prefer the \x1b[1;33;40mtwo-handed battleaxe\x1b[0m but the \x1b[1;33;40mone-handed mattock\x1b[0m allows for greater protection as one can wield some sort of shield. Please enter \x1b[1;33;40m'axe'\x1b[0m if you would like to use the \x1b[1;33;40maxe\x1b[0m until you reach \x1b[1;37;40mRivendell\x1b[0m, or enter \x1b[1;33;40m'pick'\x1b[0m if you'd prefer the \x1b[1;33;40mone-handed pick and a shield\x1b[0m."

      for char in second_steps_mirk:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

      second_steps_forest = input()

      while True:

        if second_steps_forest == "pick":
          
          print()

          dwarf_pick = "You have made the untraditional to wield the \x1b[1;33;40mone-handed pick and a shield\x1b[0m. You have limited experience in using two weapons instead of one but you are excited for the opportunity to try something different. You'r almost sure it will work out in your favor."

          for char in dwarf_pick:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "dwarven pick"

          break
          
        elif second_steps_forest == "axe":
          
          print()

          dwarf_axe = "You have decided to stick with the traditional \x1b[1;33;40mtwo-handed battleaxe\x1b[0m. You've been trained in the art of axe fighting since you were very young, as is common in most dwarven societies. You like the look of the \x1b[1;33;40mpick\x1b[0m, but aren't ready to branch out just yet."

          for char in dwarf_axe:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "dwarven axe"

          break
      
        else:

          print()

          oops = "Sorry, that is not an option. Please enter either \x1b[1;33;40m'pick'\x1b[0m or \x1b[1;33;40m'axe'\x1b[0m."

          for char in oops:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

    elif list_of_choices["first steps"] == "pass":

      second_steps_mountains = "You and your small party begin your long journey to and over Moria. After about fifty miles, you reach the small city known as Lake-Town, which serves as a trading city between the Dwarves of the Lonely Mountain and the \x1b[1;34;40mMen of the West\x1b[0m. You decide to stop here to have a good meal and divy up the weapons \x1b[1;37;40mGimli\x1b[0m recieved from his father's armory. You are offered the option of a great \x1b[1;33;40mbattleaxe\x1b[0m or a \x1b[1;33;40mwar pick\x1b[0m, more commonly known as a \x1b[1;33;40mmattock\x1b[0m. Dwarves typically prefer the \x1b[1;33;40mtwo-handed battleaxe\x1b[0m but the \x1b[1;33;40mone-handed mattock\x1b[0m allows for greater protection as one can wield some sort of shield. Please enter \x1b[1;33;40m'axe'\x1b[0m if you would like to use the \x1b[1;33;40maxe\x1b[0m until you reach \x1b[1;37;40mRivendell\x1b[0m, or enter \x1b[1;33;40m'pick'\x1b[0m if you'd prefer the \x1b[1;33;40mone-handed pick and a shield\x1b[0m."

      for char in second_steps_mountains:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

      second_steps_forest = input()

      while True:

        if second_steps_forest == "pick":
          
          print()

          dwarf_pick = "You have made the untraditional to wield the \x1b[1;33;40mone-handed pick and a shield\x1b[0m. You have limited experience in using two weapons instead of one but you are excited for the opportunity to try something different. You'r almost sure it will work out in your favor."

          for char in dwarf_pick:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "dwarven pick"

          break
          
        elif second_steps_forest == "axe":
          
          print()

          dwarf_axe = "You have decided to stick with the traditional \x1b[1;33;40mtwo-handed battleaxe\x1b[0m. You've been trained in the art of axe fighting since you were very young, as is common in most dwarven societies. You like the look of the \x1b[1;33;40mpick\x1b[0m, but aren't ready to branch out just yet."

          for char in dwarf_axe:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          print()
          
          #assigns the player's choice of weapon to the dictionary for later use
          
          list_of_choices["weapon choice"] = "dwarven axe"

          break

        else:

          print()

          oops = "Sorry, that is not an option. Please enter either \x1b[1;33;40m'pick'\x1b[0m or \x1b[1;33;40m'axe'\x1b[0m."

          for char in oops:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

def third_steps():
  
  #the player's "third steps": the third part of their  larger journey to Rivendell. 

  #depending on the first and second choice the player made, this decision will lead the player into the next unique choice of the game

  #has an option for an invalid choice in case of an incorrect input

  #this is the first set of choices that involves the addition of character traits to the dictionary of traits in order for character development to occur
  i = 0

  while i == 0:

    if list_of_choices["race"] == "human":
  
      if list_of_choices["first steps"] == "gap":

        print()

        gap_third_step = "After about seventy-five more miles of hard travel, you reach \x1b[1;37;40mEdoras\x1b[0m, the capital city of \x1b[1;37;40mRohan\x1b[0m and dwelling place of the horse-lords. Positioned high up on a hill, it looks a bit more foreboding and less welcoming than you remember from past visits. Perhaps it has something to do with the manned and closed gates. Because it's late and your company desires rest and food, your party approaches the gates to \x1b[1;37;40mEdoras\x1b[0m."

        for char in gap_third_step:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        gap_third_step2 = "'Halt!' You're surprised at the guard's words. You can't remember a time when travelers from \x1b[1;37;40mMinas Tirith\x1b[0m were not welcomed into \x1b[1;37;40mEdoras\x1b[0m almost immediately. The guard continues, and asks you to state your business or peacefully retreat. You're at least a little annoyed at the lack of hospitality, but are unsure if you want to ask for entrance or spend the night outside the walls for the sake of your pride. x1b[1;37;40mCaptain Boromir\x1b[0m, a very proud person, is in favor of forgoing entry to preserve his pride but is wise enough to know that he should not make the decision. He leaves it to you, his second-in-command. Enter \x1b[1;31;40m'yes'\x1b[0m if you would like to give the guard a reason to let you into \x1b[1;37;40mEdoras\x1b[0m or \x1b[1;34;40m'no'\x1b[0m if you would rather not reward his rude behavior."

        for char in gap_third_step2:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        gap_pride_choice = input()

        if gap_pride_choice.lower() == "yes":

          print()

          humility1 = "You humbly explain your errand to the guard: that you are traveling to \x1b[1;37;40mRivendell\x1b[0m on the summons of \x1b[1;36;40mLord Elrond\x1b[0m and are seeking shelter for a few nights, since your party has already traveled a far distance from \x1b[1;37;40mMinas Tirith\x1b[0m and are very tired. The guard seems a little embarassed at his behavior and apologizes. 'The \x1b[1;36;40mLord Théoden, ruler of Rohan\x1b[0m has ordered that all callers at the gate be questioned before entry is granted. You can't be too sure in these dangerous days, you know.' You know that's true, but the sudden lack of hospitality seems fishy to you anyway. You and your small party gain entrance to \x1b[1;37;40mEdoras\x1b[0m due to your prioritization of the greater good over your personal pride."

          print()
        
          for char in humility1:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

            character_traits["humility"] = character_traits["humility"] + 1

            break

        elif gap_pride_choice.lower() == "no":

          print()

          pride1 = "You stay silent and refuse to give the guard a reason why you should be allowed into the city. The nerve of him, honestly! He speaks to x1b[1;37;40m Captain Boromir\x1b[0m, son of Denethor, and the future steward of Gondor! Every man and woman in your party comes from a long line of noble blood. You all deserve better than this treatment. And apparently, the guard seems to realize this too as he recognizes x1b[1;37;40mBoromir\x1b[0m. He seems to realize his mistake, stammeringly apologizing to x1b[1;37;40mBoromir\x1b[0m for his mistake. 'The \x1b[1;36;40mLord Théoden, ruler of Rohan\x1b[0m has ordered that all callers at the gate be questioned before entry is granted. You can't be too sure in these dangerous days, you know, x1b[1;37;40m Captain Boromir\x1b[0m.' You know that's true, but the sudden lack of hospitality seems fishy to you anyway. You and your small party gain entrance to \x1b[1;37;40mEdoras\x1b[0m despite your pride."

          print()
        
          for char in pride1:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          character_traits["pride"] = character_traits["pride"] + 1

        else:

          print()

          oops = "Incorrect choice. Please enter 'yes' if you want to give the guard a reason for your entrance or 'no' if you'd like to prioritize the pride of your party over shelter in \x1b[1;37;40mEdoras\x1b[0m."

          print()

          for char in oops:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          i = i + 1

  while i != 0:

    oops_second_choice = "Please enter 'yes' if you want to give the guard a reason for your entrance or 'no' if you'd like to prioritize the pride of your party over shelter in \x1b[1;37;40mEdoras\x1b[0m."

    for char in oops_second_choice:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()
    
    humility_or_pride_2 = input()
    
    if humility_or_pride_2.lower() == "yes":

          print()

          humility2 = "You humbly explain your errand to the guard: that you are traveling to \x1b[1;37;40mRivendell\x1b[0m on the summons of \x1b[1;36;40mLord Elrond\x1b[0m and are seeking shelter for a few nights, since your party has already traveled a far distance from \x1b[1;37;40mMinas Tirith\x1b[0m and are very tired. The guard seems a little embarassed at his behavior and apologizes. 'The \x1b[1;36;40mLord Théoden, ruler of Rohan\x1b[0m has ordered that all callers at the gate be questioned before entry is granted. You can't be too sure in these dangerous days, you know.' You know that's true, but the sudden lack of hospitality seems fishy to you anyway. You and your small party gain entrance to \x1b[1;37;40mEdoras\x1b[0m due to your prioritization of the greater good over your personal pride."

          print()
        
          for char in humility2:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

            character_traits["humility"] = character_traits["humility"] + 1

            break

    elif humility_or_pride_2.lower() == "no":

          print()

          pride2 = "You stay silent and refuse to give the guard a reason why you should be allowed into the city. The nerve of him, honestly! He speaks to x1b[1;37;40m Captain Boromir\x1b[0m, son of Denethor, and the future steward of Gondor! Every man and woman in your party comes from a long line of noble blood. You all deserve better than this treatment. And apparently, the guard seems to realize this too as he recognizes x1b[1;37;40mBoromir\x1b[0m. He seems to realize his mistake, stammeringly apologizing to x1b[1;37;40mBoromir\x1b[0m for his mistake. 'The \x1b[1;36;40mLord Théoden, ruler of Rohan\x1b[0m has ordered that all callers at the gate be questioned before entry is granted. You can't be too sure in these dangerous days, you know, x1b[1;37;40m Captain Boromir\x1b[0m.' You know that's true, but the sudden lack of hospitality seems fishy to you anyway. You and your small party gain entrance to \x1b[1;37;40mEdoras\x1b[0m despite your pride."

          print()
        
          for char in pride2:

            sleep(0.06)

            sys.stdout.write(char)

            sys.stdout.flush()

          character_traits["pride"] = character_traits["pride"] + 1

    if list_of_choices["first steps"] == "mines":

      print()

      mines_third_step = "After about seventy-five more miles of trek, you reach the Field of Celebrant. Celebrant, which is southeast of Lothlorien, is the site of a historic battle in which the great warrior Eorl the Young of Rohan rode to the aid of Gondor. It's regarded to be a relatively safe place because of its momentous history and also because of its proximity to the protection of Lothlorien. Your party decides to stay the night here in order to have a night of rest and safety."

      for char in mines_third_step:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()
    
      print()

      mines_third_step2 = "You are surprised to see a small legion of riders of Rohan coming up the road behind you. Leading the garrison is a fair-haired warrior that you recognize as x1b[1;37;40mEomer\x1b[0m, nephew \x1b[1;36;40mLord Théoden, ruler of Rohan\x1b[0m. He rides up to your little traveling party as they set up camp and greets x1b[1;37;40mBoromir\x1b[0m warmly, as they have known each other since childhood. Glad as he is to see his old friend, he seems worried about something and goes off to speak with x1b[1;37;40mBoromir\x1b[0m about something in secret. You're slightly curious about what your captain is discussing with x1b[1;37;40mEomer\x1b[0m. Will you give into your sneaky side and listen in on their conversation? Or will you respect your captain's privacy and trust that he'll tell you later on? Enter 'yes' if you want to eavesdrop on their conversation and 'no' if you want to leave it be."

      for char in mines_third_step2:

        sleep(0.06)

        sys.stdout.write(char)

        sys.stdout.flush()

      sneaky_or_loyal1 = input()

      if sneaky_or_loyal1.lower() == "yes":

        print()

        sneaky1 = "You decide that it's important to discover what your captain and x1b[1;37;40mEomer\x1b[0m are discussing. It could be dangerous and knowledge is often the best weapon. You hide behind a large tree and listen in on the two of them. x1b[1;37;40mEomer\x1b[0m sounds very grave as he explains the situation. 'It's with great sadness that I report this news, but I fear that my uncle, \x1b[1;36;40mLord Théoden\x1b[0m, is not himself as of late. His advisor, \x1b[1;31;40mGríma Wormtongue\x1b[0m has been whispering poison into his ear. He does not offer hospitality as is our custom and has begun to send offerings of our best steeds to Mordor. I have ridden without his knowledge to find assistance in Gondor for these grave occurences. x1b[1;37;40mBoromir\x1b[0m looks very worried but remarks that he cannot go himself to the capital city of \x1b[1;37;40mEdoras\x1b[0m at this time because of how far you have already traveled on this road. He offers to send a few of your party back to \x1b[1;37;40mMinas Tirith\x1b[0m to get a larger party to go to \x1b[1;37;40mEdoras\x1b[0m to find out what fishy business is happening. x1b[1;37;40mEomer\x1b[0m gratefully accepts his offer. You retreat to think on these discoveries."

        for char in sneaky1:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        character_traits["sneakiness"] = character_traits["sneakiness"] + 1

      if sneaky_or_loyal.lower() == "no":

        print()

        loyal1 = "You decide to respect your captain's rank and privacy and help your party set up camp while the two finish their discussion. Your captain returns with x1b[1;37;40mEomer\x1b[0m, who has decided to stay the night with your company. AS you hoped, x1b[1;37;40mBoromir\x1b[0m wants to discuss what x1b[1;37;40mEomer\x1b[0m has disclosed with him. x1b[1;37;40mEomer\x1b[0m has apparently been riding without his uncle, \x1b[1;36;40mThéoden's\x1b[0m knowledge because he has been concerned that \x1b[1;36;40mThéoden\x1b[0m has not been himself of late. x1b[1;37;40mEomer\x1b[0m suspects it has something to do with his sinister advisor \x1b[1;31;40mGríma Wormtongue\x1b[0m, who has apparently been whispering poison into his ear. \x1b[1;36;40mThéoden\x1b[0m has reportedly stopped offering hospitality in Rohirrim custom and has begun to send offerings of their best steeds to Mordor. x1b[1;37;40mBoromir\x1b[0m tells you that though he is concerned about these events, he cannot go himself to help because of how far he has led the party to \x1b[1;37;40mRivendell\x1b[0m. He has offered to send a small party back to \x1b[1;37;40mMinas Tirith\x1b[0m to get a larger party to go to \x1b[1;37;40mEdoras\x1b[0m to find out what fishy business is happening. x1b[1;37;40mEomer\x1b[0m has gratefully accepted his offer. You agree with x1b[1;37;40mBoromir\x1b[0m that this is concerning news. You hope everything is resolved."

        for char in loyal1:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        character_traits["loyalty"] = character_traits["loyalty"] + 1
      
      else:

        oops = "That is an invalid response."

        for char in oops:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()

        i = i + 1

  while i != 0:
    
    second_chance = "Enter 'yes' if you want to eavesdrop on their conversation and 'no' if you want to leave it be."

    for char in second_chance:

          sleep(0.06)

          sys.stdout.write(char)

          sys.stdout.flush()
    
    second_chance1 = input


  if list_of_choices["race"] == "dwarf":

  
    #Mirkwood route. This step is Elvenking's Halls!
    #Moria route. This step is the old forest route! OOh.
  
  if list_of_choices["race"] == "hobbit":

    #both routes lead to Bree. So you're at Bree now! Hooray. This isn't the option where you get to meet Aragorn :(. That's the next one.


def play_game():

    greet_user()

    choose_gender()

    info_about_race()

    choose_race()

    choose_name()

    origin_place()

    direction_choice()

    first_steps()

    second_steps()

    third_steps()

play_game()
