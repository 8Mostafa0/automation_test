import time
import os
import shutil




def copy_file():
    shutil.copy('./test.txt','./1text1.txt')


def rem_file():
    os.remove('./1test.txt')




def push_commit(commit_message):
    commit_message=commit_message.split(" ")
    text = ""
    for i in commit_message:
        text+= i+"_"
    print(text)
    os.system(f'cmd /c "git commit -m `{commit_message}`"')
    os.system('cmd /c "git push"') 
    os.system('cmd /c "git init"')
    os.system('cmd /c "git add ."')




def main():
    copy_file()     
    push_commit("Test Mikonim")     
if __name__ == '__main__':
    main()