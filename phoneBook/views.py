from django.http import HttpResponse
from django.shortcuts import redirect, render

from phoneBook.data import autoIncrementID, database, sort, search_result_data
from phoneBook.user import User
from .forms import UserForm


def phone_book(request):
    return render(request, 'phoneBook/index.html', {
        'users': database
    })


def add_user(request):
    return render(request, 'phoneBook/add-user.html')


def add_user_form_post(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            database.append(
                User(
                    autoIncrementID.increment(),
                    form.cleaned_data['first_name'],
                    form.cleaned_data['last_name'],
                    form.cleaned_data['phone_number'],
                    form.cleaned_data['email']
                ))
            return redirect('phone_book')

    return render(request, 'phoneBook/index.html')


def sort_users(request, attr):
    if sort.currentSortOrder == 1:
        sort.bubble_sort_descending(database, attr)
        sort.currentSortOrder = -1
    elif sort.currentSortOrder == -1:
        sort.bubble_sort_ascending(database, attr)
        sort.currentSortOrder = 1

    return redirect('phone_book')


def remove_user(request, num):
    database.pop(num)
    return redirect('phone_book')


def search_for_user(request):

    if request.method == 'GET':
        search_term = request.GET['search_box']
        print(search_term)
        search_result_data.clear()

        for user in database:
            if (user.first_name == search_term or
                user.last_name == search_term or
                user.phone_number == search_term or
                    user.email == search_term):
                search_result_data.append(user)

    return render(request, 'phoneBook/search-result.html', {
        'users': search_result_data
    })
