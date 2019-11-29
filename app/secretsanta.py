import random
import os

class SecretSantaService:
    def __init__(self, conn):
        # Load the members to pick 
        self.members_to_pick = self.load_members()
        print('Members from init:')
        self.print_members()
        # Load the picked members
        
        # Connect to DB
        self.conn = conn

        self.random_gen = random
        self.random_gen.seed()

    def get_santaee_from_code(self, code):
        # get santa from code
        santa = self.get_santa_from_code(code)
        print("santa: " + santa)
        # from santa get match (from txt or make match)
        return self.determine_match(santa)

    def get_santa_from_code(self, code):
        print("getting santa with code: " + code)
        f = open("app/data/passcodes.txt", "r")
        passcodes = f.read().splitlines()
        for pass_str in passcodes:
            code_pair = pass_str.split(',')
            print(f'code pair: {code_pair[0]} -> {code_pair[1]}')
            if code_pair[0].upper() == code.upper():
                print("returning santa: " + code_pair[1])
                return code_pair[1].strip()
        return Exception("Could not match code")

    def determine_match(self, member):
        f = open("app/data/matches.txt", "r")
        match_lines = f.read().splitlines()
        f.close()
        if not match_lines:
            print("not matched lines")
            return self.pick_random(member)
        else:
            for line in match_lines:
                if line.split(',')[0].upper() == member.upper():
                    print("found match: " + line.split(',')[1])
                    return line.split(',')[1] 
            return self.pick_random(member)

    def pick_random(self, santa):
        length = len(self.members_to_pick)

        if length == 0:
            print('There are no more people!')
            return Exception("There are no more santas")

        picked = None

        while (picked == None or picked == santa):
            index = self.random_gen.randint(0, length - 1)
            picked = self.members_to_pick[index]
        
        print("picked member: " + picked)

        # Remove from file
        self.members_to_pick.remove(picked)
        self.write_members(self.members_to_pick)

        # Add the santa to santa-matches
        self.write_match(santa, picked)
        return picked

    def write_members(self, members):
        f = open("app/data/santaees_left.txt", "w")
        for member in members:
            f.write(f'{member}\n')

    def write_match(self, santa, picked):
        # save the match to the matches text
        print("wrtting to matches")
        f = open("app/data/matches.txt", "a")
        f.write(f'{santa},{picked}\n')
        f.close()    

    def print_members(self):
        for member in self.members_to_pick:
            print('   ' + member)

    def load_members(self):
        # check for the file
        print(f'==================== {os.getcwd()}')
        if not os.path.exists("app/data/santaees_left.txt"):
            f = open("app/data/santaees_left.txt", 'w+')
            f.write('Mom\n'  \
                    'Dad\n' \
                    'Spencer\n' \
                    'Jenny\n'  \
                    'Preston\n' \
                    'Christena')
            f.close()
            return ['Mom', 'Dad', 'Spencer', 'Jenny', 'Preston', 'Christena']
        else:
            f = open("app/data/santaees_left.txt", 'r')
            return f.read().splitlines()
         

''' 
RUN CODE
    For testing the sercret santa code
'''
# def run_code():
#     user_input = 'bloop'
#     ss = SecretSantaService()

#     while user_input != 'q':
#         user_input = input('Press enter to pick:')
#         print( '\n*********************  \
#                \nThe winner is: ' + ss.pick_random())
#         ss.print_members()

# run_code()
