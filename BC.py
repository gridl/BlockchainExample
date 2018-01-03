
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    #create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
        Creates new block in the blockchain

        :param proof: <int> THe proof given by the Proof of work algorithm
        :param previous_hash: (optional) <str> Hash of previous block
        :return: <dict> New Block

         """
        block = {

            'index': len(self.chain) +1
            'timestamp': time()
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1])

        }

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        # creates a new transaction to go into the next mined block

        """
        :param sender: <str> Address of the sender
        :param recepient: <str> Address of the recepient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction

        """

        self.current_transactions.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount

        })
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last BLock in the chain

        # block = {
        #     'index': 1,
        #     'timestamp': 1506057125.900785,
        #     'transactions': [
        #         {
        #             'sender': "8527147fe1f5426f9dd545de4b27ee00",
        #             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
        #             'amount': 5,
        #         }
        #     ],
        #     'proof': 324984774000,
        #     'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        # }

