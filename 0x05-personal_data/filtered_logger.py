#!/usr/bin/env python3
"""
0.Regex-ing
"""
import re
from typing import List


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
