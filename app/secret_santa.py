import random
from os import path

class SecretSanta:
    def __init__(self):
        # Load the members to pick 
        self.members_to_pick = self.load_members()
        print('Members from init:')
        self.print_members()
        # Load the picked members
        self.picked_members = []
        self.random_gen = random
        self.random_gen.seed()

    def pick_random(self):
        length = len(self.members_to_pick)

        if length == 0:
            print('There are no more people!')
            exit(0)

        index = self.random_gen.randint(0, length - 1)
        picked = self.members_to_pick[index]

        # Remove from file
        self.members_to_pick.remove(picked)
        return picked

    def remove_member(self, index):
        # Removed from file
        del self.members_to_pick[index]

    def print_members(self):
        for member in self.members_to_pick:
            print('   ' + member)

    def load_members(self):
        # check for the file
        if not path.exists("members.txt"):
            f = open("members.txt", 'w')
            f.write('Mom\n'  \
                    'Dad\n' \
                    'Spencer\n' \
                    'Preston\n' \
                    'Christena')
            f.close()
            return ['Mom', 'Dad', 'Spencer', 'Preston', 'Christena']
        else:
            f = open("members.txt", 'r')
            return f.read().splitlines()
         

''' 
RUN CODE
    For testing the sercret santa code
'''
def run_code():
    user_input = 'bloop'
    ss = SecretSanta()

    while user_input != 'q':
        user_input = input('Press enter to pick:')
        print( '\n*********************  \
               \nThe winner is: ' + ss.pick_random())
        ss.print_members()

run_code()
