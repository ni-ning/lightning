# -*-coding:utf-8 -*-

from blinker import signal


_ALPHA_SIGNAL_COMMIT_EVENT = 'alpha_signal_commit_event'
alpha_signal_commit_event = signal(_ALPHA_SIGNAL_COMMIT_EVENT)
