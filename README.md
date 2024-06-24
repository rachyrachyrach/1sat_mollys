1sat Mollys
=================

Welcome to the repository for creating [1SatOridinals](https://www.1satordinals.com) transactions using python. This is a test to create on 1satordinals 

[Documentation for Inscribing](https://panda-wallet.gitbook.io/provider-api/ordinals/inscribe)

Want to do the bare minium which is inscribing into the op_return
https://docs.1satordinals.com/#inscribing-in-outputs

May try [bsvlib](https://github.com/gitzhou/bsvlib) instead of bitsv. 
==============

1. create virtual environment 
python3 -m venv .venv

2. Install your python libraires 

```
python3 -m pip install -r requirements.txt

```


3. We will need a private key to your wallet.  I used the [BSV_wallet](https://github.com/rachyrachyrach/bsv_wallet) script.  We need to make a local environment, Run ```export BSV_KEY="Your private key"```

4. test by running the script to print out your address. ```python3 1sat.py```

5. Need to convert to hex.  Note used bsvlib https://github.com/gitzhou/bsvlib/blob/master/bsvlib/constants.py
example OP_RESVERED = b'\xae

6. we created op.py with all the stuff from bsvlib

## Notes

We found out the python library bitsv automatically includes the op_return first. 

Notes from Satchmo: 
"It looks like this is being added to OP_RETURN instead of in the script (either the beginning or the end). The unexecuted op if wrapper has to come before op_return (and you don’t need to use op return at all unless you want to add additional metadata )"


Zach mentioned using ChatGPT to have the javascript libary written.  The ```helper.py``` file is the result. 

"“Can you rewrite this js helper library in Python?"

https://x.com/developingzack/status/1803118585717616816?s=46&t=MlQ-5v3EU8bliohuL0GxHQ

https://github.com/BitcoinSchema/js-1sat-ord

# Libraries
Had to install ```pip3 install python-bitcoinlib``` for ```inscribe.py``` and ```new.py```

## The Error

```

python3 1sat.py
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
<class 'bytes'>
[Unspent(amount=9336086, confirmations=1966, txid='8283faf1b0691862f7bfa9d6631d96004a5aef9e2215438c23ab0ed3be0075e8', txindex=2), Unspent(amount=218, confirmations=833, txid='25a5856c2a9dfa0ade6ec660477ed51e597be896b352b7b6d751d2af936322c9', txindex=0), Unspent(amount=436, confirmations=830, txid='e592d6a7f1b2f4cc02a3f8412fcbf93a03ce0d730e51d5c325b018e8e4272e95', txindex=0), Unspent(amount=100, confirmations=485, txid='11c6d866bc9182b3182624e5d5330142e1c740b6081ec680b9d8b020da228a2e', txindex=0), Unspent(amount=100, confirmations=485, txid='e4f20810ac14e222a16b3aff009484ecd60e582809e4ee8e8be894710a981414', txindex=0), Unspent(amount=100, confirmations=377, txid='3b6c239c210dda68257e2182fcccd436971b9ff987b6033f3176b19b4cb14a40', txindex=0), Unspent(amount=1000, confirmations=377, txid='1a996d1bb62f73cbcd3dc730a5750b0de6fbd5c49ed372d4b766465a38397cf4', txindex=0), Unspent(amount=100, confirmations=374, txid='70dfe23c112bc4a07d864044cf8758b0c13c6856dbe34f05afbcbeccd80f2531', txindex=0), Unspent(amount=100, confirmations=374, txid='afce2f634ba87117bbe51f8bc447c1188bb728480cc34a5ac86040cb39ab51fe', txindex=0), Unspent(amount=100, confirmations=374, txid='838136e945d432921d95bd72ed03a7afd216ba1af5d635d599404ecaf3cca595', txindex=0), Unspent(amount=100, confirmations=374, txid='b5edbd86454eb1eccd18426e799d546d8b1af813db148fa2d5447911cbad6912', txindex=0), Unspent(amount=100, confirmations=369, txid='3c50fb5f4b11ac31061852db0918fe7fb8dc1a0e0950bdae967f8e26be27593f', txindex=0), Unspent(amount=10, confirmations=273, txid='8007da03e5c52ce02cb2c94e93d2fa151deed9f2a466d1187818fb38bb9acba2', txindex=0), Unspent(amount=100, confirmations=273, txid='ea32be068f0f618bda7079c87cf20364e47557ef7720f7843e508abfad35f498', txindex=0), Unspent(amount=10, confirmations=264, txid='816045f0b2b16af1c80e00c7258d42ac48c0244c1fa5c190875df7cc11ecf646', txindex=0), Unspent(amount=100, confirmations=262, txid='9d203a48830e08dbe9cbedfa8f10ecf64db4fda1b8ff0dfb8ebea8514746a8d5', txindex=0), Unspent(amount=10, confirmations=261, txid='625222f0a6c24555584800da71f819ebc9884606c14de6441cc3d983c21c6492', txindex=0), Unspent(amount=100, confirmations=261, txid='29e14f315009cb6c67e56dc1e2b622eae4e5ecda51ad1cbe560e8d8865624436', txindex=0), Unspent(amount=100, confirmations=261, txid='0311bfce731251a95662c02ad341929c3b177640979ec4292ae8a51811259dc1', txindex=0), Unspent(amount=1000, confirmations=261, txid='9d61ecc4b2662ec0d4cbfd0945771e8da8974c5492b36a4b996fd1b0b630059e', txindex=0), Unspent(amount=100, confirmations=231, txid='9b904c676fb719cfa4b9b3d436e822f9815860795f27cc56de06c4dbc7c240f4', txindex=0), Unspent(amount=100, confirmations=174, txid='11cb8e756d7d0bbba487e3151f8cf4c59df67bca701f63809547ee60402bd645', txindex=0)]
Traceback (most recent call last):
  File "/Users/rachael/github/1sat_mollys/1sat.py", line 20, in <module>
    txid = my_key.do_not_send_op_return(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'PrivateKey' object has no attribute 'do_not_send_op_return'
```
=================

Notes:

Tried using the JaveScript library. May need to try the ```await``` function call: 

In JavaScript to test out making a 1satordinal.  Our problem, we get a transaction promise from createOrdinal. We get a success call and shows a pointer.

This is the output: 

```
tx id is: [object Promise]
Transaction { ptr: 1179704 }
```


==================

Javascript example. The ```fundAndBroadcast``` adds payment and change to the transaction and broadcasts it. 

```
    public async create(file: File): Promise<string> {
        const tx = new Tx();
        const script = this.ordAdd.toTxOutScript()
            .writeOpCode(OpCode.OP_FALSE)
            .writeOpCode(OpCode.OP_IF)
            .writeBuffer(Buffer.from("ord"))
            .writeOpCode(OpCode.OP_1)
            .writeBuffer(Buffer.from(file.type))
            .writeOpCode(OpCode.OP_0)
            .writeBuffer(file.content)
            .writeOpCode(OpCode.OP_ENDIF)

        tx.addTxOut(new Bn(1), script)

        const parents: PreviousOutput[] = []
        return this.fundAndBroadcast(tx, parents)
    }
```

===================


JavaScript example using ```ts-bitcoin``` library to write the ordinals, using the Bitcoin Script directly. 

The FUND portion of fundandBroadcast


```
tx.addTxIn(
    Buffer.from(utxo.txid, 'hex').reverse(),
    utxo.vout,
    new Script(),
    TxIn.SEQUENCE_FINAL
);
tx.addTxOut(
    new Bn(satsIn - satsOut - fee),
    Address.fromString(address).toTxOutScript()
);

const sig = tx.sign(
    KeyPair.fromPrivKey(PrivKey.fromWif(wif)),
    Sig.SIGHASH_ALL | Sig.SIGHASH_FORKID,
    0,
    Script.fromBuffer(Buffer.from(utxo.script, 'hex'),
    new Bn(utxo.satoshis)
);
tx.txIns[0].setScript(
    new Script()
        .writeBuffer(sig.toTxFormat())
        .writeBuffer(this.payKp.pubKey.toBuffer())
);

const txHex = tx.toHex();
```

======

More notes for using JavaScript to create a 1satordinal:

use ```ts-bitcoin```, but to write the ordinals, I just write the Bitcoin Script directly. It's only a few op codes


======
