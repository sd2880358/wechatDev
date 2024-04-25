import logging.config
import os
from pythonjsonlogger import jsonlogger

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "json"
        },
        # 'file_handler': {
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'level': 'INFO',
        #     'formatter': 'json',
        #     'filename': "/home/ubuntu/wechatDev/log/file_handler.log",
        #     'maxBytes': 1024,
        #     'backupCount': 3
        # }
    },
    "loggers": {
        "": {
            "handlers": ["stdout"], 
            "level": "DEBUG"
            },
        # "default_log":{
        #     "handlers": ["file_handler"],
        #     "level": "INFO"
        # }
        },
                    
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('default_log')

if __name__ == '__main__':
    logging.getLogger('layer_two')
    logging.warning('second')
