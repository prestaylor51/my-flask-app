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
        cur.execute('select * from givers;')
        return cur.fetchall()
        
    """
    GET RECEIVER FROM CODE
    """
    def get_receiver_from_code(self, code):
        # get santa from code
        giver = self.get_giver_from_code(code)
        print("santa: " + giver[2])
        # from santa get match (from txt or make match)
        return self.determine_match(giver)

    """
    GET SANTA FROM CODE
    """
    def get_giver_from_code(self, code):

        upper_code = code.upper()
        cur = self.conn.cursor()
        cur.execute("select * from givers where code = %s", (upper_code,))
        row = cur.fetchone()
        giver = row[0]
        print(f'giver: {giver}')
        return giver

    '''
    DERTERMINE MATCH
    '''
    def determine_match(self, giver):
        print('called determine_match()')
        cur = self.conn.cursor()
        cur.execute('select gr.receiver_id from giver_receiver gr \
                    join givers g on gr.giver_id = g.id  \
                    where g.name = %s;',(giver.upper(),))
        row = cur.fetchone()
        if row != None:
            print(self.get_giver_by_id(row[0]))
        else: print('giver has no receiver')

    def get_giver_by_id(self, id):
        for giver in self.givers:
            if giver[0] == id:
                return giver

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
