#MadFrozenLibsForTookie

#Get Tookie's inputs

name_1 = input("Hello there! Please enter a name:  ")
animal_sound_1 = input("Please give me your favorite animal sound:  ")
name_2 = input("Can you let me know what your teacher's name is?  " )
verb_1 = input("Can you name a verb like running, flying, dancing?  ") 
animal_sound_2 = input("Finally can you give me another animal sound?  ")


# input what we want our story to say after Tookie inputs data

print("\nOkay here we go!")

print("\nMy name is {} and I love the movie Frozen.".format(name_1.title()))
print("Whenever I hear someone mention Frozen I start {}ing!".format(animal_sound_1.lower()))
print("When I tell my teacher {} how much I love Frozen they also get excited.".format(name_2.title()))
print("One time the teacher started {} during class because I said it's time to watch Frozen.".format(verb_1.lower()))  
print("I think instead of singing the songs we should all {} to them.".format(animal_sound_2.lower()))