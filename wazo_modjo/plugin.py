# -*- coding: utf-8 -*-
# Copyright 2018-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_auth_client import Client as AuthClient
from wazo_call_logd_client import Client as CallLogdClient

from .bus_consume import CdrBusEventHandler

class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']
        bus_consumer = dependencies['bus_consumer']
        bus_publisher = dependencies['bus_publisher']

        call_logd_client = CallLogdClient(**config['call_logd'])

        # Get settings
        try:
            MODJO_API = config['modjo_api']
        except:
            MODJO_API = "https://api.modjo.ai/v1/calls"
        try:
            MODJO_KEY = config['modjo_key']
        except:
            print("ERROR : DEFINE MODJO KEY !")

        try:
            MODJO_USERS = config['modjo_users']
        except:
            print("ERROR : DEFINE MODJO USERS !")

        token_changed_subscribe(call_logd_client.set_token)

        cdr_bus_event_handler = CdrBusEventHandler(bus_publisher, MODJO_KEY, MODJO_USERS)
        cdr_bus_event_handler.subscribe(bus_consumer)
