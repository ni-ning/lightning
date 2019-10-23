# -*-coding:utf-8 -*-

import logging
import event_bus

logger = logging.getLogger(__name__)


def receive_event(sync_data):
    print('sync_data: %s' % sync_data)
    logger.info('sync_data: %s' % sync_data)


event_bus.alpha_signal_commit_event.connect(receive_event)
