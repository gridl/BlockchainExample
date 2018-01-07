import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):

    def proof_of_workf(self, last_proof):
        """
        Simple proof of work algorithm:
        - Find a number 'p' such as hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof

        :param last_proof:
        :return:
        """

        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            print(last_proof)
            print(proof)
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeros?
        :param last_proof:
        :param proof:
        :return: <bool> True if connet, False f not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


