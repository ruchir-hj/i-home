import  sys , os
from string import split
from os.path import join,basename
from eigenfaces import egface
from opencv import highgui as hg 

global_frame=0
i_home_imagefile = ''

class PyFaces:
    def __init__(self,testimg,imgsdir,egfnum,thrsh,frame):
        self.testimg=testimg
        self.imgsdir=imgsdir
        self.threshold=thrsh
        self.egfnum=egfnum
        self.i_home_imagefile = ''
        self.numimgs=0
        extn=split(basename(testimg),'.')[1]        
        
        #print "to match:",self.testimg," to all ",extn," images in directory:",dirname        
        self.facet=egface()
        self.egfnum=self.setselectedeigenfaces(self.egfnum,extn)
        print "num of eigenfaces used:",self.egfnum
        try:
            self.facet.checkCache(self.imgsdir,extn,self.imgnamelist,self.egfnum,self.threshold)
        except Exception, inst:
            #print "failed :",inst.message
            print "failed :"
        else:
            mindist,matchfile=self.facet.findmatchingimage(self.testimg,self.egfnum,self.threshold)
            if not matchfile or mindist==0.0:
                print "NOMATCH! try higher threshold"
                print "including in image database :", testimg
                self.numimgs = self.numimgs + 1
                newname="image" + str(self.numimgs) + ".png"
                os.chdir("images")
                self.i_home_imagefile = newname
                hg.cvSaveImage(newname ,frame)
                os.chdir("..")
                
            else:
                print "matches :"+matchfile+" dist :"+str(mindist)
                self.i_home_imagefile = matchfile.split('\\')[1]

    def getFileName(self):
        return self.i_home_imagefile
        
        
    def setselectedeigenfaces(self,selectedeigenfaces,ext):        
        #call eigenfaces.parsefolder() and get imagenamelist        
        self.imgnamelist=self.facet.parsefolder(self.imgsdir,ext)                    
        self.numimgs=len(self.imgnamelist)        
        if(selectedeigenfaces >= self.numimgs  or selectedeigenfaces == 0):
            selectedeigenfaces=self.numimgs/2    
        return selectedeigenfaces
        
        
#if __name__ == "__main__":
def recognize_face():
    try:
        argsnum=len(sys.argv)
        print "args:",argsnum
        #if(argsnum<5):
         #   print "usage:python pyfaces.py imgname dirname numofeigenfaces threshold "
          #  sys.exit(2)                
        #imgname=sys.argv[1]
        #dirname=sys.argv[2]
        #egfaces=int(sys.argv[3])
        #thrshld=float(sys.argv[4])

        capture=hg.cvCreateCameraCapture(0)
        hg.cvNamedWindow("Snapshot")
        i=0
        #time.sleep(1)
        myframe=0
        imgname='sample.png'
        dirname='images'
        egfaces=5
        thrshld=0.3
        #frame=0
        
        while 1:     
            frame=hg.cvQueryFrame(capture)
            #print type(frame)
            hg.cvShowImage("Snapshot",frame)
            key = hg.cvWaitKey(5)
            if key=='c' or key=='C':
                hg.cvDestroyWindow("Snapshot")
                hg.cvSaveImage(imgname,frame)
                global_frame=frame
                break   
                #print frame   

        #sys.exit(0)

        pyf=PyFaces(imgname,dirname,egfaces,thrshld,frame)
        #if pyfaces returns false then save this image into images folder
        hg.cvReleaseCapture(capture) 
        return pyf.getFileName()

    except Exception,detail:
        print detail
        print "usage:python pyfaces.py imgname dirname numofeigenfaces threshold "

if __name__ == "__main__":
    recognize_face()
