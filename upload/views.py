from django.shortcuts import render, redirect
from django.db import models
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name= fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


"""Using Generic Class Based Views"""

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    fields = ('title', 'author', 'pdf', 'cover')
    success_url = reverse_lazy('book_list')
    template_name = 'upload_book.html'