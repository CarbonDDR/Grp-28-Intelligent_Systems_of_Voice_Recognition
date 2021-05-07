import os
import platform
from src.va import speak, ask
import tkinter as tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from pathlib import Path


def merger_call():
    merger = PyPDF2.PdfFileMerger()
    list1 = []

    def open_file(files):
        filepath = askopenfilename(
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if not (filepath and Path(filepath).exists()):
            return
        files.append(filepath)
        # list out all filenames
        lbl_items["text"] = "\n".join(str(f) for f in files)
        if len(files) >= 2 and btn_merge["state"] == "disabled":
            btn_merge["state"] = "normal"

    def merge_pdfs(files):
        for f in files:
            merger.append(PyPDF2.PdfFileReader(open(f, "rb")))

        output_filename = ent_output_name.get()

        if not output_filename:
            output_filename = "Untitled.pdf"
        elif ".pdf" not in output_filename:
            output_filename += ".pdf"
        merger.write(output_filename)

    window = tk.Tk()
    window.title("PDFMerger By KBG")
    window.geometry("500x500")
    # not allowed resizing x y direction
    window.resizable(0, 0)

    # --- Ask open files ---
    fr_bg1 = tk.Frame(window, bd=3)
    lbl_open = tk.Label(fr_bg1, text="Please choose PDFs to join: (2 and above)")
    lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    btn_open = tk.Button(fr_bg1, text="Open file(s)", command=lambda: open_file(list1))
    btn_open.grid(row=1, column=0, sticky="ew", padx=5)
    lbl_items = tk.Label(fr_bg1, text="")
    lbl_items.grid(row=2, column=0, pady=5)
    fr_bg1.pack()

    # --- Button to merge PDFs ---
    fr_bg2 = tk.Frame(window, bd=3)
    lbl_to_merge = tk.Label(fr_bg2, text="Merge selected files (in PDF)")
    lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

    ent_output_name = tk.Entry(master=fr_bg2, width=7)
    ent_output_name.grid(row=1, column=0, sticky="ew")

    btn_merge = tk.Button(
        fr_bg2, text="Merge PDF", state="disabled", command=lambda: merge_pdfs(list1)
    )
    btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    fr_bg2.pack()

    # --- Button to exit ---
    btn_exit = tk.Button(window, text="Exit", command=window.destroy, bd=2)
    btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

    window.mainloop()


def open_merger(line):
    merger_call()


def openTextEditor():
    pt = platform.system()
    pt = pt.lower()
    if pt == "win32" or pt == "windows":
        os.system("notepad")
    elif pt == "linux" or pt == "linux2":
        os.system("gedit")
    elif pt == "darwin":
        os.system("open /Applications/Pages.app")


def open_caller(line):
    openTextEditor()


hash_dict = {
    "open notepad": open_caller,
    "start notepad": open_caller,
    "open text editor": open_caller,
    "start text editor": open_caller,
    "open gedit": open_caller,
    "start gedit": open_caller,
    "notepad": open_caller,
    "notepad start": open_caller,
    "notepad open": open_caller,
    "text editor": open_caller,
    "gedit open": open_caller,
    "gedit start": open_caller,
    "gedit": open_caller,
    "text editor start": open_caller,
    "text editor open": open_caller,
    "merge pdf": open_merger,
    "pdf merge": open_merger,
    "merge pdfs": open_merger,
    "pdfs merge": open_merger,
    "combine pdf": open_merger,
    "combine pdfs": open_merger,
}
# open_merger("open")
