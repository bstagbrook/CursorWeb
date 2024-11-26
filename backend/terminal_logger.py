import logging
import sys

class TerminalLogger:
    def __init__(self, log_file='terminal.log'):
        self.log_file = log_file
        self.logger = logging.getLogger('TerminalLogger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(self.log_file)
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

    def log(self, message):
        self.logger.debug(message)

    def start_logging(self):
        sys.stdout = self
        sys.stderr = self

    def stop_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def write(self, message):
        if message.strip():
            self.log(message)

    def flush(self):
        pass
