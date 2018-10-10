from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.http import HttpResponse

from .forms import EmployeeForm
from .models import Employee

# # @login_required
# def main(request):
#     # This is for display the Home Page
#     return render(request, 'main.html')

def main(request):
   template = loader.get_template('main.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

def about(request):
   template = loader.get_template('about.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

def contact(request):
   template = loader.get_template('contact.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

# @login_required
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


# @login_required
def show(request):
    # Display all obj
    # employees = Employee.objects.all()

    # by ordering
    employees = Employee.objects.order_by('eid')
    return render(request, "show.html", {'employees': employees})

# @login_required
def edit(request, eid):
    employee = Employee.objects.get(eid=eid)
    return render(request, 'edit.html', {'employee': employee})

# @login_required
def update(request, eid):
    employee = Employee.objects.get(eid=eid)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

# @login_required
def destroy(request, eid):
    employee = Employee.objects.get(eid=eid)
    employee.delete()
    return redirect("/show")


# For Searching
# @login_required
def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Employee.objects.filter(Q(eid__icontains =srch) |
                                            Q(ename__icontains =srch)|
                                            Q(eemail__icontains=srch) |
                                            Q(econtact__icontains=srch)
                                            )
            if match:
                return render(request, 'show.html', {'employees': match})
            else:
                messages.error(request, 'No Result' )
        else:
            return HttpResponseRedirect('/search/')

        return render(request, 'show.html')


