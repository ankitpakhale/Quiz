from re import U
from unicodedata import name
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

# def signin(request):
#     return render(request,'signin.html')

def signin(request):
    # print("01 signin method")
    if request.method=='POST':
        # print("Inside signin post method")
        username=request.POST['username']
        password1=request.POST['your_pass']
        try:
            user=signupform.objects.get(name=username)
            if user.password==password1:
                print("Password matched")
                request.session['username'] = request.POST['username']
                print("Redirecting to HOME")
                return redirect('home')
            else:
                print("Invalid Credentials")
                messages.info(request,'Invalid Credentials')
                return render(request,'signin.html', {'msg': 'Invalid password'})
        except:
            print("except condition")
            return render(request,'signin.html', {'msg': 'Invalid username'})
    else:
        # print("Else condition")
        return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        confirm_pwd=request.POST['con_pass']
        if password==confirm_pwd:
            if signupform.objects.filter(name=name).exists():
                messages.info(request,'name Taken')
                # return redirect('signup')
                return render(request,'signup.html', {'msg': 'This Name is already taken'})
            elif signupform.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                # return redirect('signup')
                return render(request,'signup.html', {'msg': 'This Email is already taken'})
            else:
                user=signupform.objects.create(name=name,email=email,password=password)
                user.save()
                print('User Created')
                return redirect("signin")
        else:
            messages.info(request,'Password do not match')
            # return redirect('signup')
            return render(request,'signup.html', {'msg': 'Please enter correct password'})
    else:
        return render(request,'signup.html')

def features(request):
    return render(request,'features.html')

def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')

def questions(request):
    return render(request,'question.html')

def addquestions(request):
    if request.session.has_key('username'):
        cat = category.objects.all()
        if request.method=='POST':
            print("Inside POST method")
            questions=request.POST['question']
            option1=request.POST['option1']
            option2=request.POST['option2']
            option3=request.POST['option3']
            option4=request.POST['option4']
            ans=request.POST['ans']
            categoryName=request.POST['categoryName']
            try:
                categoryName = category.objects.get(nameOfCategory = categoryName)
                owner=signupform.objects.get(name=request.session['username'])
                print("Try block of addquestions function")
                v = question(question = questions,
                            option1 = option1,
                            option2 = option2,
                            option3 = option3,
                            option4 = option4,
                            ans = ans,
                            categoryName = categoryName,
                            owner = owner
                            )
                v.save()
                print("Data saved properly")
                return render(request,'add questions.html', {'msg': 'Your questions are successfully saved', 'cat': cat})
            except:
                return render(request,'add questions.html', {'msg': 'Something went wrong'})
        else:
            print("Else condition")
            return render(request,'add questions.html', {'cat': cat})
    else :
        return redirect('signin')
        
def enter(request):
    if request.POST :
        return redirect('play')
    return render(request,'enter.html')

def addCategory(request):
    if request.POST :
        try:
            catName=request.POST['addCategory']
            c = category(nameOfCategory = catName)
            c.save()
            print("Category saced successfully")
            return redirect('addquestions')
        except:
            return render(request,'addCategory.html')
    return render(request,'addCategory.html')

import plotly.graph_objects as go
from io import BytesIO
import plotly.express as px

def dashboardview(request):
    if request.session.has_key('username'):
        data=signupform.objects.get(name=request.session['username'])
        print(data.right)
        print(data.wrong)
        print(data.score)
        labels = ['Right', 'Wrong', 'Score']
        values = [data.right, data.wrong, data.score]        
        fig = go.Figure(data=[
            go.Pie(
                labels=labels, 
                values=values, 
                hole=.4, 
                title='Graph Based on Quiz Result',
                pull=[0.03, 0.03, 0.2,]
                )])
        fig.show()
        # there will also be same issue as there in play function
        return render(request,'dashboard.html',{'data' : data, 'fig' : fig})
    else :
        return redirect('signin')

def join(request):
    if request.session.has_key('username'):
        print("Inside Join function")
        if request.method=='POST':
            userID = ''
            try:
                userID = signupform.objects.get(name=request.POST['gameId'])
                # print(userID)
                request.session['userID'] = userID
                print(request.session['userID'])
                return redirect('play')
            except:
                return render(request,'join.html', {'msg': 'User Does not exist'})
            
            # userQuestion = question.objects.filter(owner = userID)
            # request.session['userQuestion'] = userQuestion
            # print(userQuestion)            
            # return redirect('play')
        return render(request,'join.html')
    else :
        return redirect('signin')


def randomquiz(request):
    if request.method=='POST':
        print("randomquiz post method")
        cheese_blog=request.POST['categoryName']
        print(cheese_blog)
        # request.session['cheese_blog'] = cheese_blog
        return redirect('play',cheese_blog)
    return render(request,'random quiz.html')

