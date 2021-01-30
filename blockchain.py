def lighting_hash(data):
	return data+ '*'

class Block:
	def __init__(self,data,hash,last_hash):
		self.data = data
		self.hash = hash
		self.last_hash = last_hash

# foo_block = Block('foo_data','foo_hash','foo_last_hash')		
# print(foo_block.data)
# print(foo_block.hash)
# print(foo_block.last_hash)

class blockchain:
	def __init__(self):
		genesis = Block('gen_data','gen_hash','gen_last_hash')
		self.chain=[genesis]

	def add_block(self,data):
		last_hash = self.chain[-1].hash
		hash = lighting_hash(data + last_hash)
		block = Block(data,hash,last_hash)

		self.chain.append(block)

foo_blockchain = blockchain()
foo_blockchain.add_block('satu')
foo_blockchain.add_block('dua')
foo_blockchain.add_block('tiga')

for block in foo_blockchain.chain:
	print(block.__dict__)

