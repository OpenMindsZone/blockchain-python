""" Tests for Blockchain structures """
import json

from project.source.main import Blockchain, chain_is_valid


class TestBlockchain:
    def test_create_block(self):
        blockchain = Blockchain()
        assert isinstance(blockchain, Blockchain)
        # Blockchain should be empty
        assert len(blockchain.chain) == 1

        blockchain.add_block(data={'data': 'content_1'})
        blockchain.add_block(data={'data': 'content_2'})

        assert len(blockchain.chain) == 3
        assert chain_is_valid(blockchain.chain) is True

