import time
import os
import shutil



def main():
    
    os.system('cmd /c "git init"')
    shutil.copy('./test.txt','./1test.txt')
    os.system('cmd /c "git add ."')
    os.system('cmd /c "git commit -m `mosielite`"')
    os.system('cmd /c "git push"')
     
if __name__ == '__main__':
    main()