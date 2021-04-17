from django.shortcuts import render

# Create your views here.
def main_page(request):
    data = {
        'cars':['BMW','Toyota','Audi','Mercedes'],
        'phone':{
            'name':'iphone',
            'color':'white',
            'memory':'512 GB',
        }
    }
    countries = {
        'Russia':{
            'president':'vladimir putin',
            'forma_pravleniya':'Демократическое государство с республиканской формой правления',
            'premier':'Mikhail Mishustin',
            'ministr_oborony':'Sergey Shoigu', 
        },
        'Kazakhstan':{
                    'president':'Kasym-Zhomart Tokayev',
                    'forma_pravleniya':'Унитарная,светская республика',
                    'premier':'Askar Mamin',
                    'ministr_oborony':'Nurlan Ermekbayev',
        },
        'USA':{
            'president':'Joseph Baiden',
            'forma_pravleniya':'Федеративно-президенсткая форма правления',
            'Vice-president':'Kamala Harris',
            'ministr_oborony':'Lloyd ostin',
        },
    }
    return render(request, 'main.html',data)

def cars(request):
    data = {
        'cars':['BMW','Toyota','Audi','Mercedes'],
        'carswimg':[
            {
            'img':'image\cars\Toyota.png',
            'name':'Toyota'
            },
            {
            'img':'image\cars\BMW.jpg',
            'name':'BMW'
            },
            {
            'img':'image\cars\honda.jpg',
            'name':'Honda'
            }
            ]
    }

    return render(request,'cars.html',data)
