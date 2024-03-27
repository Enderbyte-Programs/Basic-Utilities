#define MyAppName "Basic Utilities"
#define MyAppVersion "2.31"
#define MyAppPublisher "Enderbyte Programs"
#define MyAppURL "https://enderbyte09.wixiste.com/programs"
#define MyAppExeName "BasicUtilities.exe"
#define MyAppAssocName "BU Encrypted"
#define MyAppAssocExt ".bue"
#define Assocname2 "Turtle Drawing"
#define Assocext2 ".trt"
#define Assockey2 StringChange(Assocname2, " ", "") + Assocext2 
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt
#define Notpad "Notpad-New File"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{63C7E05A-F445-48FF-BEA1-5BCA5D95B2C8}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\BasicUtilities
ChangesAssociations=yes
DisableProgramGroupPage=auto
LicenseFile=C:\Python310\Scripts\license.txt
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Python310\Scripts\compiler-output
OutputBaseFilename=BasicUtilities-2.31-installer
SetupIconFile=C:\Python310\Scripts\bu.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
UsedUserAreasWarning=no
UninstallDisplayIcon="{app}\bu.ico"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "associate"; Description: "Associate the .bue file extension with Basic Utilities"; GroupDescription: "Registry"
Name: "assoc"; Description: "Associate the .trt file extension with Basic Utilities"; GroupDescription: "Registry"
Name: "associate2"; Description: "Add Edit with Notpad (Text Editor) to file right click menu";GroupDescription: "Registry"
Name: "clrapdat"; Description: "Delete exisiting Appdata"; GroupDescription: "Cleanup"; Flags: unchecked
Name: "clrold"; Description: "Delete unneeded files from old versions"; GroupDescription: "Cleanup"
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "openonstart"; Description: "Run Program on Startup"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "notpad"; Description: "Create shortcuts for Notpad (Text Editor)"; GroupDescription: "{cm:AdditionalIcons}"

[Files]

Source: "C:\Python310\Scripts\BasicUtilities\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue; Tasks: associate
Root: HKA; Subkey: "Software\Classes\{#Assocext2}\OpenWithProgids"; ValueType: string; ValueName: "{#Assockey2}"; ValueData: ""; Flags: uninsdeletevalue; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey; Tasks: associate
Root: HKA; Subkey: "Software\Classes\{#Assockey2}"; ValueType: string; ValueName: ""; ValueData: "{#Assocname2}"; Flags: uninsdeletekey; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"; Tasks: associate
Root: HKA; Subkey: "Software\Classes\{#Assockey2}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\turtle.ico"; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"" ""-t"""; Tasks: associate
Root: HKA; Subkey: "Software\Classes\{#Assockey2}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"" ""-d"""; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".bue"; ValueData: ""; Tasks: associate
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".trt"; ValueData: ""; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\*\shell\BU"; ValueType: string; ValueName: ""; ValueData: "Edit with Notpad"; Flags: uninsdeletekey ;Tasks: associate2
Root: HKA; Subkey: "Software\Classes\*\shell\BU\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1""" ;Tasks: associate2
[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}";Tasks: openonstart
Name: "{autoprograms}\{#Notpad}"; Filename: "{app}\{#MyAppExeName}"; Parameters: "-n" ;Tasks: notpad
Name: "{autodesktop}\{#Notpad}"; Filename: "{app}\{#MyAppExeName}"; Parameters: "-n" ; Tasks: notpad

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[InstallDelete]
Type: files; Name: "{app}\crash_reports\*"; Tasks: clrapdat
Type: dirifempty; Name: "{app}\crash_reports"; Tasks: clrapdat
Type: files; Name: "{app}\lag.csv"; Tasks: clrapdat
Type: files; Name: "{app}\.temp\*"; Tasks: clrapdat
Type: files; Name: "{app}\appdata.json"; Tasks: clrapdat
Type: files; Name: "{app}\logoff.bat";Tasks: clrold
Type: files; Name: "{app}\restart.bat";Tasks: clrold
Type: files; Name: "{app}\clrapdat.bat";Tasks: clrold
Type: files; Name: "{app}\execute.bat";Tasks: clrold
Type: files; Name: "{app}\pre-uninstall.bat";Tasks: clrold
Type: files; Name: "{app}\ping.bat";Tasks: clrold
Type: files; Name: "{app}\permaping.bat";Tasks: clrold
Type: files; Name: "{app}\stop.bat";Tasks: clrold
Type: files; Name: "{app}\notice.txt";Tasks: clrold
Type: files; Name: "{app}\notes.txt";Tasks: clrold
Type: files; Name: "{app}\changelog.txt";Tasks: clrold
Type: files; Name: "{app}\license.txt";Tasks: clrold
Type: files; Name: "{app}\warning.mp3";Tasks: clrold

Type: files; Name: "{app}\unins000.exe"
Type: files; Name: "{app}\can.mp3";Tasks: clrold
Type: files; Name: "{app}\startup.mp3";Tasks: clrold
Type: files; Name: "{app}\error.vbs";Tasks: clrold
Type: files; Name: "{app}\gameboard.jpg";Tasks: clrold
Type: files; Name: "{app}\BasicUtilities.py";Tasks: clrold
Type: files; Name: "{app}\appdata.txt" ;Tasks: clrold
Type: files; Name: "{app}\bcount.txt" ;Tasks: clrold
Type: files; Name: "{app}\btime.txt";Tasks: clrold
Type: files; Name: "{app}\bday.txt";Tasks: clrold
Type: files; Name: "{app}\history.txt";Tasks: clrold
Type: files; Name: "{app}\notifs.txt";Tasks: clrold
Type: files; Name: "{app}\health.txt" ;Tasks: clrold
Type: files; Name: "{app}\xp.txt.txt" ;Tasks: clrold
Type: files; Name: "{app}\username.txt" ;Tasks: clrold
Type: files; Name: "{app}\startsound.dat" ;Tasks: clrold

[UninstallDelete]
Type: files; Name: "{app}\appdata.txt"
Type: files; Name: "{app}\bcount.txt"
Type: files; Name: "{app}\btime.txt"
Type: files; Name: "{app}\bday.txt"
Type: files; Name: "{app}\history.txt"
Type: files; Name: "{app}\notifs.txt"
Type: files; Name: "{app}\health.txt"
Type: files; Name: "{app}\xp.txt.txt"
Type: files; Name: "{app}\username.txt"
Type: files; Name: "{app}\startsound.dat"
Type: files; Name: "{app}\log_000.log"
Type: files; Name: "{app}\appdata.json"
Type: files; Name: "{app}\warning.mp3"
Type: files; Name: "{app}\.temp\*"
Type: files; Name: "{app}\assets\*"
Type: dirifempty; Name: "{app}\.temp"
Type: dirifempty; Name: "{app}\assets"
Type: files; Name: "{app}\crash_reports\*"
Type: dirifempty; Name: "{app}\crash_reports"
Type: files; Name: "{app}\lag.csv"
Type: dirifempty; Name: {app}

