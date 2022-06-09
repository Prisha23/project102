import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vco.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshottaken")
    vco.release()
    cv2.destroyAllWindows()

def uploadfile(img_name):
    acesstoken="sl.BI1Zx0gZ8vIBHNDIPx3CVM64YteTueXkYpNZUaRDjb6YtnomEw68mozvd0OKxqADBy8UjO3W5qX9aAtnT1dH8Ka5sJkaBVCDKu7xms0qhS9DJYfNCOemsxmes-bEgM0m4iePIG4TKCw"
    file=img_name
    filefrom=file
    fileto="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(acesstoken)
    with open(filefrom,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("fileuploaded")

def main():
    while(True):
        if((time.time()-start_time)>=30):
            name=take_snapshot()
            uploadfile(name)

main()
