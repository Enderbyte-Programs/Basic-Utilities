move .\BasicUtilities\BasicUtilities.py BasicUtilities.py
move .\BasicUtilities\scupdate.py scupdate.py
del /s /f /q .\BasicUtilities\*
del .\dist\BasicUtilities.exe
del .\compiler-output\BasicUtilities.exe
del .\compiler-output\BasicUtilities.py
rmdir .\BasicUtilities\.temp
rmdir .\BasicUtilities\crash_reports
.\pyinstaller --icon=bu.ico --version-file=vf.txt --noconfirm BasicUtilities.py
.\pyinstaller --icon=bu.ico --version-file=vf.txt --onefile BasicUtilities.py
xcopy /s /e .\dist\BasicUtilities .\BasicUtilities
copy bu.ico .\BasicUtilities\bu.ico
copy turtle.ico .\BasicUtilities\turtle.ico
copy license.txt .\BasicUtilities\license.txt
copy scupdate.py .\BasicUtilities\scupdate.py
del /s /f /q .\compiler-output\*
"C:\Program Files (x86)\Inno Setup 6\iscc.exe" bu.iss
del /s /f /q .\BasicUtilities\*
rmdir /s /q .\BasicUtilities\
mkdir BasicUtilities
copy BasicUtilities.py .\compiler-output
copy bu.iss .\compiler-output
copy .\dist\BasicUtilities.exe .\compiler-output
move BasicUtilities.py .\BasicUtilities\BasicUtilities.py
move scupdate.py .\BasicUtilities\scupdate.py