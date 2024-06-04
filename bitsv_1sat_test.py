from bitsv import Key, script
import os

# Generate a new private key (use your own private key here)
private_key = os.environ.get('PRIVATE_KEY') # export PRIVATE_KEY="Your private key"
my_key = Key('private_key')

# Create the inscription script for "hello"
inscription_script = script.Script(
    [script.OP_FALSE, script.OP_IF,
     b'ord', script.OP_1, b'text/plain', script.OP_0, b'hello',
     script.OP_ENDIF]
)

# Get a UTXO to spend (replace with a real UTXO from your address)
utxo = {
    'txid': '829c4cc446e6212f0fe15b548a645b061da0fc89bd505a05bf0e7f59e7d4baa4',
    'output': 0,
    'satoshis': 1000,
}

# Create the P2PKH locking script for the recipient
recipient_address = '18jGFfSb32rBAPvkHdabBHCTsNCKwxTm1Y'
p2pkh_script = script.create_p2pkh(recipient_address)

# Create the transaction
tx = my_key.create_transaction(
    [(recipient_address, 999, 'satoshi')],
    leftover=my_key.address,
    custom_pushdata=inscription_script
)

# Broadcast the transaction
my_key.send([utxo], [p2pkh_script, inscription_script])
