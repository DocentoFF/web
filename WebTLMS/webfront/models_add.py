import os
import sqlite3
from os import path
import subprocess


def add_base_table(name):
    conn = sqlite3.connect(r'WebTLMS/db.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS' + 'webfront_' + name + '( id INT PRIMARY KEY, QorDelay TEXT'
                                                                    ', type_STR TEXT);')
    conn.commit()

    with open('models.py', 'a') as mfile:
        mfile.write('class ' + name + '(models.Model):\n')
        mfile.write("    type_STR = models.ForeignKey('TypeSTR', on_delete=models.SET_NULL, null=True)\n")
        mfile.write('    QorDelay = models.TextField(max_length=4000)\n')

        mfile.write('def __str__(self):')
        mfile.write('    return self.type_STR')

    with open('admin.py', 'a') as afile:
        afile.write('class ' + name + 'Admin(admin.ModelAdmin):\n')
        afile.write("    list_display = ('type_STR', 'QorDelay')\n")
        afile.write('admin.site.register(CourseName, CourseNameAdmin)\n')

    stop_server = os.system("nircmd.exe sendkeypress ctrl+C")
    print("stop out: " %stop_server)

    cd_home_dir = os.system("cd /WebTLMS")
    print("cd out: " %cd_home_dir)

    Rserver = os.system("cd /WebTLMS")
    print("restart out: " %Rserver)
