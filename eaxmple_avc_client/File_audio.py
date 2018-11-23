#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 15:24
# @Author  : Kevindi
# @Site    : 
# @File    : File_audio.py.py
# @Software: PyCharm Community Edition
# @Desc    :
from time import sleep

from avs_client import AlexaVoiceServiceClient

alexa_client = AlexaVoiceServiceClient(
    client_id='amzn1.application-oa2-client.0f63dd55d920481290622afc808d2083',
    secret='74229b1d18cbd3347b8a869424b205cbab2e9c92cc9c16195e568dd14001786f',
    refresh_token='Atzr|IwEBINRbNFfZtJvnXyVjh_zKElCE-STpFMzH6uuYWD413HdiK9zxJFuSkG98Hx5eFvZYK86eJ9xMja9MHdlFIn625XiAYuuwcm1kIe09B8NGebx-gD-4xy9txg2gtMRc_lSqxgm3tfgLaWZH1XdhYWEn0zEXzQPQwrtoMlRXLGUcAr6HqYWp9apwquMryXKRy93kkZ4FjV5mHDsWnWEqkOs_W_8_J0QxpaR3eTcHnpeU9VN0VK_R9FRpcwPRzXUr3_XK_XPM7_QsI8v3LZUo9jwoji25-liYgXjfIhiCy1uXskiILy9fk-emSg0PqtcBuSbE4ilMseBQypoyC4zIssf3_1NMZWY_zQpzRl2FGorBCHTJoqcqGd5UqWUN8-3KbAWxQZWiOZRf14-gAtmyRrcOCzGyMT9AUFgkprkUqO-cTiRjjFerPzGFq7_FK5c0nTRuO05oG4DNp8_RefPT5OJjgGfLtIfCPumxATpujALp4RbcQ31v0Crl1inxiSgt6qfwWrNNNGYo3mg92h8CnsOIrXSVYg9jfLJmryhtBZzU8QjvMaSdZrousQ_DHL5r-BwfGmI',
)

alexa_client.connect()  # authenticate and other handshaking steps
print('finished authenticate and handshaking.')

i = 0
while i< 10:
    with open('./alexa_what_time_is_it.wav', 'rb') as f1:
        alexa_response_audio = alexa_client.send_audio_file(f1)
        f1.close()
    with open('./output'+str(i)+'.wav', 'wb') as f2:
        f2.write(alexa_response_audio)
        f2.close()
    print('finished session: ',i)
    sleep(10)
    i += 1