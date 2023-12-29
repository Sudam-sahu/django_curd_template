from django.shortcuts import redirect, render
from .models import StudentsData

# Create your views here.

def fetching_data(request):
    students = StudentsData.objects.all().order_by('-id')
    return render(request,'fetching_data.html',{'students':students})

def adding_data(request):
    try:
        if request.method == "POST":    #   posting the data into data base table
            StudentsData(
                first_name = request.POST.get('fname'),
                last_name = request.POST.get('lname'),
                course_name = request.POST.get('course'),
                fee = request.POST.get('fee'),
                assignment1 = request.POST.get('Assignment1'),
                assignment2 = request.POST.get('Assignment2'),
                assignment3 = request.POST.get('Assignment3'),
                assignment4 = request.POST.get('Assignment4')
            ).save()
            return redirect('fetching_data')
        else:
            return render(request,'adding_data.html') 
    except:
        return render(request,'adding_data.html')  # getting the empty forms.

def update_data(request,id):
    if request.method == "POST":
        student = StudentsData.objects.get(id=id)
        student.first_name = request.POST.get('fname')
        student.last_name = request.POST.get('lname')
        student.course_name = request.POST.get('course')
        student.fee = request.POST.get('fee')
        student.assignment1 = request.POST.get('Assignment1')
        student.assignment2 = request.POST.get('Assignment2')
        student.assignment3 = request.POST.get('Assignment3')
        student.assignment4 = request.POST.get('Assignment4')
        student.save()
        return redirect('fetching_data')
    else:
        student = StudentsData.objects.get(id=id)
        return render(request,'update_data.html',{'student':student})

def delete_data(request,id):
    student = StudentsData.objects.get(id=id)
    student.delete()
    # student.save() if we used this then delete option comes to last place.
    return redirect('fetching_data')












