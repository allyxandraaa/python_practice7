import unittest
from app.io.input import file_input


class TestFileInput(unittest.TestCase):

    def test_file_input_1(self):
        expected_output = (
            "This is a standard text file.\n"
            "It contains multiple lines of ASCII text.\n"
            "Line numbers: 1, 2, 3\n"
            "Punctuation: !@#$%^&*()_+-={}[]|;:'\",.<>?/"
        )
        self.assertEqual(
            file_input("test_data/test_file_input_data/test_file_input_data_1"),
            expected_output,
        )

    def test_file_input_2(self):
        expected_output = (
            "Single line with surrounding whitespace\n"
            "\nLine with only spaces:\n"
            "Mixed    whitespace    inside"
        )
        self.assertEqual(
            file_input("test_data/test_file_input_data/test_file_input_data_2"),
            expected_output,
        )

    def test_file_input_3(self):
        expected_output = (
            'JSON-like content: {"key": "value", "num": 42}\n'
            "CSV-like content: header1,header2\\nvalue1,value2\n"
            "XML-like: <root><item>test</item></root>\n"
            "Binary-like: \\x00\\x01\\x02 (interpreted as text)\n"
            "Newlines:\\n\\n\\n\\n\n"
            "Tabs:\\t\\t\\t"
        )
        self.assertEqual(
            file_input("test_data/test_file_input_data/test_file_input_data_3"),
            expected_output,
        )
