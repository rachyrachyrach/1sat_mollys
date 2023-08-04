1sat Mollys
=================

Welcome to the repository for the Molly Match BSV blockchain generative NFT creator using python. This is a test to create on 1satordinals 


==============

1. create virtual environment 
python3 -m venv .venv

2. Create requiremnts.txt file

3. pip install git+https://github.com/Beryllium-Team/bitsv@add_key_beta

4. We will need a private key to your wallet.  I used the BSV_wallet script.  We need to make a local environment, Run ```export BSV_KEY=```

5. test by running the script to print out your address. ```python3 1sat.py```

6. Need to convert to hex.  Note used bsvlib https://github.com/gitzhou/bsvlib/blob/master/bsvlib/constants.py
example OP_RESVERED = b'\xae

7. we created op.py with all the stuff from bsvlib