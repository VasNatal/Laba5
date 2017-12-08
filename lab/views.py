from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_view(request):
    return render(request, 'base.html')

def function_view1(request):
    return render(request, 'for_first_part.html', {'my_variable':'Первая переменная'})

def function_view2(request):
    return render(request, 'for_first_part.html', {'my_variable':'Вторая переменная'})

def function_view3(request):
    return render(request, 'for_first_part.html', {'dict':{'inner':'Словарь'}})

def function_view4(request):
    return render(request, 'for_first_part.html', {'list':{'1', '2'}})

class BooksView(View):
    def get(self, request):
        data = {
            'books':[
                {'title': 'Первая книга', 'id':1},
                {'title': 'Вторая книга', 'id': 2},
                {'title': 'Третья книга', 'id': 3}
            ]
        }
        return render(request, 'for_second_part.html', data)

class BookView(View):
    def get(self, request, id):
        data = {
            'book':{
                'id':id
            }
        }
        return render(request, 'book.html', data)