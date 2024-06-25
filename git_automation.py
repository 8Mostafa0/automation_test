import os
import random
import shutil
from datetime import datetime

def copy_file():
    copy_folder('./Newfolder','./Newfolder1')


def rem_file():
    os.remove('./Newfolder1/1test1.txt')
    os.remove('./Newfolder1/test.txt')
    os.remove('./Newfolder1/tests.txt')
    os.rmdir('./Newfolder1')

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
    words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]

    # Generate a random sentence
    sentence = " ".join(random.sample(words, random.randint(5, 6)))
    return sentence


def changebranch(opt):
    bch = "main"
    if opt:
        bch = "optimize"
    print("branch set to  => ",bch)
    if(opt):
        os.system('cmd /c "git branch optimize"')
        os.system('cmd /c "git checkout optimize"')
    else:
        os.system('cmd /c "git checkout main"')

def today_commits(number):
    i = 0
    print("Commits : ",number)
    isLastMoveDelete = True
    branch = False
    while( i < number):
        print("Commit =>",i)
        i+=1
        if isLastMoveDelete == True:
            copy_file()
        else:
            rem_file()
        isLastMoveDelete = not isLastMoveDelete
        msg = generate_commit_message()
        push_commit(msg)

        if i % 2:
            changebranch(branch)


def main():
    date = datetime.now()
    while True:
        today  = datetime.now()
        if(today == date):
            print(today)
            date = datetime.now().replace(day=datetime.now().day+1)
            num = random.randint(10,20)
            today_commits(num)
    
if __name__ == '__main__':
    main()



