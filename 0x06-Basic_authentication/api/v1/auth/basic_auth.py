#!/usr/bin/env python3
""" Module of Basicauth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Bacis Auth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Base 64 Authorization Header
            Args:
                authorization_header: base64
            Return:
                Header in base64 or None
        """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded