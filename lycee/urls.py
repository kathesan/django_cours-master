from django.conf.urls import url
from . import views
from .views import StudentCreateView, CursusCreateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^cursus/create/$', CursusCreateView.as_view(), name='create_cursus'),
    url(r'^call_of/call_list_student/$', views.detail_student, name='list_student'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail_cursus, name='detail_cursus'),
    url(r'^list/(?P<cursus_id>[0-9]+)$', views.list_student, name='list_student')
]