def play(request, cat_name):
    print('inside Play function function')
    if request.session.has_key('username'):
        print('play Play')
        right = 0
        wrong = 0
        ncat = category.objects.get(nameOfCategory=cat_name)
        data = question.objects.filter(categoryName=ncat)
        # data = question.objects.all()
        print(data, 'bdvhkbvsd')
        total_data = question.objects.filter(categoryName=ncat).count()
        if request.POST:
            print('POST condition')
            for d in data :

                val = request.POST["q"+str(d.id)]
                print(val, "this is value")
                if d.ans == val :
                    print(f'\nRight Answer = {d.ans}\n')
                    right +=1
                else :
                    print(f'Wrong Answer..\nRight Answer = {d.ans}\n')
                    wrong +=1
            print(f'Right = {right}, Wrong = {wrong}')
            form = signupform.objects.get(name = request.session['username'])
            form.total_data = total_data
            form.right = right
            form.wrong = wrong
            form.score = right
            form.exam_status = True
            form.save()
            return redirect('dashboardview')
        return render(request,'Quiz.html',{'data':data})
    else:
        print('redirecting ti signin from play function')
        return redirect('signin')



def play1(request):
    print('inside Play function function')
    if request.session.has_key('username'):
        print('play Play')
        right = 0
        wrong = 0
        data = sorted(question.objects.all(),key=lambda x: random.random())
        total_data = question.objects.all().count()
        if request.POST:
            print('POST condition')
            for d in data :
                val = request.POST["q"+str(d.id)]
                print(val)
                if d.ans == val :
                    print(f'\nRight Answer = {d.ans}\n')
                    right +=1
                else :
                    print(f'Wrong Answer..\nRight Answer = {d.ans}\n')
                    wrong +=1
            print(f'Right = {right}, Wrong = {wrong}')
            # form = registerform.objects.get(name = request.session['username'])
            # form.total_data = total_data
            # form.right = right
            # form.wrong = wrong
            # form.score = right
            # form.exam_status = True
            # form.save()
            form = registerform.objects.get(name = request.session['username'])
            # there is a problem of session validation
            # this program wants to save data in registerform table using signupform session
            # which is not posible
            form.total_data = total_data
            form.right = right
            form.wrong = wrong
            form.score = right
            form.exam_status = True
            form.save()
            return redirect('dashboardview')
        return render(request,'Quiz.html',{'data':data})
    else:
        print('redirecting ti signin from play function')
        return redirect('signin')

def createquiz(request):
    return render(request,'create quiz.html')

def result(request):
    return render(request,'result.html')

def myquizes(request):
    return render(request,'my quizes.html')

def details(request):
    return render(request,'details.html')

def home(request):
    print(request.session['username'], " logged in..")
    if request.session.has_key('username'):
        try:
            print("Inside try block of home function")
            right = 0
            wrong = 0
            # obj = sorted(question.objects.all()[:2],key=lambda x: random.random())
            obj = sorted(question.objects.all(),key=lambda x: random.random())
            total_data = question.objects.all().count()
            if request.POST:
                print("inside post method")
                try:
                    for d in obj:
                        val = request.POST.get(str(d.id))
                        print(val)
                        if d.ans == val:
                            print(f'Right Answer..\n')
                            right +=1
                        else :
                            print(f'Wrong Answer..\nRight Answer = {d.ans}\n')
                            wrong +=1
                    print(f'Right = {right}, Wrong = {wrong}')
                    form = registerform.objects.get(username=request.session['username'])
                    form.total = total_data
                    form.right = right
                    form.wrong = wrong
                    form.score = right
                    form.save()
                    return redirect('result')
                except:
                    return render(request,'index.html',{'obj':obj})
            else:
                # return render(request,'index.html',{'obj':obj})
                return render(request,'index.html',{'obj':obj})
        except:
            msg = 'Something went wrong'
            print("Something went wrong in Home page")
            return render(request,'index.html',{'msg1': msg})

    
    return redirect('signin')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if registerform.objects.filter(username=name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif registerform.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')
            else:
                user=registerform.objects.create(username=name,email=email,password=password1,name=first_name)
                user.save()
                print('User Created')
                return redirect("signin")
        else:
            messages.info(request,'Password do not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def signin1(request):
    print("01 signin method")
    if request.method=='POST':
        print("Inside signin post method")
        username=request.POST['your_name']
        password1=request.POST['your_pass']
        user=registerform.objects.get(username=username)
        if user.password==password1:
            print("Password matched")
            request.session['username'] = request.POST['username']
            print("going to join function")
            return redirect('join')
        else:
            print("Invalid Credentials")
            messages.info(request,'Invalid Credentials')
            return redirect('signin')
    else:
        print("Else condition")
        return render(request,'signin.html')

# def result(request):
#     if request.session.has_key('username'):
#         data=registerform.objects.get(username=request.session['username'])
#         return render(request,'result.html',{'data' : data})
#     else :
#         return redirect('signin')

def logout(request):
    print("Inside logout function")
    if request.session.has_key('username'):
        del request.session['username']
        print("user logged out successfully")
        return redirect('signin')
    return redirect('signin')
