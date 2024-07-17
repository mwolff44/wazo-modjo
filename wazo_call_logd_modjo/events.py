# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_bus.resources.common.event import TenantEvent, UserEvent


class CallLogUserCreatedEvent(UserEvent):
    # https://github.com/wazo-platform/wazo-bus/blob/a4997b1fa8ffe3f32335337bfbf18e2e7baf3d4f/wazo_bus/resources/call_logs/events.py#L18
    service = 'call_logd'
    name = 'call_log_user_created'
    routing_key_fmt = 'call_log.user.{user_uuid}.created'
    required_acl_fmt = 'events.call_log.user'

    def __init__(self, content, tenant_uuid, user_uuid):
        super().__init__(content, tenant_uuid, user_uuid)

class CallLogCreatedEvent(TenantEvent):
    service = 'call_logd'
    name = 'call_log_created'
    routing_key_fmt = 'call_log.created'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)
