from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    data={
        'first_name':'abed Al rahman ',
       'last_name':"Habib",
       'student_id':120210986,
        'address':"Gaza-Palestine",
        'email':"",
        'date_of_birth':date(2003,2,4),
        'university': 'Islamic University of Gaza',
       'faculty': 'Information Technology',
         'major': 'Software Development',
        'github': 'https://github.com/abedahabib23',

    }
    return render(request, 'pages/index.html',data)