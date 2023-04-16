""" Sample Blockchain P.O.C. """
import datetime
import hashlib
import json

# Consts
DIFFICULTY_LEVEL = 3
DIFFICULTY_TOKEN = "0" * DIFFICULTY_LEVEL


class Block:
    def __init__(self, index, block_data=None, previous_hash=None):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.block_data = block_data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.mine_block()

    def calculate_hash(self):
        return str(
            hashlib.sha256(
                f"{self.index}{str(self.timestamp)}{self.previous_hash}{json.dumps(self.block_data)}{self.nonce}".encode()
            ).hexdigest()
        )

    def mine_block(self):
        """Proof of work"""
        while self.hash[:DIFFICULTY_LEVEL] != DIFFICULTY_TOKEN:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        # self.create_block(proof=1, previous_hash=None)

    def create_genesis_block(self):
        return Block(
            index=0,
            block_data={"data": "Genesis block"},
            previous_hash=0,
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data=None) -> None:
        latest_block = self.get_latest_block()

        block = Block(
            index=latest_block.index + 1,
            block_data=data,
            previous_hash=latest_block.hash,
        )

        self.chain.append(block)

    def get_previous_block(self):
        return self.chain[-1]


def chain_is_valid(chain) -> bool:
    previous_block = chain[0]
    block_index = 1

    while block_index < len(chain):
        block = chain[block_index]
        if block.previous_hash != Block.calculate_hash(previous_block):
            return False

        if Block.calculate_hash(block) != block.hash:
            return False
        previous_block = block
        block_index += 1

    return True


def print_blockchain(blockchain):
    for block in blockchain.chain:
        print(json.dumps(block.__dict__, indent=4))
    print("-" * 16)


def main():
    """Entry point"""

    blockchain = Blockchain()

    for n in range(4):
        data = {"field1": f"Sample data - {n}"}
        blockchain.add_block(data=data)

    print_blockchain(blockchain)
    print(f"Blockchain is valid: {chain_is_valid(blockchain.chain)}")


if __name__ == "__main__":
    main()
