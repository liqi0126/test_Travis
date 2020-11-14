import unittest
from .post import post_params_check


class PostCheckTest(unittest.TestCase):
    @staticmethod
    def base_case():
        return {
            'title': 'a' * 32,
            'content': 'b' * 128
        }

    def test_no_content_case(self):
        self.assertEqual(post_params_check(None), ('title', False))

    def test_base_case(self):
        case = self.base_case()
        self.assertEqual(post_params_check(case), ("ok", True))

    def test_title_edge_length_case(self):
        case = self.base_case()
        case['title'] = 'a'
        self.assertEqual(post_params_check(case), ("ok", True))

        case = self.base_case()
        case['title'] = 'a' * 64
        self.assertEqual(post_params_check(case), ("ok", True))

    def test_no_title_or_not_str_case(self):
        case = self.base_case()
        del case['title']
        self.assertEqual(post_params_check(case), ("title", False))

        case = self.base_case()
        case['title'] = 10
        self.assertEqual(post_params_check(case), ("title", False))

    def test_too_short_or_too_long_title_case(self):
        case = self.base_case()
        case['title'] = ''
        self.assertEqual(post_params_check(case), ('title', False))

        case['title'] = 'a' * 65
        self.assertEqual(post_params_check(case), ('title', False))

    def test_content_edge_length_case(self):
        case = self.base_case()
        case['content'] = 'b' * 15
        self.assertEqual(post_params_check(case), ('ok', True))

        case = self.base_case()
        case['content'] = 'b' * 256
        self.assertEqual(post_params_check(case), ('ok', True))

    def test_no_content_or_not_str_case(self):
        case = self.base_case()
        del case['content']
        self.assertEqual(post_params_check(case), ('content', False))

        case = self.base_case()
        case['content'] = 20
        self.assertEqual(post_params_check(case), ('content', False))

    def test_too_short_or_too_long_content_case(self):
        case = self.base_case()
        case['content'] = 'b' * 14
        self.assertEqual(post_params_check(case), ('content', False))

        case['content'] = 'a' * 257
        self.assertEqual(post_params_check(case), ('content', False))


if __name__ == '__main__':
    unittest.main()
