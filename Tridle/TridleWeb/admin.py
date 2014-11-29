from django.contrib import admin
from TridleWeb.models import *

# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
        '''
            Admin View for MyUser
        '''
        list_display = ('nickname',)
        list_filter = ('usertype','permission')
        search_fields = ['nickname']

class LetterAdmin(admin.ModelAdmin):
        '''
            Admin View for Letter
        '''
        list_display = ('title','time','flag','user_from','user_to')
        list_filter = ('time','flag')
        search_fields = ['title','context']

class ProductModelAdmin(admin.ModelAdmin):
        '''
            Admin View for ProductModel
        '''
        list_display = ('name','date','price','published','author')
        list_filter = ('author','published')
        search_fields = ['name','author']

class CommentAdmin(admin.ModelAdmin):
        '''
            Admin View for Comment
        '''
        list_display = ('author','date','produce','starts')
        list_filter = ('author','produce','starts')
        search_fields = ['author','produce','context']

class PicAdmin(admin.ModelAdmin):
        '''
            Admin View for Pic
        '''
        list_display = ('produce',)
        list_filter = ('produce',)
        search_fields = ['produce']

class ShowAdmin(admin.ModelAdmin):
        '''
            Admin View for Show
        '''
        list_display = ('title',)
        search_fields = ['descript','title']

admin.register(Show, ShowAdmin)

admin.register(Pic, PicAdmin)

admin.register(Comment, CommentAdmin)

admin.register(ProductModel, ProductModelAdmin)

admin.register(Letter, LetterAdmin)

admin.register(MyUser, MyUserAdmin)