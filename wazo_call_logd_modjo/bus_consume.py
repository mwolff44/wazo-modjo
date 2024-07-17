# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import datetime, logging, math, re

from .events import (
    CallLogUserCreatedEvent,
    CallLogCreatedEvent
)

logger = logging.getLogger(__name__)

EXTRACT_USER_UUID = re.compile(r'^events.call_log.user.([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}).created$')

class CdrBusEventHandler(object):

    def __init__(self, bus_publisher, MODJO_API, MODJO_KEY, MODJO_USERS):
        self.bus_publisher = bus_publisher
        self.MODJO_KEY = MODJO_KEY
        self.MODJO_USERS = MODJO_USERS
        self.MODJO_API = MODJO_API

    def subscribe(self, bus_consumer):
        bus_consumer.subscribe('CallLogUserCreated', self._call_log_user_created)
        bus_consumer.subscribe('CallLogCreated', self._call_log_created)

    def _call_log_user_created(self, event):
        tenant_uuid = event['tenant_uuid']
        user_uuid = EXTRACT_USER_UUID.match(event['required_acl'])
        if tenant_uuid == self.MODJO_KEY[tenant_uuid]:
            self._modjo(event, tenant_uuid)
        bus_event = CallLogUserCreatedEvent(
            event,
            tenant_uuid,
            user_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _call_log_created(self, event):
        tenant_uuid = event['tenant_uuid']
        if tenant_uuid == self.MODJO_KEY[tenant_uuid]:
            self._modjo(event, tenant_uuid)
        bus_event = CallLogCreatedEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _modjo(self, event, tenant_uuid):
        print(event)
