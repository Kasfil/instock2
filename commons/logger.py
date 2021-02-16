import logging
import logging.config
from datetime import date
from app.configs import configs

class OnDebugFalse(logging.Filter):
    """Log only if DEBUG_MODE is False"""
    def filter(self, record):
        return not configs.DEBUG_MODE

class OnDebugTrue(logging.Filter):
    """Log only if DEBUG_MODE is True"""
    def filter(self, record):
        return configs.DEBUG_MODE

# set logging configuration
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)s - %(levelname)s - %(message)s'
        },
        'file': {
            'format': '%(name)s - %(levelname)s - %(asctime)s - %(module)s - %(process)d - %(thread)d - %(message)s'
        }
    },
    'filters': {
        'debug_true': {
            '()': OnDebugTrue
        },
        'debug_false': {
            '()': OnDebugFalse
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'WARNING',
            'filters': ['debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            # should be in root/logs directory
            # filename should be month-date-year.txt
            'filename': 'logs/' + date.today().strftime('%b-%d-%Y') + '.log',
            'maxBytes': 1024
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            'propagate': True
        },
        'database': {
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}

# setup logging instance
def setup_logger():
    """setup logger"""
    logging.config.dictConfig(logging_config)
