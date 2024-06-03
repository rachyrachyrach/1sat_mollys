def init_provider():
        # Replace with actual provider initialization
        return "your_wallet_provider_token"


# Create inscription data
inscriptions = [
        {
                "address": "14kwyqNF7Ed5N1cXchroSjjxSASDrPksGA",
                "base64Data": base64.b64encode("Panda is awesome!".encode()).decode(),
                "mimeType": "text/plain",
                "map": {"app": "Cool app name", "type": "ord", "name": "Text #1"},
                },
        {
                "address": "14kwyqNF7Ed5N1cXchroSjjxSASDrPksGA",
                "base64Data": base64.b64encode("Panda is awesome!".encode()).decode(),
                "mimeType": "text/plain",
                "map": {"app": "Cool app name", "type": "ord", "name": "Text #2"},
        }
        ]

# Endpoint URL for inscription
url = "https://api.panda-wallet.com/inscribe"  # Replace with the actual endpoint URL

# Provider token
provider_token = init_provider()

# Headers for the request
headers = {
     "Content-Type": "application/json",
     "Authorization": f"Bearer {provider_token}"
    }

# Make the request to inscribe
   try:
       response = requests.post(url, headers=headers, data=json.dumps(inscriptions))
       response_data = response.json()
       print("Transaction ID:", response_data["txid"])
       print("Raw Transaction:", response_data["rawtx"])
   except requests.exceptions.RequestException as err:
       print("Error:", err)

Replace `"https://api.panda-wallet.com/inscribe"` with the actual endpoint URL and ensure `init_provider()` is correctly implemented to retrieve your wallet provider token.

For more details, visit the [Panda Wallet Provider API documentation](https://panda-wallet.gitbook.io/provider-api/ordinals/inscribe).