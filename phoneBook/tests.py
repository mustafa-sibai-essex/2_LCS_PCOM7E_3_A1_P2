from django.test import TestCase
from phoneBook.data import users, autoIncrementID
from phoneBook.user import User

# Create your tests here.


class PhoneBookTestCase(TestCase):

    def test_add_new_user(self):

        users.database.clear()
        autoIncrementID.reset()

        users.add_user(User(
            autoIncrementID.increment(),
            'Mustafa',
            'Sibai',
            '0557716033',
            'contact@m-sibai.com'
        ))

        self.assertEqual(users.database[0].id, 0)
        self.assertEqual(users.database[0].first_name, 'Mustafa')
        self.assertEqual(users.database[0].last_name, 'Sibai')
        self.assertEqual(users.database[0].phone_number, '0557716033')
        self.assertEqual(users.database[0].email, 'contact@m-sibai.com')

    def test_remove_user(self):

        users.database.clear()
        autoIncrementID.reset()

        users.add_user(User(
            autoIncrementID.increment(),
            'Anna',
            'Tookey',
            '0557788099',
            'contact@a-tookey.com'
        ))

        users.add_user(User(
            autoIncrementID.increment(),
            'Mustafa',
            'Sibai',
            '0557716033',
            'contact@m-sibai.com'
        ))

        users.add_user(User(
            autoIncrementID.increment(),
            'David',
            'John',
            '05577998899',
            'contact@d-john.com'
        ))

        users.remove_user(1)

        self.assertEqual(len(users.database), 2)

        self.assertEqual(users.database[0].id, 0)
        self.assertEqual(users.database[0].first_name, 'Anna')
        self.assertEqual(users.database[0].last_name, 'Tookey')
        self.assertEqual(users.database[0].phone_number, '0557788099')
        self.assertEqual(users.database[0].email, 'contact@a-tookey.com')

        self.assertEqual(users.database[1].id, 2)
        self.assertEqual(users.database[1].first_name, 'David')
        self.assertEqual(users.database[1].last_name, 'John')
        self.assertEqual(users.database[1].phone_number, '05577998899')
        self.assertEqual(users.database[1].email, 'contact@d-john.com')

    def test_sort_users(self):

        users.database.clear()
        autoIncrementID.reset()

        users.add_user(User(
            autoIncrementID.increment(),
            'Anna',
            'Tookey',
            '0557788099',
            'contact@a-tookey.com'
        ))

        users.add_user(User(
            autoIncrementID.increment(),
            'Mustafa',
            'Sibai',
            '0557716033',
            'contact@m-sibai.com'
        ))

        users.add_user(User(
            autoIncrementID.increment(),
            'David',
            'John',
            '05577998899',
            'contact@d-john.com'
        ))

        users.sort_users('first_name')

        self.assertEqual(len(users.database), 3)

        self.assertEqual(users.database[0].id, 0)
        self.assertEqual(users.database[0].first_name, 'Anna')
        self.assertEqual(users.database[0].last_name, 'Tookey')
        self.assertEqual(users.database[0].phone_number, '0557788099')
        self.assertEqual(users.database[0].email, 'contact@a-tookey.com')

        self.assertEqual(users.database[1].id, 2)
        self.assertEqual(users.database[1].first_name, 'David')
        self.assertEqual(users.database[1].last_name, 'John')
        self.assertEqual(users.database[1].phone_number, '05577998899')
        self.assertEqual(users.database[1].email, 'contact@d-john.com')

        self.assertEqual(users.database[2].id, 1)
        self.assertEqual(users.database[2].first_name, 'Mustafa')
        self.assertEqual(users.database[2].last_name, 'Sibai')
        self.assertEqual(users.database[2].phone_number, '0557716033')
        self.assertEqual(users.database[2].email, 'contact@m-sibai.com')

    def test_search_for_user(self):

        users.database.clear()
        autoIncrementID.reset()

        users.add_user(User(
            0,
            'Anna',
            'Tookey',
            '0557788099',
            'contact@a-tookey.com'
        ))

        users.add_user(User(
            2,
            'David',
            'John',
            '05577998899',
            'contact@d-john.com'
        ))

        users.add_user(User(
            1,
            'Mustafa',
            'Sibai',
            '0557716033',
            'contact@m-sibai.com'
        ))

        self.assertEqual(len(users.database), 3)

        self.assertEqual(users.database[0].id, 0)
        self.assertEqual(users.database[0].first_name, 'Anna')
        self.assertEqual(users.database[0].last_name, 'Tookey')
        self.assertEqual(users.database[0].phone_number, '0557788099')
        self.assertEqual(users.database[0].email, 'contact@a-tookey.com')

        self.assertEqual(users.database[1].id, 2)
        self.assertEqual(users.database[1].first_name, 'David')
        self.assertEqual(users.database[1].last_name, 'John')
        self.assertEqual(users.database[1].phone_number, '05577998899')
        self.assertEqual(users.database[1].email, 'contact@d-john.com')

        self.assertEqual(users.database[2].id, 1)
        self.assertEqual(users.database[2].first_name, 'Mustafa')
        self.assertEqual(users.database[2].last_name, 'Sibai')
        self.assertEqual(users.database[2].phone_number, '0557716033')
        self.assertEqual(users.database[2].email, 'contact@m-sibai.com')

        users.search_for_user('David')
        self.assertEqual(len(users.search_result_data), 1)

        self.assertEqual(users.search_result_data[0].id, 2)
        self.assertEqual(users.search_result_data[0].first_name, 'David')
        self.assertEqual(users.search_result_data[0].last_name, 'John')
        self.assertEqual(users.search_result_data[0].phone_number, '05577998899')
        self.assertEqual(users.search_result_data[0].email, 'contact@d-john.com')
