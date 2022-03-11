from django.db import models
import re
import bcrypt
from datetime import datetime
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(postData['password']) < 8:
            errors['password'] = "Password cannot be less than 8 characters."
        elif postData['password'] != postData['password']:
            errors['password'] = "Passwords do not match."
        if len(postData['email']) < 1:
            errors['email'] = "Email address cannot be blank."
        elif not email_regex.match(postData['email']):
            errors['email'] = "Please enter a valid email address."
        elif check:
            errors['email'] = "Email address is already registered."
        return errors
    
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Invalid Email format"
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User not found"
        if len(postData['password']) == 0:
            errors['password'] = "Password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['email'] = "Email and password do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

class RoundManager(models.Manager):
    def round_validator(self, postData):
        errors = {}
        if len(postData['date_played']) < 1:
            errors['date_played'] = "Please enter a date played."
        if len(postData['course_name']) < 1:
            errors['course_name'] = "Please enter a course name."
        if len(postData['course_location']) < 1:
            errors['course_location'] = "Please enter a course location."
        if len(postData['course_par']) < 1:
            errors['course_par'] = "Please enter a par for the course."
        if len(postData['course_score']) < 1:
            errors['course_score'] = "Please enter a score for the round."
        return errors

class Rounds(models.Model):
    date_played = models.DateField()
    course_name = models.CharField(max_length=255)
    course_location = models.CharField(max_length=255)
    course_par = models.IntegerField()
    course_score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = RoundManager()

class Instruction_choiceManager(models.Manager):
    def instructor_validator(self, postData):
        errors = {}   

        if len(postData['date_added']) < 1:
            errors['date_added'] = "Please select a date."
        if len(postData['instructor']) < 1:
            errors['instructor'] = "Please select an instructor."
        if len(postData['instructor_topic']) < 1:
            errors['instructor_topic'] = "Please select an topic."
        return errors

class Instruction_choice(models.Model):
    instructor = models.CharField(max_length=255)
    instructor_topic = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = Instruction_choiceManager()
