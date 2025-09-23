from py_utils.logger import set_logging, plog

set_logging()

plog("Mensaje de debug", level=logging.DEBUG)
plog("Mensaje de info", level=logging.INFO)
plog("Mensaje de advertencia", level=logging.WARNING)
plog("Mensaje de error", level=logging.ERROR)
plog("Mensaje crítico", level=logging.CRITICAL)
