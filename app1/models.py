from django.db import models

# Create your models here.

class category(models.Model):
    nameOfCategory=models.CharField(max_length=280, blank=True)
    def __str__(self):
        return self.nameOfCategory

class question(models.Model):
    question=models.TextField()
    option1=models.CharField("Worng Answer 1",max_length=280,default="",blank=True,null=True)
    option2=models.CharField("Worng Answer 2",max_length=280,default="",blank=True,null=True)
    option3=models.CharField("Worng Answer 3",max_length=280,default="",blank=True,null=True)
    option4=models.CharField("Worng Answer 4",max_length=280,default="",blank=True,null=True)
    ans=models.CharField("Answer",max_length=280,default="",blank=True)
    
    categoryName=models.ForeignKey(category, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.question
    
    
class registerform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    worng=models.PositiveIntegerField(default=0)
    right=models.PositiveIntegerField(default=0)
    marks=models.FloatField(default=0.0)
    total=models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    exam_status = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
    
class signupform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_pwd=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    