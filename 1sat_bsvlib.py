import base58
import hashlib
from bsvlib import PrivateKey, script as bsv_script
from os import environ

def wif_to_hex(wif: str) -> str:
    # Decode WIF to bytes
    decoded = base58.b58decode_check(wif)
    # Drop the first byte (version byte) and the last byte (compression flag or checksum)
    private_key_bytes = decoded[1:-1]
    # Convert to hex string
    return private_key_bytes.hex()

def hash160(data: bytes) -> bytes:
    sha256 = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    return ripemd160.digest()

# Load the private key from the environment variable
bsv_key_wif = environ.get("BSV_KEY_WIF")  # export BSV_KEY_WIF="Your private key in WIF format"
print(f"BSV_KEY_WIF: {bsv_key_wif}")  # Debugging line to print the BSV_KEY_WIF

if not bsv_key_wif:
    raise ValueError("BSV_KEY_WIF environment variable is not set.")

try:
    # Convert WIF to hex
    private_key_hex = wif_to_hex(bsv_key_wif)
    my_key = PrivateKey.from_hex(private_key_hex)
except ValueError as e:
    raise ValueError(f"Invalid BSV_KEY_WIF value: {e}")

# Get the public key and compute its hash160
public_key_bytes = my_key.pubkey.serialize()
public_key_hash160 = hash160(public_key_bytes).hex()

# Construct the list of pushdata using bsvlib
list_of_pushdata = [
    "OP_IF", "6f7264", "OP_DUP", "OP_HASH160", public_key_hash160, "OP_EQUALVERIFY", "OP_CHECKSIG",
    "OP_FALSE", "OP_1",
    "text/plain", "OP_0", "Mollys are coming", "OP_ENDIF"
]

# Print types of elements in the pushdata list
for pd in list_of_pushdata:
    print(type(pd))

# Create a script from the list of pushdata
script = bsv_script.Script(list_of_pushdata)

# Create a transaction with the script as the message
tx = my_key.create_transaction(outputs=[], script=script)

# Sign and broadcast the transaction
txid = my_key.sign_and_broadcast(tx)

# Print the public key address
print(my_key.address)

# Print the transaction ID
print(txid)
