import asyncio

from TonTool import *



    # client = TonApiClient()

    # client = TonCenterClient(base_url='http://127.0.0.1:80/')
s =  create_wallet()
ss = deploy_wallet(s['mnemonics'])
print(ss)
print(s)
