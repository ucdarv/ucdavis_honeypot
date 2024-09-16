#Have used the antispam package here as Prof. Bishop asked to use an existing spam filter.
import antispam
import os

#The spam_training directory has all the spam files
#The ham_training_directory has all the non spam files

spam_training_directory = os.getcwd() + '/emails/spamtraining'
ham_training_directory = os.getcwd() + '/emails/hamtraining'

spamfiles = os.listdir(spam_training_directory)
hamfiles = os.listdir(ham_training_directory)

spam = []

for file in spamfiles:
    filename = spam_training_directory + '/'+ str(file)
    desc = open(filename, 'r', errors="ignore")
    content = desc.read()
    # print(antispam.score(content))
    # print(antispam.is_spam(content))
    if(antispam.is_spam(content)):
        spam.append(file)


#The spam list has all the files that are spam.
print(spam)




