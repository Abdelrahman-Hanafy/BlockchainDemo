def mine_block(blockchain):
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'Current legth':len(blockchain.chain)}
 
    return response,blockchain

def display_chain(blockchain):
    response = {'chain': blockchain.chain}
    print(blockchain.chain)
    return response

def valid(blockchain):
    valid = blockchain.chain_valid(blockchain.chain)
    flg = False
    if valid:
        response = {'message': 'The Blockchain is valid.'}
        flg = True
    else:
        response = {'message': 'The Blockchain is not valid.'}

    return response,flg