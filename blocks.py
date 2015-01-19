#!/usr/bin/python
#Helper Functions to write blocks

#Blocks for use in the script found in usr/share/backgrounds/
def startBlock(writePath):
	"Creates the background tag and starttime block"
	writePath.write("<background>\n\t<starttime>\n\t\t<year>2009</year>\n\t\t<month>08</month>");
	writePath.write("\n\t\t<day>04</day>\n\t\t<hour>00</hour>\n\t\t<minute>00</minute>\n\t\t");
	writePath.write("<second>00</second>\n\t</starttime>\n");
	return;
def staticBlock(writePath, filePath, duration):
	"Creates a static block for images"
	writePath.write("\t<static>\n\t\t<duration>"+str(duration)+"</duration>\n");
	writePath.write("\t\t<file>"+filePath+"</file>\n\t</static>\n");
	return;
def transitionBlock(writePath, before, after, duration):
	"Creates a transition block for images"
	writePath.write("\t<transition>\n\t\t<duration>"+str(duration)+"</duration>\n");	
	writePath.write("\t\t<from>"+before+"</from>\n\t\t<to>"+after+"");
	writePath.write("</to>\n\t</transition>\n");
	return;	
#Blocks for use in the script found in usr/share/gnome-background-properties/
def GstartBlock(writePath, slideshowName, xmlPath):
	"Creates beginning block in script for gnome-background-properties with show name and path"
	writePath.write("<wallpapers>\n\t<wallpaper deleted=\"false\">\n\t\t<name>");
	writePath.write(slideshowName+"</name>\n\t\t<filename>"+xmlPath+"</filename>\n");
	writePath.write("\t\t<options>zoom</options>\n\t</wallpaper>\n");
	return;
def GwallpaperBlock(writePath, imgName, filePath):
	"Creates <wallpaper> block in gnome-background-properties"
	writePath.write("\t<wallpaper>\n\t\t<name>"+str(imgName)+"</name>\n");
	writePath.write("\t\t<filename>"+filePath+"</filename>\n\t</wallpaper>\n");
	return;
