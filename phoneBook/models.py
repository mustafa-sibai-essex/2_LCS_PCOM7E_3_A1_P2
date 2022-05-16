from django.db import models

# Create your models here.
from phoneBook.sort import Sort
from phoneBook.user import User


class Users():
    database: User = []
    sort: Sort = Sort(-1)
    search_result_data: User = []

    def __init__(self):
        pass

    def add_user_form_post(self, user: User):
        self.database.append(user)

    def sort_users(self, attr):
        if self.sort.currentSortOrder == 1:
            self.sort.bubble_sort_descending(self.database, attr)
            self.sort.currentSortOrder = -1
        elif self.sort.currentSortOrder == -1:
            self.sort.bubble_sort_ascending(self.database, attr)
            self.sort.currentSortOrder = 1

    def remove_user(self, num):
        self.database.pop(num)

    def search_for_user(self, search_term):

        self.search_result_data.clear()

        for user in self.database:
            if (user.first_name == search_term or
                user.last_name == search_term or
                user.phone_number == search_term or
                    user.email == search_term):
                self.search_result_data.append(user)

        return self.search_result_data
