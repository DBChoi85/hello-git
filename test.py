from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://alpha-virulent-brook.discover.quiknode.pro/e964325ac8ebdb46775528e73e6c7a0749343ba1/'))


account = "0x866c9a77d8Ab71d2874703e80cb7aD809b301e8e"

check_connoction = w3.is_connected()
# print(check_connoction)

latest_block_number = w3.eth.get_block_number()
# print(latest_block_number)

nonce = w3.eth.get_transaction_count(account=account)
print(nonce)
# 역방향으로 가야한다.
hash_list = []
# block create 5760 in a day
# decrease in year = 2073600 > month = 172800 > week = 40320 > day = 5760 > hour = 240 > min = 4 
for i in range(latest_block_number, 0, -5760):
    n = w3.eth.get_transaction_count(account=account, block_identifier=i)
    pre_n = w3.eth.get_transaction_count(account=account, block_identifier=(i-5760))
    if n == pre_n:
        pass
    else:
        for idx in range(i, i-5760, -1):
            t = w3.eth.get_block(idx)
            print(idx)
            t_tx = t.transactions
            for tx in t_tx:
                tx_info = w3.eth.get_transaction(tx)
                if tx_info['from'] == account or tx_info['to'] == account:
                    hash_list.append(w3.to_hex(tx))
            if len(hash_list) == nonce:
                break


print(hash_list)
