from django.http import HttpResponse
from django.shortcuts import redirect, render

from phoneBook.data import autoIncrementID, users
from phoneBook.forms import UserForm
from phoneBook.user import User


def phone_book(request):
    return render(request, 'phoneBook/index.html', {
        'users': users.database
    })


def add_user(request):
    return render(request, 'phoneBook/add-user.html')


def add_user_form_post(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            users.add_user(User(
                autoIncrementID.increment(),
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name'],
                form.cleaned_data['phone_number'],
                form.cleaned_data['email']
            ))
            return redirect('phone_book')

    return render(request, 'phoneBook/index.html')


def sort_users(request, attr):
    users.sort_users(attr)
    return redirect('phone_book')


def remove_user(request, num):
    users.remove_user(num)
    return redirect('phone_book')


def search_for_user(request):

    if request.method == 'GET':
        search_term = request.GET['search_box']

    users.search_for_user(search_term)
    return render(request, 'phoneBook/search-result.html', {
        'users': users.search_result_data
    })
