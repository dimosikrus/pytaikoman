import os
import shutil
import time

basetext = ("[Events]" + "\n" +
    "//Background and Video events" + "\n" +
    "//Storyboard Layer 0 (Background)" + "\n" +
    "//Storyboard Layer 1 (Fail)" + "\n" +
    "//Storyboard Layer 2 (Pass)" + "\n" +
    "//Storyboard Layer 3 (Foreground)" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\manbg.png\",0,0" + "\n" +
    " M,0,0,,320,240" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.8" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    "//Storyboard Layer 4 (Overlay)" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\approachcircle.png\",0,0" + "\n" +
    " M,0,0,,200,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.51" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
    " M,0,0,,200,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.48" + "\n" +
    " C,0,0,,211,211,211" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    " T,HitSoundClap,0,351327" + "\n" +
    "  C,0,0,80,90,90,211" + "\n" +
    "  C,0,80,80,211,211,211" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\approachcircle.png\",0,0" + "\n" +
    " M,0,0,,280,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.51" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
    " M,0,0,,280,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.48" + "\n" +
    " C,0,0,,211,211,211" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    " T,HitSound,0,351327" + "\n" +
    "  C,0,0,80,211,90,90" + "\n" +
    "  C,0,80,80,211,211,211" + "\n" +
    " T,HitSoundClap,0,351327" + "\n" +
    "  C,0,0,80,211,211,211" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\approachcircle.png\",0,0" + "\n" +
    " M,0,0,,360,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.51" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
    " M,0,0,,360,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.48" + "\n" +
    " C,0,0,,211,211,211" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    " T,HitSound,0,351327" + "\n" +
    "  C,0,0,80,211,90,90" + "\n" +
    "  C,0,80,80,211,211,211" + "\n" +
    " T,HitSoundClap,0,351327" + "\n" +
    "  C,0,0,80,211,211,211" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\approachcircle.png\",0,0" + "\n" +
    " M,0,0,,440,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.51" + "\n" +
    " F,0,351327,,1,0" + "\n" +
    "Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
    " M,0,0,,440,400" + "\n" +
    " F,0,0,,0,1" + "\n" +
    " S,0,0,,0.48" + "\n" +
    " C,0,0,,211,211,211" + "\n" +
    " F,0,351327,,1,0" + "\n"
    " T,HitSoundClap,0,351327" + "\n" +
    "  C,0,0,80,90,90,211" + "\n" +
    "  C,0,80,80,211,211,211" + "\n"
    )

