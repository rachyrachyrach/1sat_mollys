from bitsv import Key
from os import environ

# Replace with your private key
private_key = os.environ.get('PRIVATE_KEY') #My YoursWallet 1PXxMeP14C1A73y8Lf8DNT2o5EWGftGDUV
ord_private_key = os.environ.get('ORDINALS_PRIVATE_KEY')
key = Key(private_key)

# Replace with the recipient's address
recipient_address = '1F4aHxZMgKDVFneo34PmtNwRnB4dPzoKhR' #My HandCash address
amount = 1000  # Amount in satoshis (1 BSV = 100,000,000 satoshis)

# Create a transaction with OP_RETURN
outputs = [
    (recipient_address, amount, 'satoshi'),  # Regular output
    ('hello', 0, 'op_return')                # OP_RETURN output
]

# Send the transaction
tx_hash = key.send(outputs)
print(f'Transaction sent. TXID: {tx_hash}')
