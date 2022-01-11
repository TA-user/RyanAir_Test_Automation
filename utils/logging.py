from loguru import logger


class Logger:
    @staticmethod
    def set_logger():
        logger.remove()
        return logger.add("debug.log", format="{time:DD:MM:YYYY:h:m:s} {level} {message}", level="DEBUG",
                          rotation="10 KB")
