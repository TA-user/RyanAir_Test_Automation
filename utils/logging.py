from loguru import logger


class Logger:
    @staticmethod
    def debug_only(record):
        return record["level"].name == "DEBUG"

    @staticmethod
    def error_only(record):
        return record["level"].name == "ERROR"

    def set_logger(self):
        logger.remove()
        return logger.add("logs/debug.log",
                          format="{time:DD:MM:YYYY:h:m:s} {level} {message}",
                          level="DEBUG",
                          rotation="10 KB",
                          retention="2 days",
                          filter=self.debug_only), \
               logger.add("logs/errors.log",
                          format="{time:DD:MM:YYYY:h:m:s} {level} {message}",
                          rotation="10 KB",
                          retention="2 days",
                          filter=self.error_only)
