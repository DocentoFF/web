from django.contrib import admin
# from django.http import HttpResponseRedirect
from django import forms
# from django_ckeditor_5.widgets import CKEditor5Widget
# from django.db import models

# from ckeditor.fields import RichTextField
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import AuthAccess, SP, GAccess, CourseTable, CourseName, BotTable, ChatTable, \
    LLog, StatusFlag, RFS, TypeSTR, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ()


class CourseNameAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["QorDelay"].required = False

    class Meta:
        model = CourseName
        fields = '__all__'
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="comment"
            )
        }


class PostAdmin(admin.ModelAdmin):
    form = CourseNameAdminForm


admin.site.register(CourseName, PostAdmin)


class AuthAccessAdmin(admin.ModelAdmin):
    list_display = ('login', 'pass_w', 'l_name', 'f_name', 'g_access')


admin.site.register(AuthAccess, AuthAccessAdmin)


class SPAdmin(admin.ModelAdmin):
    list_display = ('StudProgramName', 'g_access')


admin.site.register(SP, SPAdmin)


class GAccessAdmin(admin.ModelAdmin):
    pass


admin.site.register(GAccess, GAccessAdmin)


class CourseTableAdmin(admin.ModelAdmin):
    list_display = ('CourseName', 'CourseFolder', 'Maker', 'StudProgram')


admin.site.register(CourseTable, CourseTableAdmin)


# class CourseNameAdmin(admin.ModelAdmin):
#    list_display = ('type_STR', 'QorDelay')


# admin.site.register(CourseName, CourseNameAdmin)


class TypeSTRAdmin(admin.ModelAdmin):
    pass


admin.site.register(TypeSTR, TypeSTRAdmin)


class BotTableAdmin(admin.ModelAdmin):
    list_display = ('NameBot', 'IDBot', 'g_access', 'BotLock')


admin.site.register(BotTable, BotTableAdmin)


class ChatTableAdmin(admin.ModelAdmin):
    list_display = ('NameChat', 'IDChat', 'g_access', 'ChatLock')


admin.site.register(ChatTable, ChatTableAdmin)


class StatusFlagAdmin(admin.ModelAdmin):
    pass


admin.site.register(StatusFlag, StatusFlagAdmin)


class LLogAdmin(admin.ModelAdmin):
    list_display = ('NameProcess', 'StatusFlag', 'IDBot', 'IDChat', 'CourseName')


admin.site.register(LLog, LLogAdmin)

'''

LLog

RFS


'''
