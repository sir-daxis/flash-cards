from django.contrib import admin

from .models import Word, Person, Plural, Form, Past, AppUser, WordClass

# Register your models here.
admin.site.register(Word)
admin.site.register(AppUser)
admin.site.register(WordClass)
admin.site.register(Person)
admin.site.register(Plural)
admin.site.register(Form)
admin.site.register(Past)