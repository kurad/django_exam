from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, post_Data):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_Data['first_name']) < 3:
            errors['first_name'] = "Your password must be at least 8 characters"
        if len(post_Data['last_name']) < 3:
            errors['last_name'] = "Your password must be at least 8 characters"
        if len(post_Data['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters"
        if len(post_Data['first_name']) < 2 or len(post_Data['last_name']) < 2:
            errors['name'] = "Your name must be at least 2 characters"
        if not email_checker.match(post_Data['email']):
            errors['email'] = 'Email must be valid'
        if post_Data['password'] != post_Data['confpass']:
            errors['password'] = 'Password and Confirm Password do not match'
        return errors
class JobManager(models.Manager):
    def basic_validator(self, post_Data):
        errors = {}
        if len(post_Data['title']) < 3:
            errors['title'] = "Job title must be at least 3 characters"
        if len(post_Data['description']) < 3:
            errors['description'] = "Description must be at least 3 characters"
        if len(post_Data['location']) < 3:
            errors['location'] = "Location must be at least 3 characters"
        if len(post_Data['location']) == "":
            errors['location'] = "Location cannot be empty"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Category(models.Model):
    cat_name = models.CharField(max_length=50)

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = JobManager()
