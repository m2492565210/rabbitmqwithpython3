'''
Created on 2018年3月20日

@author: m24
'''
# -*- coding: UTF-8 -*-

import pika, sys
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel();

channel.exchange_declare(exchange="hello-exchange", 
                         exchange_type="direct", 
                         passive=False, 
                         durable=True, 
                         auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(body=msg, 
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola")
