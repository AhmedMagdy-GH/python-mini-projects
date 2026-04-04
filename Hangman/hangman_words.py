import random
animals = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white"]

fruits=['apple', 'banana', 'mango', 'orange', 'grape', 'watermelon', 'strawberry', 'kiwi']

chosen_cat=[animals, colors, fruits]

word_list= random.choice(chosen_cat)

