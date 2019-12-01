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
        givers = cur.fetchall()
        cur.close()
        return givers
        
    """
    GET RECEIVER FROM CODE
    """
    def get_receiver_from_code(self, code):
        # get santa from code
        giver = self.get_giver_from_code(code)
        print(giver)
        print(f'santa: {giver[2]}')
        # from santa get match (from txt or make match)
        return self.determine_match(giver)

    """
    GET SANTA FROM CODE
    """
    def get_giver_from_code(self, code):

        upper_code = code.upper()
        cur = self.conn.cursor()
        cur.execute("select * from givers where code = %s", (upper_code,))
        giver = cur.fetchone()
        cur.close()
        print(f'giver: {giver[2]}')
        return giver

    '''
    DERTERMINE MATCH
    '''
    def determine_match(self, giver):
        print('called determine_match()')
        cur = self.conn.cursor()

        # get the match if exists
        cur.execute('select gr.* from givers g \
                    join giver_receiver gr on gr.giver_id = g.id \
                    where g.id = %s;',(giver[0],))
        row = cur.fetchone()
        cur.close()

        if row != None:
            print('giver has receiver already')
            receiver = self.get_giver_by_id(row[1])
            print(receiver)
            return receiver[2]
        else: 
            # if no match for giver then create one
            print('giver has no receiver')
            return self.select_match_for_giver(giver)

    # returns name of selected receiver
    # use rowcount
    def select_match_for_giver(self, giver):
        cur = self.conn.cursor()
        cur.execute('select g.id from givers g \
                    where g.id not in (select receiver_id from giver_receiver);')
        size = cur.rowcount
        print(f'size: {size}')
        rows = cur.fetchall()
        cur.close()
        print(f'rows: {rows}')
        ran_index = self.random_gen.randint(0,size - 1)
        receiver_id = rows[ran_index][0]
        print(f'index: {ran_index}')
        print(f'row: {rows[ran_index]}')

        # write giver_receiver row for giver and id
        print(f'new receiver id: {receiver_id}')
        self.save_giver_receiver(giver[0], receiver_id)
        return self.get_giver_by_id(receiver_id)[2]

    def save_giver_receiver(self, giver_id, receiver_id):
        cur = self.conn.cursor()
        cur.execute('insert into giver_receiver values (%s, %s);',(giver_id, receiver_id,))
        self.conn.commit()
        cur.close()

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
