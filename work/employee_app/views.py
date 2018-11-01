from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import EmployeeForm
from .models import Employee


from django.http import HttpResponse
from django.views.generic import View

from employee_app.utils import render_to_pdf
import datetime

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
    # obje = get_object_or_404(Employee, pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                print("Please Enter the Data ")
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


# @login_required
def show(request):
    # Display all obj
    # employees = Employee.objects.all()

    # by ordering it will display the records which is created recently
    employees = Employee.objects.order_by('-eid')
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
            # eid__icontains --> It's a case-insensitive containment test.
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


# Reference:  https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/
# Generate a PDF document
def generatepdf(request, eid):
    employee = Employee.objects.get(eid = eid)
    pdf = render_to_pdf('pdf.html', {'employee':employee})
    return HttpResponse(pdf, content_type='application/pdf')


# Force download the PDF
# Reference:  https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/
class GeneratePDFForce(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf.html')
        context = {
            "Data": "Employee information",
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")