from django.db import models

# Create your models here.

class category(models.Model):
    nameOfCategory=models.CharField(max_length=280,default="",blank=True,null=True)
    def __str__(self):
        return self.nameOfCategory

    
class signupform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    tot_que = models.PositiveIntegerField(default=0)
    right = models.PositiveIntegerField(default=0)
    wrong = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    exam_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    

class question(models.Model):
    question=models.TextField()
    option1=models.CharField("Worng Answer 1",max_length=280,default="",blank=True,null=True)
    option2=models.CharField("Worng Answer 2",max_length=280,default="",blank=True,null=True)
    option3=models.CharField("Worng Answer 3",max_length=280,default="",blank=True,null=True)
    option4=models.CharField("Worng Answer 4",max_length=280,default="",blank=True,null=True)
    ans=models.CharField("Answer",max_length=280,default="",blank=True)
    categoryName=models.ForeignKey(category, on_delete=models.CASCADE, null=True, default="")
    owner=models.ForeignKey(signupform, on_delete=models.CASCADE, null=True, default="")

    def __str__(self):
        return self.question
        
        
class registerform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

