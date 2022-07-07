# Installion 
1. Python
3. Inkscape  

are needed to run this script.

The easiest way to install python on a Windows computer is to open Powershell and type:
```commandline
python3
```
https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=en-us&gl=US is the direct link to it.  
This should open the windows store to the Python3.10 app which you should install.    

Next, type 
```commandline
python3.10 -m pip install keyboard
```
which installs a necessary dependency for the script to run.

Inkscape can be downloaded from here: https://inkscape.org/release/inkscape-1.2/
# Usage  
First, create a folder with all your DXF files (DXF-FOLDER) and an output folder for your SVG files (SVG-FOLDER).

Then copy the script into the parent directory of both those folders. Right click and open a terminal in the same parent folder and run:
```commandline
python3.10 dxf2svg.py DXF-FOLDER SVG-FOLDER
```
replacing the folder names with whatever it is in your system.

More generally:
```commandline
python dxf2svg.py indir outdir
```

# Design  
The script uses the Inkscape CLI to export a DXF as an SVG. The Inkscape CLI does an annoying thing where it opens a dialog window to confirm scaling.
To avoid this, the script presses enter 5 seconds after opening the DXF file in Inkscape to skip the dialogue which could be problematic if Inkscape takes longer than 5 seconds to open a DXF file.

Ideally, Python would wait for the dialog to load in, then press enter but that would require way more code.

# Troubleshooting
It could be the case that Python presses enter on a window which is not the dialog. In that case, you would manually click OK on the inkscape dialogue and the script will continue as normal.
To avoid this, refrain from clicking around or typing while the script is running, which is an unfortunate design flaw of it.