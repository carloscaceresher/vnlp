from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator

def Home(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request,'index.html', {'posts':post})

def General(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'General'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            categoria = Categoria.objects.get(nombre = 'General'),
        ).distinct()

    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request,'general.html', {'posts':post})

def Villena(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Villena'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            categoria = Categoria.objects.get(nombre = 'Villena')
        ).distinct()

    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request,'villena.html', {'posts':post})

def Otros(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Otros'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            categoria = Categoria.objects.get(nombre = 'Otros')
        ).distinct()

    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request,'otros.html', {'posts':post})

def Nacional(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Nacional'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            categoria = Categoria.objects.get(nombre = 'Nacional')
        ).distinct()

    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    
    return render(request,'nacional.html', {'posts':post})

def DetallePost(request,slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detalle_post':post})
