#!/usr/bin/env python3
"""
0.Regex-ing
"""
import re
import logging
from typing import List
from mysql.connector import (connection)
import os


PII_FIELDS: List[str] = ['name', 'email', 'phone', 'ssn', 'ip']


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """
    Agrs:
        fields: a list of strings representing
        all fields to obfuscate
        redaction: a string representing by
        what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which
        character is separating all fields in the
        log line (message)
    Return:
        obfuscated text
    """
    for field in fields:
        message = re.sub(rf'(?<={field}=).*?(?={separator})',
                         redaction,  message)

    return message


def get_logger() -> logging.Logger:
    """
    Args:
        Void
    Return:
        logging.Logger
    """
    user_sata_logger = logging.getLogger("user_data")
    user_sata_logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    user_sata_logger.addHandler(stream_handler)

    return user_sata_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Args:
        Void
    Return:
        Connect to secure database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hosting = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')
    cnx = connection.MySQLConnection(username=username, password=password',
                                     host=hosting,
                                     database=db)
    return cnx


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[int]):
        """
        Init
        Args:
            fields: list of fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Args:
            Record: the record instance
        Return:
            record formatted message
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
