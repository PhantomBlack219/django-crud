from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Author
from .models import Book
from .forms import AuthorForm
from .forms import librosForm

# Create your views here.
def index(request):
    template = loader.get_template('libros/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

#Vista para listar autores
def listarAutores(request):
    lista = Author.objects.all()
    context = {'lista':lista}
    template = loader.get_template('autores/autores.html')
    return HttpResponse(template.render(context,request))

#Vista para listar libros
def listarLibros(request):
    listaB = Book.objects.all()
    context = {'listaB':listaB}
    template = loader.get_template('libros/libros.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def detail_view(request, id):
    context = {}

    context['object'] = Author.objects.get(id = id)

    return render(request,'autores/autor_detalle.html',context)
   
#Vista para ver detalles de un libro
def detail_view_libros(request, id):
    context = {}

    context['object'] = Book.objects.get(id = id)

    return render(request,'libros/libro_detalle.html',context)

#vista para crear autores.
def create_autor(request):

    context = {}

    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form
    return render(request,'autores/create_autor.html', context)

#vista para crear libros.
def create_libros(request):

    context = {}

    form = librosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('libros')
    
    context['form'] = form
    return render(request,'libros/create_libros.html', context)


#vista para actualizar autores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_autor(request,id):

    context = {}

    obj = get_object_or_404(Author, id = id)

    #formulario que contendra la instancia
    form = AuthorForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form

    return render(request, "autores/update_view.html", context)

#vista para actualizar libros
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_libros(request,id):

    context = {}

    obj = get_object_or_404(Book, id = id)

    #formulario que contendra la instancia
    form = librosForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('libros')
    
    context['form'] = form

    return render(request, "libros/update_view.html", context)


#Vista para eliminar un autor
def delete_view(request, id):

    context = {}

    obj = get_object_or_404(Author, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('autores')
    
    return render(request, "autores/delete_view.html", context)

#Vista para eliminar un libro
def delete_view_libros(request, id):

    context = {}

    obj = get_object_or_404(Book, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('libros')
    
    return render(request, "libros/delete_view.html", context)
