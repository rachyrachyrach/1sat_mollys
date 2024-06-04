import requests
import json
import logging
from bsvlib import PrivateKey, Tx, Script

# Configuration
GORILLA_POOL_API_URL = 'https://ordinals.gorillapool.io/api/tx/submit'

# Set up logging
logging.basicConfig(level=logging.INFO)

def inscribe(base64_data, mime_type, app_name, data_name, destination_address, private_key_wif, utxo):
    try:
        logging.info(f"Preparing UTXO: {utxo}")

    # Initialize the private key using WIF (Wallet Import Format)
    private_key = PrivateKey.from_wif(private_key_wif)

# Create the inscription object following the ordinals envelope format
inscription = {
    "base64Data": base64_data,
    "mimeType": mime_type,
    "map": {
        "app": app_name,
        "type": "ord",
        "name": data_name
        }
        }
logging.info(f"Inscription created: {inscription}")

# Create a new transaction object
tx = Tx()

# Add an input to the transaction using the UTXO data
tx.add_input(
    prev_txid=utxo['txid'], # Transaction ID of the UTXO
    prev_index=utxo['vout'], # Output index of the UTXO
    prev_satoshis=utxo['satoshis'], # Amount of satoshis in the UTXO
    script_pubkey=Script.from_hex(utxo['script']) # ScriptPubKey of the UTXO
    )

# Add the output with OP_RETURN data (this includes the inscription)
op_return_script = Script.p2pkh_from_address(destination_address) + Script.op_return(inscription)
tx.add_output(op_return_script, 1) # 1 satoshi for the OP_RETURN output

logging.info(f"Transaction created: {tx.to_dict()}")

# Sign the transaction with the private key
tx.sign(private_key)
logging.info(f"Transaction signed")

# Serialize the transaction to raw hex format for broadcasting
raw_tx_hex = tx.serialize()

# Broadcast the transaction to the Gorilla Pool API
headers = {
    'Content-Type': 'application/json'
    }
response = requests.post(GORILLA_POOL_API_URL, headers=headers, data=json.dumps({"rawtx": raw_tx_hex}))
response_data = response.json()
logging.info(f"Gorilla Pool API response: {response_data}")

# Check if the transaction was successfully broadcasted
if response.status_code == 200 and response_data.get('txid'):
    logging.info(f'Success: Transaction ID: {response_data["txid"]}')
    return {'success': True, 'txid': response_data['txid']}
else:
    logging.error(f'Error: {response_data.get("message", "Unknown error")}')
    return {'success': False, 'error': response_data.get('message', 'Unknown error')}

except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {str(e)}")
        return {'success': False, 'error': f"Network error: {str(e)}"}
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {'success': False, 'error': str(e)}

if __name__ == '__main__':
    # Example inputs
    base64_data = "your_base64_data"
    mime_type = "your_mime_type"
    app_name = "your_app_name"
    data_name = "your_data_name"
    destination_address = "your_destination_address"
    private_key_wif = "your_private_key_wif"
    utxo = {
        'txid': 'your_utxo_txid',
        'vout': 0,
        'satoshis': 1000,
        'script': 'your_utxo_script'
    }

result = inscribe(base64_data, mime_type, app_name, data_name, destination_address, private_key_wif, utxo)
    print(result)