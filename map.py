x=0
import random
import math
import PIL
from PIL import Image
import numpy
phase=0
data=[]
landdata=[]
counter=0
sea=40
land=200
length=0
height=0
length2=length*length
percent=0
arr=[]
circles=[]
radiuses=[]
progress=0
op=0 #Old Progress
p=0 #Progress
def circle(mid,radius): #Generate Circles
    angle=0
    while angle<360:
        temp=0
        while temp<=radius:
            xcoord=temp*math.cos(math.radians(angle))
            ycoord=temp*math.sin(math.radians(angle))
            xcoord=round(xcoord,0)
            xcoord=int(xcoord)
            ycoord=round(ycoord,0)
            ycoord=int(ycoord)
            try:
                data[mid+xcoord+ycoord*length]=sea
            except:
                placeholder=0
            temp=temp+1
        angle=angle+(360/(7*radius))
    return

def landcircle(mid,radius): #Create landcircle, currently unused.
    angle=0
    while angle<360:
        temp=0
        while temp<=radius:
            xcoord=temp*math.cos(math.radians(angle))
            ycoord=temp*math.sin(math.radians(angle))
            xcoord=round(xcoord,0)
            xcoord=int(xcoord)
            ycoord=round(ycoord,0)
            ycoord=int(ycoord)
            try:
                data[mid+xcoord+ycoord*length]=land
            except:
                placeholder=0
            temp=temp+1
        angle=angle+(360/(7*radius))
    return

def edges(mid,radius): #Return coords of edges of a circle
    global sea
    counter=0
    while counter<5:
        radius=radius+2
        counter=0
        angle=(random.random()*360)
        xcoord=radius*math.cos(math.radians(angle))
        ycoord=radius*math.sin(math.radians(angle))
        xcoord=round(xcoord,0)
        xcoord=int(xcoord)
        ycoord=round(ycoord,0)
        ycoord=int(ycoord)
        num=mid+xcoord+ycoord*length
        try:
            if data[num]==land:
                counter=5
        except:
            placeholder=0
        counter=counter+1
    return num
        

def rough(mid,radius,crag): #Roughen up the shorelines by making a bunch of smaller circles)
    global sea
    global cir
    counter=0
    radius=radius+2
    while counter<crag:
        angle=(random.random()*360)
        xcoord=radius*math.cos(math.radians(angle))
        ycoord=radius*math.sin(math.radians(angle))
        xcoord=round(xcoord,0)
        xcoord=int(xcoord)
        ycoord=round(ycoord,0)
        ycoord=int(ycoord)
        num=mid+xcoord+ycoord*length
        try:
            if data[num]==land:
                circle(num,radius/random.randint(5,20))
        except:
            placeholder=0
        counter=counter+1




while x==0:
    while phase==0:
        print("What percentage do you wish your world be water? (0-100 please.)")
        percent=input(">")
        try:
            percent=float(percent)
        except:
            print("That's not a number.")
            break
        if percent>100:
            print("That's over 100.")
            break
        if percent<0:
            print("That's under 0.")
            break
        phase="size"
    while phase=="size":
        print("What size do you want your world? (Length)")
        length=input(">")
        try:
            length=int(length)
        except:
            print("That's not an integer.")
            break
        if length<0:
            print("You can't have negative pixels!")
            break
        phase="height"
    while phase=="height":
        print("What size do you want your world? (Height)")
        height=input(">")
        try:
            height=int(height)
        except:
            print("That's not an integer.")
            break
        if length<0:
            print("You can't have negative pixels!")
            break
        phase="height"
        phase="cir"
    while phase=="cir":
        print("What scale do you want your world to be? (1=1 standard world map).")
        cir=input(">")
        cir=float(cir)
        cir=float((length)*cir)/50
        cir=round(cir,0)
        cir=int(cir)
        print("Brush Size",cir)
        phase=1
    while phase==1:
        data=[]
        counter=0
        while counter<length*height:
            data.append(land)
            counter=counter+1
        counter=0
        phase=2
    while phase==2:
        percent=percent/100
        middle=random.randint(0,length)+random.randint(0,height)*length
        rad=cir*2*random.random()
        while (data.count(sea)/(length*height))<percent:
            circle(middle,rad)
            rad10=rad*10
            rough(middle,rad,rad)
            counter=0
            oldmiddle=middle
            middle=edges(middle,rad)
            rad=rad*(random.random()*0.5+0.5)
            oldprogress=progress
            progress=((data.count(sea)*100/(length*height))/percent)
            if oldprogress==progress:
                middle=random.randint(0,length)+random.randint(0,height)*length
                rad=cir*2*random.random()
            if rad<1:
                middle=random.randint(0,length)+random.randint(0,height)*length
                rad=cir*2*random.random()
            op=p
            p=(round(progress,0))
            if p>op:
                print("Progress:",p,"%")
        print("Processing complete.")
        phase="convert"
    while phase=="convert":
        data=numpy.array(data)
        data=data.reshape((height,length)).astype('uint8')
        im=Image.fromarray(data)
        im.show()
        phase=0
        data=[]
    while phase=="never": #Just a storage for code that will never be used.
        try:
            data[num]=sea
        except:
            placeholder=0
        rand=random.randint(0,1)
        if rand==1:
            try:
                data[num+1]=sea
            except:
                placeholder=0
        rand=random.randint(0,1)
        if rand==1:
            try:
                data[num-1]=sea
            except:
                placeholder=0
        rand=random.randint(0,1)
        if rand==1:
            try:
                data[num+length]=sea
            except:
                placeholder=0
        rand=random.randint(0,1)
        if rand==1:
            try:
                data[num-length]=sea
            except:
                placeholder=0
