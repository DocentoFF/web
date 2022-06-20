from django.db import models
from django.utils import timezone
from django.conf import settings

from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models

from ckeditor.fields import RichTextField


class Post(models.Model):
    content = RichTextField()

class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    text = CKEditor5Field('Text', config_name='extends')

class AuthAccess(models.Model):
    login = models.CharField(max_length=50)
    pass_w = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    g_access = models.ForeignKey('GAccess', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.l_name


class SP(models.Model):
    StudProgramName = models.CharField(max_length=100)
    g_access = models.ForeignKey('GAccess', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.StudProgramName


class GAccess(models.Model):
    G_access_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.G_access_Name


class CourseTable (models.Model):
    CourseName = models.CharField(max_length=100)
    CourseFolder = models.CharField(max_length=100, null=True)
    Maker = models.CharField(max_length=50)
    StudProgram = models.ForeignKey('SP', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.CourseName


class TypeSTR(models.Model):
    type_STR = models.CharField(max_length=50)

    def __str__(self):
        return self.type_STR


class CourseName(models.Model):
    type_STR = models.ForeignKey('TypeSTR', on_delete=models.SET_NULL, null=True)
    QorDelay = models.TextField(max_length=4000)


class BotTable(models.Model):
    NameBot = models.CharField(max_length=100)
    IDBot = models.CharField(max_length=100)
    g_access = models.ForeignKey('GAccess', on_delete=models.SET_NULL, null=True)
    BotLock = models.BooleanField

    def __str__(self):
        return self.NameBot


class ChatTable(models.Model):
    NameChat = models.CharField(max_length=100)
    IDChat = models.CharField(max_length=100)
    g_access = models.ForeignKey('GAccess', on_delete=models.SET_NULL, null=True)
    ChatLock = models.BooleanField

    def __str__(self):
        return self.NameChat


class LLog(models.Model):
    NameProcess = models.CharField(max_length=100)
    # Step = models.PositiveSmallIntegerField
    StatusFlag = models.ForeignKey('StatusFlag', on_delete=models.SET_NULL, null=True)
    IDBot = models.ForeignKey('BotTable', on_delete=models.SET_NULL, null=True)
    IDChat = models.ForeignKey('ChatTable', on_delete=models.SET_NULL, null=True)
    CourseName = models.ForeignKey('CourseTable', on_delete=models.SET_NULL, null=True)
    Started = models.DateTimeField
    Stopped = models.DateTimeField


class StatusFlag(models.Model):
    status_flag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_flag_name


class RFS(models.Model):
    NameProcess = models.CharField(max_length=100)
    IDBot = models.CharField(max_length=100)
    IDChat = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=100)
    CourseFolder = models.FilePathField
    Q_step = models.PositiveSmallIntegerField
    QorDelay = models.CharField(max_length=4000)


class TEMPTest(models.Model):
    NameProcess = models.CharField(max_length=100)
    IDBot = models.CharField(max_length=100)
    IDChat = models.CharField(max_length=100)
    CourseFolder = models.CharField(max_length=100)