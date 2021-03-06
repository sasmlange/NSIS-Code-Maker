import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

SaveFile = ""
OpenWith = False

def ChangeInstallerDirectory():
    NewInstallerDirectory = filedialog.askdirectory()
    NewInstallerDirectory = NewInstallerDirectory.replace("/", "\\")

    InstallerDirectory.delete(0, tk.END)
    InstallerDirectory.insert(0, NewInstallerDirectory)


def ChangeLicense():
    NewLicenseFile = filedialog.askopenfilename(filetypes=[("All Accepted Files", "*.txt *.rtf"),
                                                           ("Text Documents", "*.txt"),
                                                           ("Rich Text File", "*.rtf"),
                                                           ("All Files", "*")])

    NewLicenseFile = NewLicenseFile.replace("/", "\\")

    License.delete(0, tk.END)
    License.insert(0, NewLicenseFile)


def ChangeOutputFile():
    NewOutputFile = filedialog.asksaveasfilename(filetypes=[("NSIS Script Files", "*.nsi"), ("All Files", "*.*")])
    NewOutputFile = NewOutputFile.replace("/", "\\")

    OutputFile.delete(0, tk.END)
    OutputFile.insert(0, NewOutputFile)


def Generate():
    Format = (
        License.get(), Name.get(), ExeName.get(), ShortName.get(), Name.get(),
        ExeOnShortcut.get(), Name.get(), InstallerDirectory.get(), Name.get(), Name.get()
    )
    with open("InstallerTemplate.nsi") as File:
        InstallerText = File.read() % Format


    try:
        with open(OutputFile.get(), "w") as File:
            File.write(InstallerText)
    except:
        messagebox.showerror("Script Generator", "Output Path Not Found")
        return

    messagebox.showinfo("Script Generator", "The installer has been created!")


def Open():
    global SaveFile, OpenWith
    if OpenWith == False:
        SaveFile = filedialog.askopenfilename(filetypes=[("NSIS Code Maker Files", "*.nscm"), ("All Files", "*.*")])
        if SaveFile == "":
            return
    OpenWith = False
    with open(SaveFile) as File:
        Code = File.read()
    Code = Code.split(";")

    InstallerDirectory.delete(0, tk.END)
    InstallerDirectory.insert(0, Code[0])

    OutputFile.delete(0, tk.END)
    OutputFile.insert(0, Code[1])

    Name.delete(0, tk.END)
    Name.insert(0, Code[2])

    ShortName.delete(0, tk.END)
    ShortName.insert(0, Code[3])

    License.delete(0, tk.END)
    License.insert(0, Code[4])

    ExeOnShortcut.delete(0, tk.END)
    ExeOnShortcut.insert(0, Code[5])

    ExeName.delete(0, tk.END)
    ExeName.insert(0, Code[6])

def SaveAs():
    global SaveFile
    SaveFile = filedialog.asksaveasfilename(filetypes=[("NSIS Code Maker Files", "*.nscm"), ("All Files", "*.*")])
    if SaveFile == "":
        return
    with open(SaveFile, "w") as File:
        File.write(f"{InstallerDirectory.get()};{OutputFile.get()};{Name.get()};{ShortName.get()};{License.get()};{ExeOnShortcut.get()};{ExeName.get()}")

def Save():
    global SaveFile
    if SaveFile == "":
        SaveAs()
        return

    with open(SaveFile, "w") as File:
        File.write(f"{InstallerDirectory.get()};{OutputFile.get()};{Name.get()};{ShortName.get()};{License.get()};{ExeOnShortcut.get()};{ExeName.get()}")


Window = tk.Tk()
Window.title("NSIS Code Maker")

MenuBar = tk.Menu(Window)
Window.config(menu=MenuBar)

MenuBar.add_command(label="Open...", command=Open)
MenuBar.add_command(label="Save", command=Save)
MenuBar.add_command(label="Save As...", command=SaveAs)

Label1 = ttk.Label(text="Installer Directory: ")
Label1.grid(row=1, column=1)

InstallerDirectory = ttk.Entry()
InstallerDirectory.grid(row=1, column=2)

InstallerDirectoryButton = ttk.Button(text="...", command=ChangeInstallerDirectory)
InstallerDirectoryButton.grid(row=1, column=3)

Label2 = ttk.Label(text="Output File: ")
Label2.grid(row=2, column=1)

OutputFile = ttk.Entry()
OutputFile.grid(row=2, column=2)

OutputDirectoryButton = ttk.Button(text="...", command=ChangeOutputFile)
OutputDirectoryButton.grid(row=2, column=3)

Label3 = ttk.Label(text="App Name: ")
Label3.grid(row=3, column=1)

Name = ttk.Entry()
Name.grid(row=3, column=2)

Label4 = ttk.Label(text="App Short Name: ")
Label4.grid(row=4, column=1)

ShortName = ttk.Entry()
ShortName.grid(row=4, column=2)

Label5 = ttk.Label(text="License: ")
Label5.grid(row=5, column=1)

License = ttk.Entry()
License.grid(row=5, column=2)

LicenseButton = ttk.Button(text="...", command=ChangeLicense)
LicenseButton.grid(row=5, column=3)

Label6 = ttk.Label(text="Execute on Shortcut: ")
Label6.grid(row=6, column=1)

ExeOnShortcut = ttk.Entry()
ExeOnShortcut.grid(row=6, column=2)

Label7 = ttk.Label(text="EXE Name: ")
Label7.grid(row=7, column=1)

ExeName = ttk.Entry()
ExeName.grid(row=7, column=2)

SubmitButton = ttk.Button(text="Generate", command=Generate)
SubmitButton.grid(row=8, column=2)

Window.mainloop()

if len(sys.argv) > 1:
    SaveFile = sys.argv[1]
    OpenWith = True
    Open()
