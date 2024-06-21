
import os
import google.generativeai as genai
#Initial commit
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

#Add/Remove extensions from these lists according to your need.
video_formats= ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.webm', '.vob', '.ogv', '.ts')
subtitle_formats= ('.srt', '.vtt', '.sbv', '.sub', '.ass/.ssa', '.dfxp')


#get the name of media files in a given directory
def findingmedia(directory):
    media=[]
    for path,subdir, files in os.walk(directory):
        for file in files:
            #Appends the path and names of video files into media list.
            if file.lower().endswith(video_formats):
                media.append((path,file))
    return media


#get the format and example from the user and get the names of files from Gemini according to that

def newname(prompt):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    nname = model.generate_content(prompt)
    return nname  

#Rename according to format and example provided by the user 
def rename(media, format, examplein, exampleout):
    for element in media:
        prompt= "rename the following media according to the format \n" + format + "\n\n" + "for example" + examplein + "\n will change to \n" + exampleout+ "\n now rename this" + element[1]+ "only return the renamed name as your output"
        print(f'The name of this file is {element[1]}')
        splitname=element[1].split('.')
        format=splitname[-1]
        nname=newname(prompt)
        nname=nname+'.'+format
        try:
            file=os.path.join(element[0], element[1])
            newname= os.path.join(element[0], nname)
            #Rename
            os.rename(file, newname)
            print(f'File with name {element[1]} renamed to {nname} successfully')
        except OSError as error:
            print(f"Could not rename file {element[1]} \n Error = {error}")

#Deletes obsolete files other than the files with extensions specified in the subtitle_formats and video_formats tuples.
def deleter(directory):
    count=0
    for path, subdir, files in os.walk(directory):
         for file in files:
            if not file.lower().endswith(subtitle_formats) and not file.lower().endswith(video_formats):
                try:
                    os.remove(os.path.join(path,file))
                    count+=1
                except OSError as error:
                    print(f"Could not delete file {file} \n Error = {error}")

#Lets the user rename another Directory/exit the program
def again():
    choice= input("Do you want to rename any other directory? \n 1. Yes \n 2.No \n")
    if choice.lower()=='yes' or choice=='1':
        main()
    elif choice.lower()=='no' or choice =='2':
        print("Thank you for using this program :)")
        quit()
    else:
        print("Wrong input, try again")
        again()

#Main function
def main():
    print("Welcome to media renamer ^-^")
    directory=str(input("please enter the directory to be renamed \n"))
    format=str(input("Please enter the format you will like the files to be renamed in"))
    examplein=str(input("Enter an example name to be changed"))
    exampleout=str(input("Enter the accurate output desired for the given example"))
    
    if not os.path.isdir(directory):
        print("Wrong Directory, exiting this directory. ")
        again()
    
    #format=str(input("Please enter the format you will like the files to be renamed in"))
    media=findingmedia(directory)
    if not media:
        print(f"No media files in this directory \n {directory}")
        again()
    
    rename(media, format, examplein, exampleout)
    delete= input("Do you want to delete obsolete files in this directory? \n 1. Yes \n 2.No \n")
    if delete.lower()=='yes' or delete=='1':
        deleter(directory)
        print(f"Files in the directory {directory} renamed and obsolete files deleted successfully.")
        
    elif delete.lower()=='no' or delete=='2':
        print(f"Files in the directory {directory} renamed successfully")
    else:
        print("wrong input, ignoring.")
    again()

main()
    

    


