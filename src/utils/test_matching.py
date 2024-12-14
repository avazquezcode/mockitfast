import unittest
from utils.matching import replace_variables_in_str, replace_variables_in_dict
from dataclasses import dataclass


class Test(unittest.TestCase):
    def test_replace_variables_in_str(self):
        @dataclass
        class TestCase:
            name: str
            variables: dict
            target: str
            expected: str

        tests = [
            TestCase(
                name="empty variables",
                variables={},
                target="abc",
                expected="abc",
            ),
            TestCase(
                name="empty text",
                variables={"a": "b"},
                target="",
                expected="",
            ),
            TestCase(
                name="no matches available",
                variables={"a": "b"},
                target="eed",
                expected="eed",
            ),
            TestCase(
                name="match available",
                variables={"a": "b", "d": "e"},
                target="{a}{a}d",
                expected="bbd",
            ),
            TestCase(
                name="match available - d is also a variable in the target",
                variables={"a": "b", "d": "e"},
                target="{a}{a}{d}",
                expected="bbe",
            ),
        ]

        for test in tests:
            result = replace_variables_in_str(test.variables, test.target)
            self.assertEqual(
                test.expected,
                result,
                "test: {} failed - expected: {} - got: {}".format(
                    test.name,
                    test.expected,
                    result,
                )
            )

    def test_replace_variables_in_dict(self):
        @dataclass
        class TestCase:
            name: str
            variables: dict
            target: dict
            expected: dict

        tests = [
            TestCase(
                name="empty variables",
                variables={},
                target={"a": "b"},
                expected={"a": "b"},
            ),
            TestCase(
                name="empty dict",
                variables={"a": "b"},
                target={},
                expected={},
            ),
            TestCase(
                name="no matches available",
                variables={"a": "b"},
                target={"c": "d"},
                expected={"c": "d"},
            ),
            TestCase(
                name="match available in the index",
                variables={"a": "b"},
                target={"{a}_1": "d"},
                expected={"b_1": "d"},
            ),
            TestCase(
                name="match available in the value",
                variables={"a": "b"},
                target={"1": "{a} d"},
                expected={"1": "b d"},
            ),
            TestCase(
                name="match available in both index and value",
                variables={"a": "b"},
                target={"{a}_1": "{a} d"},
                expected={"b_1": "b d"},
            ),
            TestCase(
                name="match available in both index and value, where value is a dict with more than 1 level",
                variables={"a": "b"},
                target={"{a}_1": {"b_{a}": "{a}"}},
                expected={"b_1": {"b_b": "b"}},
            ),
        ]

        for test in tests:
            result = replace_variables_in_dict(test.variables, test.target)
            self.assertEqual(
                test.expected,
                result,
                "test: {} failed - expected: {} - got: {}".format(
                    test.name,
                    test.expected,
                    result,
                )
            )


if __name__ == '__main__':
    unittest.main()
