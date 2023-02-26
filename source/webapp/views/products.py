from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product

from webapp.forms import ProductForm
from webapp.models import CategoryChoice


def products_view(request):
    products = Product.objects.exclude(balance=0).order_by(
        'category', 'name'
    )
    context = {'products': products}
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


def products_add_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={
            'choices': CategoryChoice.choices,
            'form': form
        })

    form = ProductForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'product_add.html', context={
            'choices': CategoryChoice.choices,
            'form': form
        })
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)





# def products_delete_view(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.delete()
#     return redirect('products_view')


# def products_edit_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         context = {
#             'product': product,
#             'categories': Category.objects.all()
#         }
#         return render(request, 'product_edit.html', context=context)
#     product.name = request.POST.get('name')
#     product.category = get_object_or_404(Category, category=request.POST.get('category'))
#     product.description = request.POST.get('description', None)
#     product.coast = request.POST.get('coast')
#     product.image = request.POST.get('image')
#     product.save()
#     return redirect('products_view')
