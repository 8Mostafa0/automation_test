import time
import subprocess as sp
import shutil
import random
import os
from datetime import datetime
sp.call (['echo','Program ==================================== Started'])
os.chdir("/home/mosielite5/mosi/automation_test/")
sp.call(["ls","-l"])
# sp.call(["cd","/mosi/automation_test/"])

# Lists of words for different parts of speech
subjects = ["Python", "Loops", "Functions", "Variables"]
verbs = ["learned", "practiced", "debugged", "built"]
adjectives = ["fun", "challenging", "powerful", "useful"]
articles = ["a", "an"]
prepositions = ["with", "on", "about"]

# Function to generate a random sentence
def generate_sentence():
  subject = random.choice(subjects)
  verb = random.choice(verbs)
  adjective = random.choice(adjectives)
  article = random.choice(articles) if subject not in ["Python"] else ""
  preposition = random.choice(prepositions)

  # Combine the words with spaces and punctuation
  sentence = f"{article} {subject} lesson was {adjective} and we {verb} {preposition} it in class."
  return sentence

# Generate and print 5 random sentences

def generate_commit_message():
    sentence = ""
    for _ in range(7):
        sentence = generate_sentence()
    return sentence

def commands(string):
    sp.call(["echo",string+"\n\n"])
    sp.call(string.split())

def copy_file():
    copy_folder('./Newfolder','./Newfolder1')


def rem_file():
    try:
        shutil.rmtree('Newfolder1')
    except:
        os.call(["echo","ERROR in DELETE FILES"])



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


def push_commit(commit_message,branch):
    commands('git add .')
    txt = ' git commit -m '
    for i in commit_message.split():
        txt += i+"_"


    commands(txt+"_"+branch)
    commands('git push mosi '+branch)




def changebranch(opt):
    bch = "main"
    if opt:
        bch = "optimize"
    print("branch set to  => ",bch)
    if(opt):
        commands('git branch  optmize')
        commands("git --set-upstream origin optmize")
    else:
        commands('git checkout main')

def today_commits(number):
    i = 0
    sp.call(["echo","Commits : ",str(number)])
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
        branch = "main"
        push_commit(msg,branch)
        if i % 2 == 0:
            if branch == "main":
                branch = "optmize"
            else:
                branch = "main"
            changebranch(branch)



def main():
    date = datetime.today().strftime("%Y-%m-%d")
    sleeped = False
    while True:
        today  = datetime.today().strftime("%Y-%m-%d")
        print(today)
        print(date)
        if datetime.strptime(today, "%Y-%m-%d") == datetime.strptime(date, "%Y-%m-%d") :
            date = datetime.strptime(today, "%Y-%m-%d").replace(day=datetime.strptime(today, "%Y-%m-%d").day+1).strftime("%Y-%m-%d")
            num = random.randint(0,15)
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



