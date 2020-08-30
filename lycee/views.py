from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.utils.translation import template

from .models import Cursus,Student
from .form import StudentForm, CursusForm
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):

  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)


def detail(request, cursus_id):
  resp = "result for cursus {}".format(cursus_id)
  return HttpResponse(resp)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentUpdateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class CursusCreateView(CreateView):
  # ref au modEle
  model = Cursus
  # ref au formulaire
  form_class = CursusForm
  # le nom du render
  template_name = "lycee/cursus/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

def call_of_roll_student(request):


    return HttpResponse()

def call_of_details_student(request, student_id):


    """return render(request, "lycee/student/detail_student.html", context)"""

def call_list_student(request):



    """return render(request, "lycee/call_of/call_list_student.html", context)"""


def detail_cursus(request, cursus_id):
    # result_list = Student.objects.get(pk=student_id)
    result_list = Student.objects.filter(cursus_id=cursus_id)
    template = loader.get_template("lycee/cursus/detail_cursus.html")
    # context
    context = {'liste': result_list, }
    return HttpResponse(template.render(context, request))

def list_student(request,cursus_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = Student.objects.filter(cursus_id=cursus_id)
    template = loader.get_template("lycee/student/list_student.html")
    # context
    context = {'liste': result_list,}
    return HttpResponse(template.render(context, request))