#!/usr/bin/env python
from __future__ import print_function
from subprocess import Popen, call, PIPE, check_output
from time import sleep
import os
import cx_Oracle


# Check if image exists in VNP Database
def image_exist(cur, filename):
    try:
        cur.execute("SELECT FILE_NAME, FOLDER FROM prepaid.subscribers_images WHERE FILE_NAME='" + filename + "'")
    except cx_Oracle.DatabaseError:
        print("Exception: "+filename)
        f = open('/root/scripts/arch.log', 'a')
        f.write('Exception: '+filename)
        f.close()
        return True
    rel = cur.fetchall()
    if rel:
        return True
    else:
        return False


# Move unknown image to archive folder
def archive_image(folder, filename):
    # move filename to archive folder
    f = open('/root/scripts/arch.log', 'a')
    if not os.path.exists('/backup_7200/IMG_HIST/'+folder):
        os.makedirs('/backup_7200/IMG_HIST/'+folder)
    f.write('/image_files/'+folder+'/'+filename+'\n')
    call(['mv', '/image_files/'+folder+'/'+filename, '/backup_7200/IMG_HIST/'+folder], stdout=f, stderr=f)
    f.close()


# images process:
def image_process(folder):
    folder_path = "/image_files/" + folder
    f = open("/tmp/"+folder, 'w')
    call(["ls", "-1", folder_path], stdout=f)
    f.close()
    f = open('/tmp/'+folder, 'r')
    con = cx_Oracle.connect('subadmin/tt#tinhcuoc#2710@10.149.34.74/VNP')
    cur = con.cursor()
    for filename in f.xreadlines():
        filename = filename.rstrip('\n')
        # delay 1 seconds
        sleep(1)
        if not image_exist(cur, filename):
            archive_image(folder, filename)
    cur.close()
    con.close()
    f.close()


if __name__ == '__main__':
    # list all folder:
    # folders: list to store all folders
    for y in range(2012, 2017):
        p1 = Popen(['ls', '-1', '/image_files'], stdout=PIPE)
        folders = check_output(['grep', str(y)], stdin=p1.stdout).splitlines()
        while folders:
            print(folders[0])
            image_process(folders[0])
            folders.pop(0)

    # for y in range(2017, 2018):
    #     for m in range(1, 12):
    #         for d in range(1, 31):
    #             folders.append(str(m)+str(y)+"/"+str(d))
