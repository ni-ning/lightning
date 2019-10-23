# -*-coding:utf-8 -*-

import event_bus


def commit_event():
    sync_data = {
        'custom_id': '007',
        'custom_name': 'beta'
    }
    event_bus.alpha_signal_commit_event.send(sync_data)

