from django.shortcuts import render
from .models import Book, Author

def main(request):
    return render(request, 'library/main.html')

def books_list(request):
    books = Book.objects.all()
    print(f'this is the list of books {books}')
    return render(request, 'library/books_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    print(f'this is the book details {book}')
    return render(request, 'library/book_detail.html', {'book': book})

def authors_list(request):
    authors = Author.objects.all()
    print(f'this is the list of authors {authors}')
    return render(request, 'library/authors_list.html', {'authors': authors})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    print(f'this is the author details {author}')
    return render(request, 'library/author_detail.html', {'author': author})

