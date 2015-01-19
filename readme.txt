GNOME Wallpaper Slideshow Generator

Downloading
-----------
GNOME Wallpaper Slideshow Generator is publicly available on GitHub

	https://github.com/jknollmeyer/gnome-slideshow

Download main.py and blocks.py into the same directory to use the script

Usage
-----
To use the generator, run main.py using python from the command line. Enter the name of the slideshow and the slide duration in the appropriate fields. Select the images using the file dialog, the order of the slideshow will be order in which the files are selected in the dialog. After those 3 settings have been decided, click create script to generate the files.

There will be two files created, [slideshowName].xml and [slideshowName]-properties.xml. [slideshowName].xml will need to be moved to /usr/share/backgrounds/, and [slideshowName]-properties.xml needs to be moved in /usr/share/gnome-background-properties. After this has been done, the slideshow will be available from the normal wallpaper setting dialog.

Bug Reporting
-------------
Please use the Issues section of the GitHub page to report bugs or problems which are encountered in the usage of the generator.
