from django.shortcuts import render

# Create your views here.
# 
from django.http import HttpResponse, JsonResponse
from .models import School, Category, Food
import random

def index(request):
    return render(request, "eatwhat/index.html")

def eatwhat(request):
    category = Category.objects.all()
    school = School.objects.all()
    all_food = Food.objects.all()
    count = all_food.count()
    food = []
    num_seq = []
    while len(food) < 4:
        num = random.randint(0, count-1)
        if num not in num_seq:
            num_seq.append(num)
            food.append(all_food[num])

    context={'category':category, 
            'school':school,
            'food':food[0:3],
            'today_food': food[3]
            }
    return render(request, "eatwhat/eatwhat.html", context=context)


def select_food(request):
    if request.method=="POST":
        school = request.POST.get('school')
        category = request.POST.get('category')
        price_from = request.POST.get('from')
        price_to = request.POST.get('to')
        print(school,category,price_from,price_to)
        
        if category == '-1':
            food = Food.objects.filter(school=school, price__range=(price_from, price_to))
        else:
            # category = Category.objects.filter(id=category)
            food = Food.objects.filter(school=school, category=category, price__range=(price_from, price_to))

        count = food.count()
        print(count)
        if count == 0:
            context = {
                'name':"什么都没有",
                'price':"什么都没有",
                'category': "什么都没有",
                'location': "什么都没有",
                'comment': "什么都没有",
            }
        else:
            num = random.randint(0, count-1)
            context = {
                'name':str(food[num].name),
                'price':str(food[num].price),
                'category': str(food[num].category),
                'location': str(food[num].location),
                'comment': str(food[num].comment),
            }
        return JsonResponse(context)

def add_food(request):
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get('name')
        school = request.POST.get('school')
        category= request.POST.get('category')
        price = float(request.POST.get('price'))
        location = request.POST.get('location')
        comment = request.POST.get('comment')

        # food = Food(name=name, school=school, category=category, price=price, location=location, comment=comment)
       
        try:
            food = Food(name=name, price=price, location=location, comment=comment)
            food.category_id = category
            food.school_id = school
            food.save()
        except:
            return HttpResponse("ERROR")
            # raise Exception
        else:
            return HttpResponse("OK")

        # return HttpResponse("OK")