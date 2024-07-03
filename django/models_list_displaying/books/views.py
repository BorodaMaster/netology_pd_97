from django.shortcuts import render
from django.db.models import F

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books_objects = Book.objects.all()
    books = [element for element in books_objects.values()]

    context = {'books': books}

    return render(request, template, context)


def books_view_filtered(request, pub_date):
    template = 'books/books_list_filtering.html'

    # Get books by date
    books_objects = Book.objects.filter(pub_date__exact=pub_date)
    books = [element for element in books_objects.values()]

    # Get previews and next dates
    previous_dates = Book.objects.filter(pub_date__lt=pub_date).order_by("-pub_date").values("pub_date")
    next_dates = Book.objects.filter(pub_date__gt=pub_date).order_by("pub_date").values("pub_date")

    if previous_dates:
        previous_date = previous_dates[0]["pub_date"].strftime('%Y-%m-%d')
    else:
        previous_date = ""
    if next_dates:
        next_date = next_dates[0]["pub_date"].strftime('%Y-%m-%d')
    else:
        next_date = ""

    context = {
        'books': books,
        "previous_date": previous_date,
        "next_date": next_date,
    }

    return render(request, template, context)
