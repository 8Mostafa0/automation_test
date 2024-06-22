import time
import os
import shutil




def copy_file():
    copy_folder('./Newfolder','./Newfolder1')


def rem_file():
    os.remove('./1test.txt')

def copy_folder(src,dst,symlink=False,ignore=None):
    if os.path.exists(dst) == False or os.path.isdir(dst) == False:
        os.mkdirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src,item)
        d = os.path.join(dst,item)
        if os.path.isdir(s):
            shutil.copytree(s,d,symlink,ignore)
        else: 
            shutil.copy2(s,d)


def push_commit(commit_message):
    commit_message=commit_message.split(" ")
    text = ""
    for i in commit_message:
        text+= i+"_"
    os.system(f'cmd /c "git commit -m\"{text}\""')
    os.system('cmd /c "git push"') 
    os.system('cmd /c "git init"')
    os.system('cmd /c "git add ."')




def main():
    copy_file()     
    push_commit("make apps automaticly push commit to git hub and now create a part for copy a folder")     
if __name__ == '__main__':
    main()