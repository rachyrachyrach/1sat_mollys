from bitsv import Key
from os import environ
from op import OP

my_key = Key(environ["BSV_KEY"])
hex_of_key = my_key.to_hex()

list_of_pushdata = [
    OP.OP_DUP, OP.OP_HASH160, bytes.fromhex(hex_of_key), OP.OP_EQUALVERIFY, OP.OP_CHECKSIG,
    OP.OP_FALSE, OP.OP_IF, bytes.fromhex(0x6f7264), OP.OP_1,
    "text/plain".encode("utf-8"), OP.OP_0, "Mollys are coming".encode("utf-8"), OP.OP_ENDIF
    ]  # encode string to utf-8 encoded bytes]

txid = my_key.send(
    outputs = [],
    message = list_of_pushdata,
    custom_pushdata = True)

#This prints out Public key to test
print(my_key.address)

#This shows what is in wallet
print(my_key.get_unspents())

#Used to see the txid
print(txid)