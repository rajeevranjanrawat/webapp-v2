from django.shortcuts import render, redirect
from crud.forms import EmployeeForm
from crud.models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.

def create(request):

    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
           emp = Employee()
           empName = form.cleaned_data['emp_email'].split('@')[0]
           emp.emp_name = empName
           emp.emp_email = form.cleaned_data['emp_email']
           emp.address = form.cleaned_data['address']
           emp.phone = form.cleaned_data['phone']
           emp.save()

           return redirect(index)


            #form.save()         #API CALL

    return render(request, 'crud/create.html', {'form': form})

@login_required(login_url='/sites/signin')   #decorator
def index(request):

    resultSet = Employee.objects.all()
    #resultSet = Employee.objects.filter().order_by('-id')
    #resultSet = Employee.objects.raw("select * from employee where emp_name='rajeev'")

    return render(request, 'crud/index.html', {'data': resultSet})

def update(request, id):

    data = Employee.objects.get(id=id)
    #select * from employee where id = id
    form = EmployeeForm(instance=data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            emp = Employee()
            emp.id = id
            empName = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()

            return redirect(index)

            # form.save()         #API CALL

    return render(request, 'crud/update.html', {'form': form})

def delete(request, id):

    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request, id):

    data = Employee.objects.get(id=id)
    return render(request, 'crud/view.html', {'data': data})


