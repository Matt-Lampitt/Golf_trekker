from django.shortcuts import render, redirect
from .models import *
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_rounds': Rounds.objects.all(),
        'all_instruction': Instruction_choice.objects.all()
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
        request.session['user_id'] = new_user.id
        return redirect('/login_success')
    return redirect('/')

def member_login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('login_success')
    return redirect('/home.html')

def member_logout(request):
    request.session.flush()
    return redirect('/')

def login_success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_rounds': Rounds.objects.all()
    }
    return render(request, 'home.html', context)

#rounds.objects.filter().first() saved the day to at least get something on screen!
def rounds(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_rounds': Rounds.objects.all(),
    }
    return render(request, 'rounds.html', context)

def one_round(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'one_round': Rounds.objects.one_round[0],
    }
    return render(request, 'rounds.html', context)

def post_round(request):
    if request.method == 'POST':
        errors = Rounds.objects.round_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('rounds')
        rounds = Rounds.objects.create(
            date_played = request.POST['date_played'],
            course_name = request.POST['course_name'],
            course_par = request.POST['course_par'],
            course_score = request.POST['course_score'],
            course_location = request.POST['course_location']
        )
        this_user = User.objects.filter(id=request.session['user_id'])
        print(request.POST)
        return redirect('round_success')
    return render(request,'post_round.html')
        
def round_success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_rounds': Rounds.objects.all()
    }
    return render(request, 'rounds.html', context)

def instruction(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_instruction': Instruction_choice.objects.all()
    }
    return render(request, 'instruction.html', context)

def add_instruction(request):
    if request.method == 'POST':
        instruction_choice = Instruction_choice.objects.create(
        instructor = request.POST['instructor'],
        instructor_topic = request.POST['instructor_topic'],
        )
        this_user = User.objects.filter(id=request.session['user_id'])
        print(request.POST)
        return redirect('instruction_success')
    return render(request,'add_instruction.html')

def instruction_success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'all_instruction': Instruction_choice.objects.all()
    }
    return render(request, 'instruction.html', context)

