import tparse_exceptions
"""The Parser
    Be Defensive.
    One potential solution would be to Iterate through the text, checking for opening and closing
    characters. If an opener is found, we put it on a stack. We have to ensure validity of the
    opening and closing tags. While looping we need to ensure that the tags are not empty. If it is
    not empty or accepted, it needs to be removed.

    The interface will probably look like something with a list of what is accepted. So lets first
    focus on removing all tags and leaving the text.
"""


class TParse:
    def __init__(self, accepted_tags=None):
        """

        Args:
            accepted_tags (list): A list of accepted Tags

        """
        self.accepted_tags = [] if accepted_tags is None else accepted_tags

    def tparse(self, text):
        """

        Args:
            text (str):

        Returns: A string that has been cleaned of bad tags

        """
        tags = []
        i = 0
        cleansed_string = ""
        while i < len(text):
            char = text[i]
            if char == '<':
                tag = self.check_tag(text, i)
                if self.is_opener(text, i):
                    tags.append(tag)
                    i += len(tag)
                    if tag in self.accepted_tags:
                        cleansed_string += tag
                else:
                    opener = tags.pop()
                    if '</' + opener[1:] != tag:
                        raise tparse_exceptions.BadTagStructure("Mismatched Tag Structure")
                    i += len(tag)
                    if self.make_opener(tag) in self.accepted_tags:
                        cleansed_string += tag
            else:
                cleansed_string += char
                i += 1
        if tags:
            raise tparse_exceptions.MissingClosingTag("There are {0} tags that are never closed".format(len(tags)))
        return cleansed_string

    @staticmethod
    def make_opener(tag):
        """

        Args:
            tag (str): The string to make the closer for

        Returns: str, the associated opener

        """
        return '<' + tag[2:]

    @staticmethod
    def check_tag(text, i):
        """
        Args:
            text (str):
            i (int):

        Returns: The tag that has been found, otherwise return None

        """
        tag = ''
        while len(text) > i:
            char = text[i]
            if char == ' ':
                raise tparse_exceptions.InvalidTag("Tag in string`{0}`has a blank space".format(char))

            tag += char

            if char == '>':
                return tag
            i += 1
        raise tparse_exceptions.MissingClosingTag("Tag is never closed")

    @staticmethod
    def is_opener(text, i):
        """

        Args:
            text (str):
            i (int):

        Returns: Bool, returns whether the string is an opener or not

        """
        if i < len(text):
            return text[i + 1] != '/'
        raise tparse_exceptions.MissingClosingTag("Tag is never closed")
