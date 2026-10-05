from django.urls import path
from form_app.views import *


urlpatterns = [
     path('blog_list/', blog_list, name='blog_list'),
     path('add_blog/', add_blog, name='add_blog'),
     path('wellcome/', wellcome_view, name='wellcome_view'),
     path('update/<str:blog_id>/',update_blog, name='update_blog'),




path('add_course/', add_course, name='add_course'),
path('course_list/', course_list, name='course_list'),
path('update_course/<int:u_id>/', update_course, name='update_course'),



]