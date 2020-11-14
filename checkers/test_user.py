import unittest
from .user import register_params_check


class UserCheckTest(unittest.TestCase):

    @staticmethod
    def base_case():
        return {
            'username': '!@#1As~',
            'password': 'ABCabc123',
            'nickname': 'duludu',
            'document_number': '140202199901264034',
            'mobile': 15801266030,
            'email': 'liqi17@mails.tsinghua.edu.cn'
        }

    def test_no_content_case(self):
        self.assertEqual(register_params_check(None), ('username', False))

    def test_base_case(self):
        case = self.base_case()
        self.assertEqual(register_params_check(case), ('ok', True))

    def test_username_edge_case(self):
        case = self.base_case()
        case['username'] = 'a' * 6
        self.assertEqual(register_params_check(case), ('ok', True))

        case['username'] = 'a' * 10
        self.assertEqual(register_params_check(case), ('ok', True))

    def test_username_too_long_or_too_short(self):
        case = self.base_case()
        case['username'] = 'a' * 5
        self.assertEqual(register_params_check(case), ('username', False))

        case = self.base_case()
        case['username'] = 'a' * 11
        self.assertEqual(register_params_check(case), ('username', False))

    def test_no_username_or_wrong_type_case(self):
        case = self.base_case()
        del case['username']
        self.assertEqual(register_params_check(case), ('username', False))

        case = self.base_case()
        case['username'] = 10
        self.assertEqual(register_params_check(case), ('username', False))

    def test_password_edge_length_case(self):
        case = self.base_case()
        case['password'] = '1' * 2 + 'a' * 2 + 'A' * 2
        self.assertEqual(register_params_check(case), ('ok', True))

        case['password'] = '1' * 6 + 'a' * 6 + 'A' * 6
        self.assertEqual(register_params_check(case), ('ok', True))

    def test_no_password_or_wrong_type_case(self):
        case = self.base_case()
        del case['password']
        self.assertEqual(register_params_check(case), ('password', False))

        case = self.base_case()
        case['password'] = 123
        self.assertEqual(register_params_check(case), ('password', False))

    def test_password_no_num_case(self):
        case = self.base_case()
        case['password'] = 'abABabAB'
        self.assertEqual(register_params_check(case), ('password', False))

    def test_password_no_upper_case(self):
        case = self.base_case()
        case['password'] = 'abc123abc'
        self.assertEqual(register_params_check(case), ('password', False))

    def test_password_no_lower_case(self):
        case = self.base_case()
        case['password'] = 'ABC123ANC'
        self.assertEqual(register_params_check(case), ('password', False))

    def test_password_invalid_character(self):
        case = self.base_case()
        case['password'] = 'ABCabc123_'
        self.assertEqual(register_params_check(case), ('password', False))

    def test_password_too_long_or_too_short_case(self):
        case = self.base_case()
        case['password'] = '1Aa'
        self.assertEqual(register_params_check(case), ('password', False))

        case = self.base_case()
        case['password'] = '1' * 10 + 'a' * 10 + 'A' * 10
        self.assertEqual(register_params_check(case), ('password', False))

    def test_no_nickname_or_wrong_type(self):
        case = self.base_case()
        del case['nickname']
        self.assertEqual(register_params_check(case), ('nickname', False))

        case = self.base_case()
        case['nickname'] = 10
        self.assertEqual(register_params_check(case), ('nickname', False))

    def test_nickname_edge_length_case(self):
        case = self.base_case()
        case['nickname'] = 'a' * 2
        self.assertEqual(register_params_check(case), ('ok', True))

        case = self.base_case()
        case['nickname'] = 'a' * 8
        self.assertEqual(register_params_check(case), ('ok', True))

    def test_nickname_too_long_or_too_short_case(self):
        case = self.base_case()
        case['nickname'] = 'a'
        self.assertEqual(register_params_check(case), ('nickname', False))

        case = self.base_case()
        case['nickname'] = 'a' * 9
        self.assertEqual(register_params_check(case), ('nickname', False))

    def test_no_document_number_or_wrong_type(self):
        case = self.base_case()
        del case['document_number']
        self.assertEqual(register_params_check(case), ('document_number', False))

        case = self.base_case()
        case['document_number'] = int(case['document_number'])
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_wrong_length(self):
        case = self.base_case()
        case['document_number'] = '14020219990126403'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_address_not_number(self):
        case = self.base_case()
        case['document_number'] = '14020X199901264034'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_birthday_not_number(self):
        case = self.base_case()
        case['document_number'] = '1402021999012X4034'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_order_not_number(self):
        case = self.base_case()
        case['document_number'] = '1402021999012640X4'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_02_29(self):
        case = self.base_case()
        case['document_number'] = '140202199902294032'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_invalid_date(self):
        case = self.base_case()
        case['document_number'] = '140202199913254034'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_wrong_check_code(self):
        case = self.base_case()
        case['document_number'] = '14020219990126403X'
        self.assertEqual(register_params_check(case), ('document_number', False))

        for i in range(10):
            if i == 4:
                continue
            case = self.base_case()
            case['document_number'] = '14020219990126403' + str(i)
            self.assertEqual(register_params_check(case), ('document_number', False))

    def test_document_number_less_than_18(self):
        case = self.base_case()
        case['document_number'] = '140202200002294032'
        self.assertEqual(register_params_check(case), ('ok', True))

        case = self.base_case()
        case['document_number'] = '140202201501264034'
        self.assertEqual(register_params_check(case), ('document_number', False))

    def test_no_mobile_or_wrong_type(self):
        case = self.base_case()
        del case['mobile']
        self.assertEqual(register_params_check(case), ('mobile', False))

        case = self.base_case()
        case['mobile'] = '15801266030'
        self.assertEqual(register_params_check(case), ('mobile', False))

    def test_wrong_mobile_length_case(self):
        case = self.base_case()
        case['mobile'] = 1580126603
        self.assertEqual(register_params_check(case), ('mobile', False))

        case['mobile'] = 158012660301
        self.assertEqual(register_params_check(case), ('mobile', False))

    def test_no_email_or_wrong_type(self):
        case = self.base_case()
        del case['email']
        self.assertEqual(register_params_check(case), ('email', False))

        case = self.base_case()
        case['email'] = 1515151515
        self.assertEqual(register_params_check(case), ('email', False))

    def test_email_wrong_at_number(self):
        case = self.base_case()
        case['email'] = 'liqi17@mails@tsinghua.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))

        case = self.base_case()
        case['email'] = 'liqi17.mails.tsinghua.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))


    def test_inhost_invalid_character(self):
        case = self.base_case()
        case['email'] = 'ijk123^@tsinghua.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_inhost_too_long(self):
        case = self.base_case()
        case['email'] = 'a' * 64 + '@tsinghua.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_too_long(self):
        case = self.base_case()
        case['email'] = 'liqi17@' + 'a' * 63 + '.cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_no_dot(self):
        case = self.base_case()
        case['email'] = 'liqi17@cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_dot_with_no_content(self):
        case = self.base_case()
        case['email'] = 'liqi17@.cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_invalid_character(self):
        case = self.base_case()
        case['email'] = 'liqi17@mails^.tsinghua.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_pure_number_in_last(self):
        case = self.base_case()
        case['email'] = 'liqi17@mails.tsinghua.edu.127'
        self.assertEqual(register_params_check(case), ('email', False))

    def test_host_hypen(self):
        case = self.base_case()
        case['email'] = 'liqi17@mails.thu-pku.edu.cn'
        self.assertEqual(register_params_check(case), ('ok', True))

        case = self.base_case()
        case['email'] = 'liqi17@mails.thu-.pku.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))

        case = self.base_case()
        case['email'] = 'liqi17@mails.thu.-pku.edu.cn'
        self.assertEqual(register_params_check(case), ('email', False))


if __name__ == '__main__':
    unittest.main()
