# This is a placeholder. Use the appropriate library for Bitcoin SV in Python.
import bsvlib
from base64 import b64decode

class Utxo:
    def __init__(self, satoshis, txid, script, vout):
        self.satoshis = satoshis
        self.txid = txid
        self.script = script
        self.vout = vout

def create_ordinal(utxo, ordinal_destination_address, payment_pk, change_address, sat_per_byte_fee, inscription):
    
    ###Create a transaction to inscribe an ordinal.
    
    ###Parameters:
    ###- utxo: Utxo object
    ###- ordinal_destination_address: str
    ###- payment_pk: PrivateKey object
    ###- change_address: str
    ###- sat_per_byte_fee: int
    ###- inscription: dict with keys 'dataB64' and 'contentType'
    
    ###Returns:
    ###- Transaction object

    # Decode the base64 inscription data
    data = b64decode(inscription['dataB64'])
    
    # Create a new transaction
    tx = bsv.Transaction()
    
    # Add the input from the UTXO
    tx.add_input(utxo.txid, utxo.vout, utxo.script, utxo.satoshis)
    
    # Add the output for the ordinal
    tx.add_output(ordinal_destination_address, 1, data)
    
    # Add the change output
    tx.add_output(change_address, utxo.satoshis - 1 - (len(data) * sat_per_byte_fee))
    
    # Sign the transaction
    tx.sign(payment_pk)
    
    return tx

def send_ordinal(utxo, ordinal, payment_pk, change_address, sat_per_byte_fee, ord_pk, ord_destination_address):
    """
    Send an ordinal to a destination address.
    
    Parameters:
    - utxo: Utxo object
    - ordinal: Utxo object
    - payment_pk: PrivateKey object
    - change_address: str
    - sat_per_byte_fee: int
    - ord_pk: PrivateKey object
    - ord_destination_address: str
    
    Returns:
    - Transaction object
    """
    # Create a new transaction
    tx = bsv.Transaction()
    
    # Add the input from the UTXO
    tx.add_input(utxo.txid, utxo.vout, utxo.script, utxo.satoshis)
    
    # Add the input for the ordinal
    tx.add_input(ordinal.txid, ordinal.vout, ordinal.script, ordinal.satoshis)
    
    # Add the output for the ordinal destination
    tx.add_output(ord_destination_address, 1)
    
    # Add the change output
    tx.add_output(change_address, utxo.satoshis + ordinal.satoshis - 1 - (len(ordinal.script) * sat_per_byte_fee))
    
    # Sign the transaction
    tx.sign(payment_pk)
    tx.sign(ord_pk)
    
    return tx

def send_utxos(utxos, payment_pk, address, fee_sats):
    """
    Send all UTXOs to a destination address.
    
    Parameters:
    - utxos: list of Utxo objects
    - payment_pk: PrivateKey object
    - address: str
    - fee_sats: int
    
    Returns:
    - Transaction object
    """
    # Create a new transaction
    tx = bsv.Transaction()
    
    total_satoshis = 0
    
    # Add all inputs
    for utxo in utxos:
        tx.add_input(utxo.txid, utxo.vout, utxo.script, utxo.satoshis)
        total_satoshis += utxo.satoshis
    
    # Add the output for the destination address
    tx.add_output(address, total_satoshis - fee_sats)
    
    # Sign the transaction
    tx.sign(payment_pk)
    
    return tx
