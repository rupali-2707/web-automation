import logging

logger = None


def get_logger(name='' , file_handler=False):
    global logger
    
    if not logger:
        name = name if name.strip() else __name__
        logger = logging.getLogger(name)
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s')
        logger.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        
        if file_handler:
            fh = logging.FileHandler('logs.txt')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
    
    return logger
