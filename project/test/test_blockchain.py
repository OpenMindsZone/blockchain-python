""" Tests for Blockchain structures """
import json

from project.source.main import Blockchain, mine_block


class TestBlockchain:
    def test_create_block(self):
        blockchain = Blockchain()
        assert isinstance(blockchain, Blockchain)

        result = mine_block(blockchain)

        # Blockchain should be empty
        assert result['index'] == 2

