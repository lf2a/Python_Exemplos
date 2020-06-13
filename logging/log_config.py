import logging.config

logging.config.fileConfig(fname='log_config.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug('Isto é uma mensagem de debug')
