from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Category


def category_add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'category_add.html')
    category_data = {
        'category': request.POST.get('category'),
        'description': request.POST.get('description', None)
    }
    Category.objects.create(**category_data)
    return redirect('categories_view')


def categories_view(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'categories.html', context=context)


def category_delete_view(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories_view')


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        context = {'category': category}
        return render(request, 'category_edit.html', context=context)
    category.category = request.POST.get('category')
    category.description = request.POST.get('description', None)
    category.save()
    return redirect('categories_view')
