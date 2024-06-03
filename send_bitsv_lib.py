from bitsv import Key
import os

client_address = os.environ.get('CLIENT_ADDRESS')# insert the wallet address you're sending money to. client id by export CLIENT_ADDRESS local file To my HandCash wallet
client_private_key = os.environ.get('CLIENT_PRIVATE_KEY')# insert your wallet's private key by using export CLIENT_PRIVATE_KEY local file From my YoursWallet

network = 'main' #'test' for Testnet, 'stn' for scaling testnet. 'main' for mainnet.

my_key_test = Key(client_private_key, network=network) #private key
my_key_test.get_balance()

print(my_key_test.get_unspents())
# Can include a long list of tuples as outputs
outputs = [
    (client_address, 1, 'satoshi'),
    ('hello', 0, 'op_return')
    ]

my_key_test.send(outputs)
