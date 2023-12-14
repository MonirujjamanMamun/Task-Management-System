from django.shortcuts import render, redirect
from .forms import AddCategoryForms

# Create your views here.


def add_category(request):
    if request.method == 'POST':
        category_form = AddCategoryForms(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = AddCategoryForms()
    return render(request, 'category.html', {'form': category_form})
