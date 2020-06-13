import logging

# criando um logger customizado
logger = logging.getLogger(__name__)

# criando handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('handler.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# criando formatadores e adicionando aos handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# adicionando handlers ao log
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