class taikoman:
    def __init__(self):
        self.osufile:str = ""
        self.osbfile:str = ""
        self.resourcefolder:str = ""
        self.hitobjects:bool = False
        self.fileselected:bool = False
        self.scanned:bool = False
        self.filesadded:bool = False
        self.loopcount:int = 0
        self.dt:bool = False

    def generate(self):
        if self.fileselected and not self.hitobjects:
            with open(self.osbfile,"w") as file:
                file.write(basetext)
            self.scanned = True
            with open(self.osufile, "r", encoding="utf-8") as file:
                self.readosufile = file.readlines()
            for i in range(len(self.readosufile)):
                if self.readosufile[i] == "[HitObjects]\n":
                    self.hitobjects = True
                elif self.hitobjects:
                    self.elements = self.readosufile[i].split(',')
                    self.timing = self.elements[2]
                    self.colour = self.elements[4].replace("\n","")
                    try:
                        self.spinner = self.elements[5]
                    except:
                        self.spinner = "0"

                    if self.dt: self.timingnotdone = int(self.timing) - 1800
                    else: self.timingnotdone = int(self.timing) - 1200
                    self.timingdone = int(self.timing)

                    self.loopcount += 1

                    redright = ("Sprite,Overlay,Centre,\"SB\\taikohitcircle.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",360\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n" +
                        " C,0," + str(self.timingdone) + ",,235,69,44\n" +
                        "Sprite,Overlay,Centre,\"SB\\taikohitcircleoverlay.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",360\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n"
                        # f"Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
                        # f" M,0,{self.timingnotdone},,360,400" + "\n" +
                        # f" S,0,{self.timingnotdone},,0.48" + "\n" +
                        # f" T,HitSoundClap,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,211,211,211" + "\n" +
                        # f" T,HitSound,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,211,90,90" + "\n" +
                        # f"  C,0,80,80,211,211,211" + "\n"
                        )
                    
                    redleft = ("Sprite,Overlay,Centre,\"SB\\taikohitcircle.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",280\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n" +
                        " C,0," + str(self.timingdone) + ",,235,69,44\n" +
                        "Sprite,Overlay,Centre,\"SB\\taikohitcircleoverlay.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",280\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n"
                        # f"Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
                        # f" M,0,{self.timingnotdone},,280,400" + "\n" +
                        # f" S,0,{self.timingnotdone},,0.48" + "\n" +
                        # f" T,HitSoundClap,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,211,211,211" + "\n" +
                        # f" T,HitSound,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,211,90,90" + "\n" +
                        # f"  C,0,80,80,211,211,211" + "\n"
                        )
                    
                    blueright = ("Sprite,Overlay,Centre,\"SB\\taikohitcircle.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",200\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n" +
                        " C,0," + str(self.timingdone) + ",,67,142,172\n" +
                        "Sprite,Overlay,Centre,\"SB\\taikohitcircleoverlay.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",200\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n"
                        # f"Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
                        # f" M,0,{self.timingnotdone},,440,400" + "\n" +
                        # f" S,0,{self.timingnotdone},,0.48" + "\n" +
                        # f" T,HitSoundClap,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,90,90,211" + "\n" +
                        # f"  C,0,80,80,211,211,211" + "\n"
                        )
                    
                    blueleft = ("Sprite,Overlay,Centre,\"SB\\taikohitcircle.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",440\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n" +
                        " C,0," + str(self.timingdone) + ",,67,142,172\n" +
                        "Sprite,Overlay,Centre,\"SB\\taikohitcircleoverlay.png\",0,197" + "\n" +
                        " MX,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",440\n" +
                        " MY,0," + str(self.timingnotdone) + "," + str(self.timingdone) + ",-640,400\n" +
                        " F,0," + str(self.timingdone) + ",,1,0\n" +
                        " S,0," + str(self.timingdone) + ",,0.456\n"
                        # f"Sprite,Overlay,Centre,\"SB\\taikobigcircle.png\",0,0" + "\n" +
                        # f" M,0,{self.timingnotdone},,200,400" + "\n" +
                        # f" S,0,{self.timingnotdone},,0.48" + "\n" +
                        # f" T,HitSoundClap,{self.timingnotdone},{self.timingdone+180}" + "\n" +
                        # f"  C,0,0,80,90,90,211" + "\n" +
                        # f"  C,0,80,80,211,211,211" + "\n"
                        )

                    if self.spinner[0] != "0":
                        self.loopcount -= 1
                        #print("spinner", self.spinner[0])
                    elif self.colour == "12" or self.colour == "6":
                        with open(self.osbfile, "a") as file:
                            file.write(blueright + blueleft)
                        #print("blueright + blueleft")
                    elif self.colour == "4":
                        with open(self.osbfile, "a") as file:
                            file.write(redright + redleft)
                        #print("redright + redleft")
                    elif self.loopcount % 2 == 0:
                        if self.colour == "8" or self.colour == "2":
                            with open(self.osbfile, "a") as file:
                                file.write(blueright)
                            #print("blueright == 0")
                        elif self.colour == "0":
                            with open(self.osbfile, "a") as file:
                                file.write(redright)
                            #print("redright == 0")
                    elif self.loopcount % 2 != 0:
                        if self.colour == "8" or self.colour == "2":
                            with open(self.osbfile, "a") as file:
                                file.write(blueleft)
                            #print("blueleft != 0")
                        elif self.colour == "0":
                            with open(self.osbfile, "a") as file:
                                file.write(redleft)
                            #print("redleft != 0")
                
        elif self.fileselected == False:
            print("You need to select a .osu file to read first!")
            time.sleep(1/2)
            return False
        elif self.hitobjects:
            print("Already generated a storyboard for this map.")
            time.sleep(1/2)
            return False
        
        if self.scanned and not self.filesadded:
            with open(self.osbfile, "a") as file:
                file.write("//Storyboard Sound Samples")

            if not os.path.isdir(self.resourcefolder):
                os.mkdir(self.resourcefolder)
                print("Recource Directory Created")
                time.sleep(1/2)

            shutil.copy(src="Resources/manbg.png",         dst=os.path.join(self.resourcefolder, "manbg.png"))
            shutil.copy(src="Resources/approachcircle.png",         dst=os.path.join(self.resourcefolder, "approachcircle.png"))
            shutil.copy(src="Resources/taikobigcircle.png",         dst=os.path.join(self.resourcefolder, "taikobigcircle.png"))
            shutil.copy(src="Resources/taikohitcircle.png",         dst=os.path.join(self.resourcefolder, "taikohitcircle.png"))
            shutil.copy(src="Resources/taikohitcircleoverlay.png",  dst=os.path.join(self.resourcefolder, "taikohitcircleoverlay.png"))
            print("Success!")
            self.filesadded = True
            return True

    def fileselector(self):
        fn = input("input file path: ")
        
        filename, file_extension = os.path.splitext(fn)
        if fn == "":
            print("Select a file")
            return False
        elif file_extension != ".osu":
            print("File needs to have a .osu extension.")
            return False
        else:
            print("Currently selected map: " + fn)
            self.fileselected = True
            self.hitobjects = False
            self.scanned = False
            self.filesadded = False
            self.osufile = fn
            self.osbfile = fn[:fn.rfind("[")-1] + ".osb"
            print(self.osbfile)
            self.resourcefolder = os.path.dirname(os.path.abspath(fn)) + "\\SB\\"
            return True

if __name__ == "__main__":
    taikom = taikoman()
    def taikomand():
        print("""Select mode:
        0 file selector
        1 generator""")

        answer = str(input("> "))
        if answer not in ["0","1"]:
            taikomand()
        else:
            if answer == "0":
                oo = taikom.fileselector()
                if oo:
                    taikomand()
                elif not oo:
                    print("Error")
                    taikomand()
            elif answer == "1":
                answerdt = str(input("dt? y/n"))
                if answerdt not in ['y','n']:
                    taikomand()
                else:
                    if answerdt == "n":
                        taikom.dt = False
                        oo = taikom.generate()
                        if oo:
                            taikomand()
                        elif not oo:
                            print("Error")
                            taikomand()
                    elif answerdt == "y":
                        taikom.dt = True
                        oo = taikom.generate()
                        if oo:
                            taikomand()
                        elif not oo:
                            print("Error")
                            taikomand()
            else:
                print("Exit")

    taikomand()