# define name of installer
OutFile "InstallNsisCodeMakerV1"
 
# define installation directory
InstallDir $LOCALAPPDATA\Programs\NsisCodeMaker
 
# For removing Start Menu shortcut in Windows 7
RequestExecutionLevel user
 
# start default section
Section
 
    # set the installation directory as the destination for the following actions
    SetOutPath $INSTDIR
 
    # create the uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
 
    # create a shortcut named "new shortcut" in the start menu programs directory
    # point the new shortcut at the program uninstaller
    CreateShortcut "$SMPROGRAMS\NSIS Code Maker.lnk" "$INSTDIR\NsisCodeMaker.exe"
    CreateShortcut "$SMPROGRAMS\NSIS Code Maker Uninstall.lnk" "$INSTDIR\uninstall.exe"

    File /r "C:\AllFiles\MaxPyCharm\NSIS-Code-Maker\EXE\*"

SectionEnd
 
# uninstaller section start
Section "uninstall"
 
    # first, delete the uninstaller
    Delete "$INSTDIR\uninstall.exe"
 
    # second, remove the link from the start menu
    Delete "$SMPROGRAMS\NSIS Code Maker.lnk"
    Delete "$SMPROGRAMS\NSIS Code Maker Uninstall.lnk"
 
    Delete $INSTDIR

# uninstaller section end
SectionEnd