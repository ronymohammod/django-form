from django.db import models



class BlogModel(models.Model):
    title=models.CharField(max_length=50,null=True)
    content=models.TextField(null=True)
    author=models.CharField(max_length=100,null=True)
    blog_image=models.ImageField(upload_to='media/blog_image',null=True)
    publish_date=models.DateField(auto_now_add=True,null=True)



 
    def __str__(self):
        return f'{self.title}-{self.author_name}'



class CourseModel(models.Model):
    CAGETORY_CHOICE=[
        ('CSE','CSE'),
        ('EEE','EEE'),
        ('CIVIL','CIVIL'),
    ]
    course_name =models.CharField(max_length=100,null=True)
    description =models.TextField(null=True)
    category =models.CharField(choices=CAGETORY_CHOICE,max_length=100,null=True)
    course_image =models.ImageField(upload_to='media/course_image',null=True)
    course_fee =models.CharField(max_length=100,null=True)



    def __str__(self):
        return f'{self.course_name}-{self.category}'



