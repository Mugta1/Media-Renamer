
import os
import openai
#Initial commit

openai.api_keyapi= "your openai key"

#get the name of media files in a given directory

def findingmedia(directory):
    media=[]
    for path,subdir, files in os.walk(directory):
        for file in files:
            if file.lower.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.webm', '.vob', '.ogv', '.ts')):
                media.append(os.path.join(path,file))

    return media




#get the format from the user and get the names of files from openAI according to that


    

#Rename



#final function

def main():
    directory=str(input("please enter the directory to be renamed"))
    format=str(input("Please enter the format you will like the files to be renamed in"))
