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

def join(request):
    return render(request,'join.html')

def features(request):
    return render(request,'features.html')

def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')

def questions(request):
    return render(request,'question.html')

def randomquiz(request):
    return render(request,'random quiz.html')

def addquestions1(request):
    # have to work on this function
    # to add ques on db through user side  
    return render(request,'add questions.html')

def addquestions(request):
    print("addquestions")
    if request.method=='POST':
        print("Inside signin post method")
        questions=request.POST['question']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        option4=request.POST['option4']
        ans=request.POST['ans']
        try:
            v = question()
            v.question = questions
            v.option1 = option1
            v.option2 = option2
            v.option3 = option3
            v.option4 = option4
            v.ans = ans
            v.save()
            return render(request,'add questions.html', {'msg': 'Your questions are successfully saved'})
        except:
            return render(request,'add questions.html', {'msg': 'Something went wrong'})

    else:
        print("Else condition")
        return render(request,'add questions.html')

def enter(request):
    if request.POST :
        return redirect('play')
    return render(request,'enter.html')

def dashboardview(request):
    if request.session.has_key('username'):
        data=registerform.objects.get(name=request.session['username'])
        # there will also be same issue as there in play function
        return render(request,'dashboard.html',{'data' : data})
    else :
        return redirect('signin')

def play(request):
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
    print('unknown user')
    if request.session.has_key('username'):
        print('logged in user')
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
        print("You have been logged out")
        return redirect('signin')
    return redirect('signin')
