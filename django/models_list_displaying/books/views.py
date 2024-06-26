from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books_objects = Book.objects.all()
    books = [element for element in books_objects.values()]

    context = {'books': books}

    return render(request, template, context)


def pub_date(request, pub_date):
    template = 'books/books_list.html'

    books_objects = Book.objects.filter(pub_date=pub_date)
    books = [element for element in books_objects.values()]

    print(books)

    paginator = Paginator(books, 25)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'page': page,
        'books': page.object_list
    }

    return render(request, template, context)
