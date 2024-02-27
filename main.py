from tkinter import *
from sklearn import linear_model
import pandas as pd
import math
import os
from fileSelect import *


# Creating a main window
root=Tk()
root.title('Choose a File')
choose_button =Button(root, text="Choose File", command=choose_file)
choose_button.pack(pady=10)






root.mainloop()