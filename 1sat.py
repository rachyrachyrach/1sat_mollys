from bitsv import Key
from os import environ

my_key = Key(environ["BSV_KEY"])
list_of_pushdata = [
    bytes.fromhex('6d01'), # encode hex to bytes
    'New_Name'.encode('utf-8')]  # encode string to utf-8 encoded bytes]

my_key.send(
    outputs = [],
    message = list_of_pushdata,
    custom_pushdata = True)

#This prints out Public key to test
print(my_key.address)

#This shows what is in wallet
print(my_key.get_unspents())

