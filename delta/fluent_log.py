# -*- coding:utf-8 -*-
import logging
import traceback
from fluent import sender

SETUP_STATES = {'done': False}


class FluentTaggedHandler(logging.Handler):
    def __init__(self, base_tag, host="localhost", port=24224, timeout=1):
        logging.Handler.__init__(self)
        self.sender = sender.FluentSender(base_tag, host=host, port=port, timeout=timeout)

    def emit(self, record):
        content = record.getMessage()
        if record.exc_info:
            tb = traceback.format_exception(*record.exc_info)
            content = '%s\n%s' % (content, ''.join(tb))
        return self.sender.emit(record.name, content)


def setup_fluent(base_tag, host="localhost", port=24224, timeout=1, level=logging.INFO):
    '''
    setup root logger to a fluent handler.
    '''
    if SETUP_STATES['done']:
        return False
    SETUP_STATES['done'] = True
    handler = FluentTaggedHandler(base_tag, host=host, port=port, timeout=timeout)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level)
    return True


if __name__ == '__main__':
    setup_fluent('root', host='127.0.0.1', port=24224)

