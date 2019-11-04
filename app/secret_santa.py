import random

class SecretSanta:
    def __init__(self):
        # Load the members to pick 
        self.members_to_pick = [
            'Mom',
            'Dad',
            'Spencer',
            'Jenny',
            'Preston',
            'Christena',
        ]
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
        print('\nRemianing Members:')
        for member in self.members_to_pick:
            print('   ' + member)

'''

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
