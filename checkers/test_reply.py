import unittest
from .reply import reply_post_params_check


class ReplyCheckTest(unittest.TestCase):

    @staticmethod
    def base_case():
        return {
            'content': 'a' * 128,
            'replyId': 10
        }

    def test_no_content_case(self):
        self.assertEqual(reply_post_params_check(None), ('content', False))

    def test_base_case(self):
        case = self.base_case()
        self.assertEqual(reply_post_params_check(case), ("ok", True))

    def test_no_content_or_not_str(self):
        case = self.base_case()
        del case['content']
        self.assertEqual(reply_post_params_check(case), ('content', False))

        case = self.base_case()
        case['content'] = 123123123
        self.assertEqual(reply_post_params_check(case), ('content', False))

    def test_content_edge_length_case(self):
        case = self.base_case()
        case['content'] = 'a' * 15
        self.assertEqual(reply_post_params_check(case), ('ok', True))

        case['content'] = 'a' * 256
        self.assertEqual(reply_post_params_check(case), ('ok', True))

    def test_too_long_or_too_short_content_case(self):
        case = self.base_case()
        case['content'] = 'a' * 14
        self.assertEqual(reply_post_params_check(case), ('content', False))

        case = self.base_case()
        case['content'] = 'a' * 257
        self.assertEqual(reply_post_params_check(case), ('content', False))

    def test_no_replyId_case(self):
        case = self.base_case()
        del case['replyId']
        self.assertEqual(reply_post_params_check(case), ('ok', True))

    def test_replyId_not_int_or_neg_case(self):
        case = self.base_case()
        case['replyId'] = 'a'
        self.assertEqual(reply_post_params_check(case), ('replyId', False))

        case = self.base_case()
        case['replyId'] = -1
        self.assertEqual(reply_post_params_check(case), ('replyId', False))

if __name__ == '__main__':
    unittest.main()
