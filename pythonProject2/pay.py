shopId = '506751'
shopArticleId = '538350'
PaymentTokenYandex='381764678:TEST:37437'

from yoomoney import Authorize
from yoomoney import Client

token="410014340604062.0859939BBEDBF76CE9A9838A4ED9D9B0356A912730E070695028B957AC81EFF316D0951AA1E6E31AEC0A2C0699A198ABF97AD596C09358ED512BCAF82B9D53F2F0E8AA95FD1B6A7F68912CBB51105FC724AB65C0768A96F66A58A61EDB6D189BF9FD49E14CDDE7DCC1EC90B20B7287B414EF77F0E54868C7E43A998F5CDCCA0F"

# Получение токена
# def ConnectWith():
#     Authorize(
#         client_id="E96D646CF657A5550D26777597D658599E4E0EE0A6D258C4D37A581DCF334338",
#         redirect_uri="https://t.me/First1111App_Bot",
#
#         scope=["account-info",
#                  "operation-history",
#                  "operation-details",
#                  "incoming-transfers",
#                  "payment-p2p",
#                  "payment-shop",
#                ]
#         )
#
def ConnectWith():
    client = Client(token)
    user = client.account_info()
    print("Account number:", user.account)
    print("Account balance:", user.balance)
    print("Account currency code in ISO 4217 format:", user.currency)
    print("Account status:", user.account_status)
    print("Account type:", user.account_type)
    print("Extended balance information:")
    for pair in vars(user.balance_details):
        print("\t-->", pair, ":", vars(user.balance_details).get(pair))
    print("Information about linked bank cards:")
    cards = user.cards_linked
    if len(cards) != 0:
        for card in cards:
            print(card.pan_fragment, " - ", card.type)
    else:
        print("No card is linked to the account")