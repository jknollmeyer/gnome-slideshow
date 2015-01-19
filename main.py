#!/usr/bin/python
import os, blocks;
from Tkinter import *
from tkFileDialog import *
#Declaring GUI root and global variables (lazy, needs to change in future)
FileList = [] #Array for paths for each image
root = Tk()
statusString = StringVar() #StringVar which is updated to show app status
statusString.set("Welcome to the GNOME Wallpaper Slideshow Generator!")
#Function to select image files to be put in global file array
#currently the selection is overwritted every time this is opened
def SelectFiles():
	global fileList #Use global scope for global vars
	global statusString
	fileList = askopenfilenames() #dialog to select multiple images
	if len(fileList) <= 0:
		statusString.set("No Files Selected")
	else:
		statusString.set("Image Files Selected")
#Function takes files from file array and creates two scripts
#outputScript can stay where it is, and transition details for the show
#G-File needs to be moved to /usr/share/gnome-background-properties/
#it contains property info about the show and the slides
#you can't move the output script because G-File has to know its location
#outputScript: name of slideshow
#duration: obvious
def CreateFiles(outputScript, duration):
	global statusString
	statusString.set("Failed to generate script")
	global fileList
	outputFile = open(outputScript+".xml", "w+");
	GFile = open(outputScript+"-properties.xml","w+");
	blocks.startBlock(outputFile);
	blocks.GstartBlock(GFile,outputScript, os.path.join(os.path.dirname(os.path.realpath(__file__)),outputFile.name));
	x = len(fileList);
	#Cycles through the filelist, creating the appropriate block for each
	#file, but it leaves out the last block because the last entry needs
	#a special transition, since the last slide needs to wrap to the first
	for i in range(x-1):
		blocks.staticBlock(outputFile, fileList[i],duration);
		blocks.GwallpaperBlock(GFile,os.path.splitext(os.path.basename(fileList[i]))[0],fileList[i]);
		blocks.transitionBlock(outputFile,fileList[i], fileList[i+1],5.0);
#Special case because the last transition needs to wrap around
	blocks.staticBlock(outputFile, fileList[x-1],duration);
	blocks.GwallpaperBlock(GFile,os.path.splitext(os.path.basename(fileList[x-1]))[0],fileList[x-1]);
	blocks.transitionBlock(outputFile,fileList[x-1], fileList[0],5.0);
	#Closing tags and update the status to indicate it ran true
	GFile.write("</wallpapers>");
	outputFile.write("</background>");
	statusString.set("Scripts successfully created")
#App holds all the widgets for the Tkinter GUI
#Widgets: frame (Holds them all), name text label, name entry field
#duration text label, duration entry field, SelectFiles bttn, CreateFiles bttn
class App:
	def __init__(self, master):
		global statusString
		frame = Frame(master)
		frame.pack()
		w = Label(frame, text="Enter the name for the script:")
		w.pack()
		self.nameEntry = Entry(frame)
		self.nameEntry.pack();
		y = Label(frame, text="Enter the duration of the slides")
		y.pack()
		self.durationEntry = Entry(frame);
		self.durationEntry.pack();
		#Using lambda before commands prevents them from running
		#on startup, idk why
		self.filesButton = Button(
			frame, text="Choose Files...", command = lambda: SelectFiles()
			)
		self.filesButton.pack()
		self.runButton = Button(
			frame, text="Create scripts", command=lambda:CreateFiles(self.nameEntry.get(),self.durationEntry.get())
			)
		self.runButton.pack()
		self.statusLabel = Label(frame, textvariable=statusString)
		self.statusLabel.pack();
app = App(root)
root.mainloop()
