import random
import os

class SecretSantaService:
    """
    INIT
    """
    def __init__(self, conn):
        # set connection
        self.conn = conn

        # load givers
        self.givers = self.load_givers()

        print('members from db: ')
        print(self.givers)

        # Seed random generator
        self.random_gen = random
        self.random_gen.seed()

    """
    LOAD GIVERS
    """
    def load_givers(self):
        cur = self.conn.cursor()
        cur.execute('select * from santas;')
        return cur.fetchall()
        
    """
    GET RECEIVER FROM CODE
    """
    def get_receiver_from_code(self, code):
        # get santa from code
        santa = self.get_santa_from_code(code)
        print("santa: " + santa)
        # from santa get match (from txt or make match)
        return self.determine_match(santa)

    """
    GET SANTA FROM CODE
    """
    def get_santa_from_code(self, code):

        upper_code = code.upper()
        cur = self.conn.cursor()
        cur.execute("select name from santas where code = %s", (upper_code,))
        row = cur.fetchone()
        giver = row[0]
        print(f'giver: {giver}')
        return giver

    '''
    DERTERMINE MATCH
    '''
    def determine_match(self, member):
        print('called determine_match()')
        cur = self.conn.cursor()
        cur.execute('select ')

    '''
    PICK RANDOM
    '''
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
        self.save_match(santa, picked)
        return picked

    '''
    SAVE MATCH
    '''
    def save_match(self, santa, picked):
        # save the match giver_receiver table
        print('called save_match()')


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
