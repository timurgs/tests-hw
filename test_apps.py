import unittest
from unittest.mock import patch
from ya_api import CreateFolderYaApi
from secretary_app import *


class TestSecretaryApp(unittest.TestCase):

    def test_people(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            self.assertEqual(people(), 'Геннадий Покемонов')

    def test_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertEqual(shelf(), '2')

    def test_list_(self):
        self.assertEqual(list_(), ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"',
                                   'insurance "10006" "Аристарх Павлов"'])

    def test_add(self):
        with unittest.mock.patch('builtins.input', return_value='3'):
            self.assertEqual(add(), 'Новый документ добавлен!')

    def test_delete(self):
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            self.assertEqual(delete(), 'Документ удален!')

    def test_move(self):
        self.assertEqual(move("11-2", '2'), 'Документ перемещен!')

    def test_add_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='4'):
            self.assertEqual(add_shelf(), 'Новая полка добавлена!')


class TestYandexApi(unittest.TestCase):

    def test_ya_api_1(self):
        ya_request = CreateFolderYaApi('')  # токен
        ya_request.create_folder()
        check_create = ya_request.check_create_folder()
        self.assertEqual(check_create.status_code, 200)

    def test_ya_api_2(self):
        ya_request = CreateFolderYaApi('')
        create = ya_request.create_folder()
        self.assertEqual(create.status_code, 200)

    def test_ya_api_3(self):
        ya_request = CreateFolderYaApi('')
        check_create = ya_request.check_create_folder()
        self.assertEqual(check_create.status_code, 201)
