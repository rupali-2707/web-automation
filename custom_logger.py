import logging

logger = None


def get_logger(name=''):
    global logger
    if not logger:
        name = name if name.strip() else __name__
        logger = logging.getLogger(name)
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s')
        logger.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        fh = logging.FileHandler('logs.txt')
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(sh)
        logger.addHandler(fh)
    return logger
