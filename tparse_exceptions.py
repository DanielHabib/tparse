"""Exceptions for Tparse"""


class TParseException(Exception):
    """TParse Exception"""


class BadTagStructure(TParseException):
    """There is an inconsistency between open and close tags

        ex: <em><foo></em></foo>
    """


class MissingClosingTag(TParseException):
    """There are unclosed tags"""


class InvalidTag(TParseException):
    """The Tag is Invalid"""
