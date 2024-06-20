##This can be used to rename your files manually, without using OpenAI or Any other LLM
import os




#Add/Remove extensions from these lists according to your need.
video_formats= ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.webm', '.vob', '.ogv', '.ts')
subtitle_formats= ('.srt', '.vtt', '.sbv', '.sub', '.ass/.ssa', '.dfxp')


#get the name of media files in a given directory
def findingmedia(directory):
    media=[]
    for path,subdir, files in os.walk(directory):
        for file in files:
            #Appends the path and names of video files into media list.
            if file.lower.endswith(video_formats):
                media.append((path,file))
            #Checks if other files are subtitle files, if not, deletes them.
            elif not file.lower.endswith(subtitle_formats):
                os.remove(file)



            

    return media

    





#Rename according to inputs provided by the user
def rename(media):
    for element in media:
        print(f'The name of this file is {element[1]}')
        nname=str(input("Enter the new name for this file"))
        newname= os.path.join(element[0], nname)
        file=os.path.join(element[0], element[1])
        os.rename(file, newname)

#final function

def main():
    directory=str(input("please enter the directory to be renamed"))
    #format=str(input("Please enter the format you will like the files to be renamed in"))
    media=findingmedia(directory)
    rename(media)


