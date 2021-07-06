import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def ChangeInstallerDirectory():
    NewInstallerDirectory = filedialog.askdirectory()
    NewInstallerDirectory = NewInstallerDirectory.replace("/", "\\")

    InstallerDirectory.delete(0, tk.END)
    InstallerDirectory.insert(0, NewInstallerDirectory)


def ChangeOutputFile():
    NewOutputFile = filedialog.asksaveasfilename(filetypes=[("NSIS Script Files", "*.nsi"), ("All Files", "*.*")])
    NewOutputFile = NewOutputFile.replace("/", "\\")

    OutputFile.delete(0, tk.END)
    OutputFile.insert(0, NewOutputFile)


def Generate():
    Format = (
        ExeName.get(), ShortName.get(), Name.get(), ShortName.get(),
        Name.get(), InstallerDirectory.get(), Name.get(), Name.get()
    )
    with open("InstallerTemplate.nsi") as File:
        InstallerText = File.read() % Format


    try:
        with open(OutputFile.get(), "w") as File:
            File.write(InstallerText)
    except:
        messagebox.showerror("Error", "Output Path Not Found")
        return

    messagebox.showinfo("Installer Created!", "The installer has been created!")


Window = tk.Tk()
Window.title("NSIS Code Maker")

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

Label5 = ttk.Label(text="Execute on Shortcut: ")
Label5.grid(row=5, column=1)

ExeOnShortCut = ttk.Entry()
ExeOnShortCut.grid(row=5, column=2)

Label6 = ttk.Label(text="EXE Name: ")
Label6.grid(row=6, column=1)

ExeName = ttk.Entry()
ExeName.grid(row=6, column=2)

SubmitButton = ttk.Button(text="Generate", command=Generate)
SubmitButton.grid(row=6, column=2)

Window.mainloop()
