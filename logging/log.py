import logging

# tipos logging
logging.debug('Isto é um debug')
logging.info('Isto é uma info')
logging.warning('Isto é um aviso')
logging.error('Isto é um erro')
logging.critical('Isto é um erro critico')

logging.basicConfig(format='[%(asctime)s - %(message)s] %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Cuidado')
