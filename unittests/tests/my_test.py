import unittest
from unittest import TestCase
from unittest.mock import patch
from main import show_all_docs_info
from main import check_document_existence
from main import delete_doc
from main import add_new_doc


class TestMain(TestCase):

    @patch('builtins.input', side_effect=["2255 876299", "passport", "Василий Уткин", "3"])
    def test_append_doc_to_shelf(self, mock_input):
        add_new_doc()
        result = show_all_docs_info()
        self.assertEqual(result, [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "passport", "number": "2255 876299", "name":  "Василий Уткин"}
        ])

    def test_check_document_existence(self):
        result = check_document_existence("10006")
        self.assertEqual(result, True)

    @patch('builtins.input', lambda _: "10006")
    def test_remove_doc_from_shelf(self):
        # delete document # 10006
        delete_doc()

        result = show_all_docs_info()
        self.assertEqual(result, [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
            {"type": "passport", "number": "2255 876299", "name": "Василий Уткин"}
        ])

    def test_show_all_info(self):
        result = show_all_docs_info()
        self.assertEqual(result, [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
            {"type": "passport", "number": "2255 876299", "name": "Василий Уткин"}
        ])


if __name__ == '__main__':
    unittest.main()
