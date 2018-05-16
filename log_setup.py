import logging
import logging.handlers

# Получаем описатель логгера с названием test_log (логгер по умолчанию - logging.getLogger() )
logger = logging.getLogger("client_connected")

# Конструируем форматную строку - то, как будут записыватся сообщения в лог, если лог будет хранится в файле
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Конструируем файловое хранилище лога
fn = logging.FileHandler("connections.log")
fn.setLevel(logging.DEBUG)
fn.setFormatter(formatter)

# Присоединяем хранилище к логгеру
logger.addHandler(fn)
logger.setLevel(logging.DEBUG)

##########################

def connections_log(f):

	def wrap(*args, **kwargs):
		lst = list(args)
		client_info = f(lst[0], lst[1], lst[2])
		if client_info:
		    logger.info('client has connected with ip = {0}'.format(client_info))
		return(client_info)

	return(wrap)