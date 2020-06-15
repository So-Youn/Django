from django.shortcuts import render
import random
# Create your views here.
def students(request):
    student = ['윤소윤','김민정','이영주','김현수']
    pick = random.choice(student)
    context = {
        'pick' : pick
    }
    return render(request, 'students.html', context)