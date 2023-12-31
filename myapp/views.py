from django.shortcuts import render, redirect
from .models import Book

def home(request):
    return redirect('book_list')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})
