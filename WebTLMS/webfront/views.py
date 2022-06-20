from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django.forms
from .models import *
from django.views.generic.list import ListView
import datetime
from .base import *


def index(request):

    bots = BotTable.objects.all() # .values_list('NameBot')
    auth = AuthAccess.objects.all()
    sp = SP.objects.all()
    gaccess = GAccess.objects.all()
    course_table = CourseTable.objects.all()
    course_name = CourseName.objects.all()
    chat = ChatTable.objects.all()
    llog = LLog.objects.all()
    status = StatusFlag.objects.all()
    rfs = RFS.objects.all()
    t_str = TypeSTR.objects.all()
    tttable = TEMPTest.objects.all()
    for bot in bots:
        print(bot.IDBot)
    return render(request,
                  'webfront/index.html', {'bots': bots,
                                          'auth': auth,
                                          'sp': sp,
                                          'gaccess': gaccess,
                                          'course_table': course_table,
                                          'course_name': course_name,
                                          'chat': chat,
                                          'llog': llog,
                                          'status': status,
                                          'rfs': rfs,
                                          't_str': t_str,
                                          'tttable': tttable})

def create(request):
    if request.method == "POST":
        data = TEMPTest()
        data.IDBot = request.POST.get("id_bot")
        data.IDChat = request.POST.get("id_chat")
        data.NameProcess = request.POST.get("NameProcess")
        data.CourseFolder = request.POST.get("CourseFolder")
        data.save()
    return HttpResponseRedirect("/")
