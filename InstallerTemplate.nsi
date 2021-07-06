!include "MUI.nsh"

!define MUI_ABORTWARNING # This will warn the user if they exit from the installer.

!insertmacro MUI_PAGE_WELCOME # Welcome to the installer page.
!insertmacro MUI_PAGE_DIRECTORY # In which folder install page.
!insertmacro MUI_PAGE_INSTFILES # Installing page.
!insertmacro MUI_PAGE_FINISH # Finished installation page.

!insertmacro MUI_LANGUAGE "English"

Name "%s" # Name of the installer (usually the name of the application to install).
OutFile "%s" # Name of the installer's file.
InstallDir "$LOCALAPPDATA\Programs\%s" # Default installing folder

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
    CreateShortcut "$SMPROGRAMS\%s.lnk" "$INSTDIR\%s"
    CreateShortcut "$SMPROGRAMS\%s Uninstall.lnk" "$INSTDIR\uninstall.exe"

    File /r "%s\*"

SectionEnd
 
# uninstaller section start
Section "uninstall"
 
    # first, delete the uninstaller
    Delete "$INSTDIR\uninstall.exe"
 
    # second, remove the link from the start menu
    Delete "$SMPROGRAMS\%s.lnk"
    Delete "$SMPROGRAMS\%s Uninstall.lnk"
 
    Delete $INSTDIR

# uninstaller section end
SectionEnd