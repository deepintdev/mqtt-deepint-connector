#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.


import logging
import logging.config
from os import path


LOGGER_NAME = 'mqtt-deepint-connector'
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler']
        }
    },
    'formatters': {
        'consoleFormatter': {
            'format': '[%(asctime)s] %(message)s'
        }
    },
    'handlers': {
        'consoleHandler': {
            'level': 'INFO',
            'formatter': 'consoleFormatter',
            'class': 'logging.StreamHandler'
        }
    }
}


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)


def serve_application_logger():
    """
    Setups logger for application if not initializes, and servers the application logger.

    Returns: 
        :obj:`logging.logger` application logger
    """

    return logger