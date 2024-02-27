from tkinter import filedialog
from Modelmain import *
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        print("Selected file:", file_path)
        
    model(file_path)   
 
