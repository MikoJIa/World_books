from django.shortcuts import render, HttpResponse

from .models import Author, Book, BookInstance
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'catalog/book_list.html'


def index(request):
    text_head = 'На наше сайте вы можете получить книги в электронном виде'
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instance = BookInstance.objects.all().count()
    # Доступные книги (статус = 'на складе')
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    # Данные об авторах книг
    authors = Author.objects.all()
    num_authors = Author.objects.count()
    # Словарь для передачи данных в шаблон index.html
    context = {
        'books': books,
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'authors': authors,
        'num_authors': num_authors,
        'text_head': text_head
    }
    return render(request, 'catalog/index.html', context)
