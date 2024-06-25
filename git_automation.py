import time
import os
import random
import shutil,errno
from datetime import datetime


def commain(string):
    os.system(string)

def copy_file():
    copy_folder('./Newfolder','./Newfolder1')


def rem_file():
    try:
        shutil.rmtree('Newfolder1')
    except:
        print("ERROR in DELETE FILES")



def copy_folder(src,dst,symlink=False,ignore=None):
    os.makedirs(dst, exist_ok=True)
    
    # Iterate through the contents of the source folder
    for root, dirs, files in os.walk(src):
        # Determine the new directory path relative to the destination folder
        relative_dir = os.path.relpath(root, src)
        new_dir = os.path.join(dst, relative_dir)
        
        # Create the new directory if it doesn't exist
        os.makedirs(new_dir, exist_ok=True)
        
        # Copy the files
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(new_dir, file)
            shutil.copy2(src_file, dst_file)


def push_commit(commit_message):
    commain(f'cmd /c git commit -m \"{commit_message}\"')
    commain('cmd /c "git push') 
    commain('cmd /c "git init')
    commain('cmd /c "git add ."')



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
        commain("git push --set-upstream origin optmize")
        commain('cmd /c git checkout -b optmize')
    else:
        commain('cmd /c git checkout main')

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
        if i % 2 == 0:
            changebranch(branch)


def main():
    date = datetime.today().strftime("%Y-%m-%d")
    sleeped = False
    while True:
        today  = datetime.today().strftime("%Y-%m-%d")
        print(today)
        print(date)
        if datetime.strptime(today, "%Y-%m-%d") == datetime.strptime(date, "%Y-%m-%d") :
            date = today.replace(day=datetime.strptime(today, "%Y-%m-%d").day+1)
            num = random.randint(10,20)
            today_commits(num)
            sleeped= False
        else:
            if sleeped == False:
                sleeped= True
                sleep_duration = 23 * 3600 + 55 * 60
                print("Sleeping for 23 hours and 55 minutes...")
                time.sleep(sleep_duration)
                print("Woke up!")


if __name__ == '__main__':
    main()



