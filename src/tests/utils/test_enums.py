

from enum import Enum
import unittest

from research_base.utils.enum_utils import convert_str_arg_to_enum_member
from research_base.utils.utils import str2enum


class EnumTest(Enum):
    """
    A simple enum for testing.
    """
    VALUE1 = "value1"
    VALUE_2 = "value_2"
    VALUE_3 = "value_3"

from enum import Enum
class SomeBasicEnum(Enum):
    A = 1
    B = 2
    C = 3

class TestProgramParamsSmoke(unittest.TestCase):

    def test_convert_str_to_enum(self):
        test_cases = [
            ("value1", EnumTest.VALUE1),
            ("VALUE1", EnumTest.VALUE1),
            ("value_2", EnumTest.VALUE_2),
            ("VALUE_2", EnumTest.VALUE_2),
            ("value_3", EnumTest.VALUE_3),
            ("VALUE_3", EnumTest.VALUE_3),
        ]

        for (arg, expected) in test_cases:
            with self.subTest(arg=arg):
                self.assertEqual(expected, convert_str_arg_to_enum_member(arg, EnumTest))
    


    def test_str2enum(self):
        test_cases = [
            ("A", SomeBasicEnum.A),
            ("B", SomeBasicEnum.B),
            ("C", SomeBasicEnum.C),
        ]

        for (arg, expected) in test_cases:
            with self.subTest(arg=arg):
                self.assertEqual(expected, str2enum(arg, SomeBasicEnum))