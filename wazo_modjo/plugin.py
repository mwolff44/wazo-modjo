# -*- coding: utf-8 -*-
# Copyright 2018-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

logger = logging.getLogger(__name__)

class Plugin:

    def load(self, dependencies):
        print("ok")
