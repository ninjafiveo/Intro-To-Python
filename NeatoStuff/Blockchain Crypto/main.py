import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="First Block", proof=100)


    def new_block(self, proof, previous_hash=None):
    	# Here we can verify the proof value, but since this is basics, we'll not do that.
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # we reset the transactions to be included in the new block
        self.pending_transactions = []
        # add the block to the chain
        self.chain.append(block)

        return block

	
    # quick function to give us the last block on the chain
    @property
    def last_block(self):
        return self.chain[-1]


    def new_transaction(self, sender, recipient, amount):
    	# we get the details here and append them to self.pending_transactions
    	# it'll wait to be included in a block
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1


    def hash(self, block):
    	# we use SHA256 here, same as most other cryptos
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
# 								SENDER | RECIPIENT | HOW MUCH / WHATS SENT
t1 = blockchain.new_transaction("moe", "mr sekol", '999999999 BTC')
t2 = blockchain.new_transaction("idk", "Satoshi", 'fbi agent')
blockchain.new_block(12345)

t5 = blockchain.new_transaction("person x", "moe", '0.5 BTC')
t6 = blockchain.new_transaction("im not very creative with these names", "Mike", '2 BTC')
blockchain.new_block(6789)

with open(".\\output.json", "w") as f:
	json.dump(blockchain.chain, f, indent=4)
	f.close()