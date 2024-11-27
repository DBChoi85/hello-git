from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://alpha-virulent-brook.discover.quiknode.pro/e964325ac8ebdb46775528e73e6c7a0749343ba1/'))


account = "0x866c9a77d8Ab71d2874703e80cb7aD809b301e8e"

check_connoction = w3.is_connected()
# print(check_connoction)

latest_block_number = w3.eth.get_block_number()
# print(latest_block_number)

account_nonce = w3.eth.get_transaction_count(account=account)
print(account_nonce)
# 역방향으로 가야한다.
hash_list = []

day_block = 5760
hour_block = 240
min_block = 4
week_block = 40320
month_block = 172800
year_block = 2073600
# block create 5760 in a day
# decrease in year = 2073600 > month = 172800 > week = 40320 > day = 5760 > hour = 240 > min = 4 

for year_idx in range(latest_block_number, 0, -(year_block)):
    year_blcok_number = year_idx
    compare_year_block_number = year_idx - year_block
    if compare_year_block_number < 0:
        compare_year_block_number = 0
    year_nonce = w3.eth.get_transaction_count(account, year_blcok_number)
    compare_year_nonce = w3.eth.get_transaction_count(account, compare_year_block_number)
    print('year compare : ',year_nonce, compare_year_nonce)
    if year_nonce != compare_year_nonce:
        for month_idx in range(year_idx, year_idx-year_block, -(month_block)):
            month_nonce = w3.eth.get_transaction_count(account, month_idx)
            compare_month_nonce = w3.eth.get_transaction_count(account, month_idx - month_block)
            print('month compare : ', month_nonce, compare_month_nonce)
            if month_nonce != compare_month_nonce:
                for week_idx in range(month_idx, month_idx-month_block, -(week_block)):
                    week_nonce = w3.eth.get_transaction_count(account, week_idx)
                    compare_week_nonce = w3.eth.get_transaction_count(account, week_idx - week_block)
                    print('week compare : ', week_nonce, compare_week_nonce)
                    if week_nonce != compare_week_nonce:
                        for day_idx in range(week_idx, week_idx - week_block, -(day_block)):
                            print('day idx : ',day_idx)
                            day_nonce = w3.eth.get_transaction_count(account, day_idx)
                            compare_day_nonce = w3.eth.get_transaction_count(account, day_idx - day_block)
                            print('day compare : ', day_nonce, compare_day_nonce)
                            if day_nonce != compare_day_nonce:
                                for hour_idx in range(day_idx, day_idx - day_block, -(hour_block)):
                                    hour_nonce = w3.eth.get_transaction_count(account, hour_idx)
                                    compare_hour_nonce = w3.eth.get_transaction_count(account, hour_idx - hour_block)
                                    print('hour compare : ', hour_nonce, compare_hour_nonce)
                                    if hour_nonce != compare_hour_nonce:
                                        for min_idx in range(hour_idx, hour_idx - hour_block, -(min_block)):
                                            min_nonce = w3.eth.get_transaction_count(account, min_idx)
                                            compare_min_nonce = w3.eth.get_transaction_count(account, min_idx - min_block)
                                            print('min compare : ', min_nonce, compare_min_nonce)
                                            if min_nonce != compare_min_nonce:
                                                for idx in range(min_idx, min_idx - min_block, -1):
                                                    print('block idx : ', idx)
                                                    block_info = w3.eth.get_block(idx)
                                                    tx_info = block_info.transactions
                                                    for tx in tx_info:
                                                        tx_detail = w3.eth.get_transaction(tx)
                                                        if tx_detail['from'] == account or tx_detail['to'] == account:
                                                            hash_list.append(w3.to_hex(tx))
                                                            if len(hash_list) == account_nonce:
                                                                break


print(hash_list)
