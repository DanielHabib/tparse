from unittest import TestCase

from tparse_exceptions import BadTagStructure, InvalidTag, MissingClosingTag
from main import TParse


class TParseTest(TestCase):
    def test_invalid_tag_raised(self):
        """Ensure a tag with whitespace `< em>` fails"""
        tparse = TParse()
        string = "<e m>dfsf sdfsd<em>"

        with self.assertRaises(InvalidTag):
            tparse.tparse(string)

    def test_missing_closing_tag(self):
        """Be sure that if missing a closing tag, we throw an error"""
        tparse = TParse()
        string1 = "<em>dfsf sdfsd"

        with self.assertRaises(MissingClosingTag):
            tparse.tparse(string1)

        string2 = "<em>dfsf<foo></foo>sdfsd"

        with self.assertRaises(MissingClosingTag):
            tparse.tparse(string2)

    def test_bad_tag_structure_fails(self):
        """Test that bad tag integrity fails"""
        tparse = TParse()
        string = "<em>dfsf<foo></foo>sdfsd<bar></em></bar>"

        with self.assertRaises(BadTagStructure):
            tparse.tparse(string)
