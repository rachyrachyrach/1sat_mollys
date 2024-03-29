1sat Mollys
=================

Welcome to the repository for creating [1SatOridinals](https://www.1satordinals.com) transactions using python. This is a test to create on 1satordinals 


==============

1. create virtual environment 
python3 -m venv .venv

2. Create requiremnts.txt file

3. pip install git+https://github.com/Beryllium-Team/bitsv@add_key_beta

4. We will need a private key to your wallet.  I used the [BSV_wallet](https://github.com/rachyrachyrach/bsv_wallet) script.  We need to make a local environment, Run ```export BSV_KEY="Your private key"```

5. test by running the script to print out your address. ```python3 1sat.py```

6. Need to convert to hex.  Note used bsvlib https://github.com/gitzhou/bsvlib/blob/master/bsvlib/constants.py
example OP_RESVERED = b'\xae

7. we created op.py with all the stuff from bsvlib

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
