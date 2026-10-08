from django.shortcuts import render,redirect,get_object_or_404
from form_app.forms import *
from form_app.models import *



def wellcome_view(request):
    return render(request,'wellcome.html')

def blog_list(request):
    blog_data = BlogModel.objects.all()
    context ={
        'blog_data' : blog_data
    }

    return render (request,'blog-list.html',context)


def add_blog(request):

    form_data = BlogForm()
    if request.method == 'POST':
        form_data = BlogForm(request.POST,request.FILES)
        if form_data.is_valid():
           form_data.save()  
           return redirect('blog_list')

    context = {
           'form_data':form_data
    }
    return render(request,'add-blog.html',context)





def update_blog(request,blog_id):
    blog_data = get_object_or_404(BlogModel, id=blog_id)

    form_data = BlogForm(instance=blog_data)
    if request.method == 'POST':
        form_data = BlogForm(request.POST,request.FILES, instance=blog_data)
        if form_data.is_valid():
           form_data.save()  
           return redirect('blog_list')

    context = {
        'form_data':form_data
    }
    return render(request,'update-blog.html',context)









def add_course(request):
    form_data = CourseForm()

    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES)

        if form_data.is_valid():
            form_data.save()
            return redirect('course_list')

    context = {
        'form_data': form_data
    }

    return render(request, 'add-course.html', context)






def course_list(request):
       course_data = CourseModel.objects.all()
       context ={
            'course_data' : course_data
        }

       return render(request,'course-list.html',context)



def update_course(request, u_id):
    course_data = get_object_or_404(CourseModel, id=u_id)
    form_data = CourseForm(instance=course_data)

    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES, instance=course_data )

        if form_data.is_valid():
            form_data.save()
            return redirect('course_list')

    context = {
        'form_data': form_data
    }

    return render(request, 'update_course.html', context)


