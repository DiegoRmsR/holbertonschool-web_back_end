#!/usr/bin/env python3
""" Module of Basicauth
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decodes the value of a base64 string
            Args:
                base64_authorization_header: Base64 header
            Return:
                string header decoded or None
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
        except base64.binascii.Error:
            return None

        return decoded.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Base64 decoded value
            Args:
                decoded_base64_authorization_header: string
            Return:
                tuple about user credentials (user_email, user_pwd)
                or tuple (None, None)
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':')

        return credentials[0], credentials[1]

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ email and password
            Args:
                user_email: Email from user
                user_pwd: Currrent user
            Return:
                User instance or None
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({
            "email": user_email,
        })

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
