import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import patoolib

 

def decompression(filename):
    """This function converts a .tbl.Z file into a .txt file."""
    input = filename+'.Z'                                           #First, we rename the file
    patoolib.extract_archive(input, outdir=".")                     #then, we uncompress it by using patoolib library
    next_file_path = os.path.splitext(filename)[0]+'.txt'           #Then we convert it into a .txt file
    os.rename(filename, next_file_path)                             #Finally, we rename it
    output_text.insert(tk.END,f"File {next_file_path} were created in directory : , {os.getcwd()}\n")   #The user is informed where is the new file

 

def drop(event):
    """This function allows a user to do a drag and drop """
    file_list = root.tk.splitlist(event.data)   #we get the list of files
    print("Fichiers déposés : ", file_list)
    for file in file_list:
        if file.endswith('.tbl.Z'):             #For each file, we use the function decompression to convert it
            decompression(os.path.splitext(file)[0])

 

root = TkinterDnD.Tk()
root.title('Conversion')

label = tk.Label(root, text='Drag and Drop Files Here', width=50, height=20)
label.pack()

output_text = tk.Text(root, width=50, height=15)
output_text.pack()

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()