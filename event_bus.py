# -*-coding:utf-8 -*-

from blinker import signal


_BETA_SIGNAL_COMMIT_EVENT = 'beta_signal_commit_event'
beta_signal_commit_event = signal(_BETA_SIGNAL_COMMIT_EVENT)
