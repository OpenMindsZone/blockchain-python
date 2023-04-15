""" Sample Blockchain P.O.C. """
import datetime
import hashlib
import json

# Consts
DIFFICULTY_LEVEL = 5
DIFFICULTY_TOKEN = "0" * DIFFICULTY_LEVEL


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash=None)

    def create_block(self, proof, previous_hash) -> dict:
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "data": {
                "data_file_one": None,
                "data_file_two": None,
                "data_file_three": None,
            },
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)

        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:DIFFICULTY_LEVEL] == DIFFICULTY_TOKEN:
                check_proof = True
            else:
                check_proof += 1

        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False

            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:DIFFICULTY_LEVEL] != DIFFICULTY_TOKEN:
                return False
            previous_block = block
            block_index += 1


def mine_block(blockchain):
    # Mining a new block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        "message": "A block is MINED",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }

    return response


def main():
    """Entry point"""
    blockchain = Blockchain()
    result = mine_block(blockchain)
    print(json.dumps(blockchain.chain, indent=4))


if __name__ == "__main__":
    main()
