import time
import os
import shutil
from threading import Timer
from random import randrange
from datetime import datetime

def copy_file():
    copy_folder('./Newfolder','./Newfolder1')


def rem_file():
    os.remove('./1test.txt')

def copy_folder(src,dst,symlink=False,ignore=None):
    if os.path.exists(dst) == False or os.path.isdir(dst) == False:
        os.mkdir(dst)

    for item in os.listdir(src):
        s = os.path.join(src,item)
        d = os.path.join(dst,item)
        if os.path.isdir(s):
            shutil.copytree(s,d,symlink,ignore)
        else: 
            shutil.copy2(s,d)


def push_commit(commit_message):
    os.system(f'cmd /c "git commit -m \"{commit_message}\""')
    os.system('cmd /c "git push"') 
    os.system('cmd /c "git init"')
    os.system('cmd /c "git add ."')



def generate_commit_message():
    return "Test"


def del_or_add():
    isLastMoveDelete = True
    if isLastMoveDelete == True:
        copy_file()
    else:
        rem_file()
    isLastMoveDelete = not isLastMoveDelete
    msg = generate_commit_message()
    push_commit(msg)



def today_commits(number):
    i = 0
    print(i)
    start = randrange(9)
    date = datetime.now()
    while( i < number):
        i+=1
        if date.hour >= start:
            del_or_add()



def start():
    start_date = datetime.now()
    next_date = start_date.replace(day=start_date.day+1)
    today_commits(1)
         



def main():
    start()
if __name__ == '__main__':
    main()



