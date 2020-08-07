# snipeit-brother-label

Label Printer for SnipeIT with Brother PT-E550W in 24mm or 12mm

### Requirements
python3<br>
Ptouch editor for create label templates<br>
Brother Printer SDK<br>

### Files

label.lbx - Template created in PTouch Label Editor <br>
labelprint.py - Python file to interact with snipeit api to get Asset details<br>
labelscript.vbs - Template VBScript <br>
new.vbs - File will be overwritten with content to print<br>
run.bat/exe - File to new.vbs in python. <i> convert to exe </i><br>

### For building Python to Exe
pyinstaller --onefile labelprint.py <br>

Save all files in <i>D:\labelcreater</i> or change the path in  code.
