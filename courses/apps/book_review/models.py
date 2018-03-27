from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class UserManager(models.Manager):
    def validate_user(self,postData):
        info={
            'status':'good',
            'data':[],
        }
        if len(postData['name'])<5 or not postData['name'].isalpha():
            info['status']='bad'
            info['data'].append('User Name Not Valid!!')
        if not EMAIL_REGEX.match(postData['email']):
            info['status']='bad'
            info['data'].append('Email Not Valid!!')
        if len(postData['password'])<8 or len(postData['cpassword'])<8 or postData['password']!=postData['cpassword']:
            info['status']='bad'
            info['data'].append('Password Not Valid!!')
        if info['status']=='bad':
            return info
        else:
            pw=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())
            user=self.create(name=postData['name'],email=postData['email'],password=pw)
            info['data']=user
            return info

    def validate_login(self,postData):
        info={
            'status':'good',
            'data':'',
        }
        try:
            user=self.get(email=postData['email'])
        except:
            info['status']='bad'
            info['data']='Email or Password is INCORRECT!!'
            return info
        if bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
            info['data']=user
        else:
            info['status']='bad'
            info['data']='Email or Password is INCORRECT!!'
        return info

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Author(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author,related_name='books')

class Review(models.Model):
    rating=models.IntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    book=models.ForeignKey(Book,related_name='reviews')
    user=models.ForeignKey(User,related_name='reviews')
