from bitsv import Key
from os import environ
from op import OP

my_key = Key(environ["BSV_KEY"]) # export BSV_KEY="Your private key"
hex_of_key = my_key.to_hex()

list_of_pushdata = [
    OP.OP_IF.value, bytes.fromhex("6f7264"), OP.OP_DUP.value, OP.OP_HASH160.value, bytes.fromhex(hex_of_key), OP.OP_EQUALVERIFY.value, OP.OP_CHECKSIG.value,
    OP.OP_FALSE.value, OP.OP_1.value,
    "text/plain".encode("utf-8"), OP.OP_0.value, "Mollys are coming".encode("utf-8"), OP.OP_ENDIF.value
    ]  # encode string to utf-8 encoded bytes]

for pd in list_of_pushdata: #pd means pushdata
    print(type(pd))

#list_of_pushdata = [
#    OP.OP_DUP.value, OP.OP_HASH160.value, bytes.fromhex(hex_of_key), OP.OP_EQUALVERIFY.value, OP.#OP_CHECKSIG.value, bytes.fromhex("6f7264"), OP.OP_1.value,
#    "text/plain".encode("utf-8"), OP.OP_0.value, "Mollys are coming".encode("utf-8"), OP.OP_ENDIF.value
#    ]  # encode string to utf-8 encoded bytes]

for x in list_of_pushdata:
    print(type(x))

#This shows what is in wallet
#print(my_key.get_unspents())

txid = my_key.send(
    outputs = [],
    message = list_of_pushdata)
    #custom_pushdata = True)
    #list_of_pushdata = list_of_pushdata)

#This prints out Public key to test
print(my_key.address)

#Used to see the txid
print(txid)