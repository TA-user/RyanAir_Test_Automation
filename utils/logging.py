from loguru import logger


class Logger:
    logger.remove()
    logger.add("debug.log", format="{time:DD:MM:YYYY:h:m:s} {level} {message}", level="DEBUG", rotation="10 KB")
