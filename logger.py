import logging

if logging.getLogger().hasHandlers():
    logging.getLogger().setLevel(level=logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


class LoggerFactory:
    @staticmethod
    def get_stream_logger(name):
        logger = logging.getLogger(name)
        if logger.hasHandlers():
            for handler in logger.handlers:
                logger.removeHandler(handler)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s,%(msecs)d - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        return logger
