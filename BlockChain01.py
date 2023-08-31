
#tushar kalaskar
#small blockchain using python

import hashlib

def hashGenrator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class BlockChain:
    def __init__(self):
        hashlast=hashGenrator('genrate_last')
        hashstart=hashGenrator('genrate_start')

        genesis=Block('i am tushar,from amravati',hashstart,hashlast)
        self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenrator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)


bc=BlockChain()
bc.add_block('001')
bc.add_block('002')
bc.add_block('003')
bc.add_block('004')
bc.add_block('005')
bc.add_block('006')
bc.add_block('007')
bc.add_block('008')
bc.add_block('009')
bc.add_block('010')
bc.add_block('011')
bc.add_block('012')
bc.add_block('013')
bc.add_block('014')
bc.add_block('015')
bc.add_block('016')
bc.add_block('017')
bc.add_block('hi here is last block')

for block in bc.chain:
    print(block.__dict__)





