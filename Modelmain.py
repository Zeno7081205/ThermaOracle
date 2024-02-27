import math
from sklearn import linear_model
import pandas as pd
import math
from tkinter import *
from tkinter import filedialog


def model(file):
    df = pd.read_csv(file)
    reg = linear_model.LinearRegression()
    # reg.fit(df[['Hour 0: Humidity','Hour 0: Wind Speed (km/h)','Hour 0: Wind Bearing (degrees)','Hour 0: Visibility (km)','Hour 0: Pressure (millibars)',
    #             'Hour 1: Humidity','Hour 1: Wind Speed (km/h)','Hour 1: Wind Bearing (degrees)','Hour 1: Visibility (km)','Hour 1: Pressure (millibars)',
    #             'Hour 2: Humidity','Hour 2: Wind Speed (km/h)','Hour 2: Wind Bearing (degrees)','Hour 2: Visibility (km)','Hour 2: Pressure (millibars)',
    #             'Hour 3: Humidity','Hour 3: Wind Speed (km/h)','Hour 3: Wind Bearing (degrees)','Hour 3: Visibility (km)','Hour 3: Pressure (millibars)',
    #             'Hour 4: Humidity','Hour 4: Wind Speed (km/h)','Hour 4: Wind Bearing (degrees)','Hour 4: Visibility (km)','Hour 4: Pressure (millibars)',
    #             'Hour 5: Humidity','Hour 5: Wind Speed (km/h)','Hour 5: Wind Bearing (degrees)','Hour 5: Visibility (km)','Hour 5: Pressure (millibars)']], df['Temperature (C)'])
  
    reg.fit(df[['Apparent Temperature (C)','Humidity','Wind Speed (km/h)','Wind Bearing (degrees)','Visibility (km)','Pressure (millibars)']],df['Temperature (C)'])
    
    
    root = Tk()
    root.title("Predict")
    
    def Predict(a, b, c, d, e, f):
        prediction = reg.predict([[a, b, c, d, e, f]])
        medals=str(math.floor(prediction[0]))
        l7=Label(root,text="Medals : "+medals)
        l7.grid(row=8,column=0,columnspan=2)
    
    def Get():
        a = int(e1.get())
        b = int(e2.get())
        c = float(e3.get())
        d = float(e4.get())
        e = float(e5.get())
        f = float(e6.get())
        Predict(a, b, c, d, e, f)
    def Test():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        df=pd.read_csv(file_path)
        total_rows = df.shape[0]
        print(total_rows)
        a=8
        row_index = 0
        for i in range(0,total_rows):
           
            # columns_of_interest = ['Hour 0: Humidity','Hour 0: Wind Speed (km/h)','Hour 0: Wind Bearing (degrees)','Hour 0: Visibility (km)','Hour 0: Pressure (millibars)',
            #     'Hour 1: Humidity','Hour 1: Wind Speed (km/h)','Hour 1: Wind Bearing (degrees)','Hour 1: Visibility (km)','Hour 1: Pressure (millibars)',
            #     'Hour 2: Humidity','Hour 2: Wind Speed (km/h)','Hour 2: Wind Bearing (degrees)','Hour 2: Visibility (km)','Hour 2: Pressure (millibars)',
            #     'Hour 3: Humidity','Hour 3: Wind Speed (km/h)','Hour 3: Wind Bearing (degrees)','Hour 3: Visibility (km)','Hour 3: Pressure (millibars)',
            #     'Hour 4: Humidity','Hour 4: Wind Speed (km/h)','Hour 4: Wind Bearing (degrees)','Hour 4: Visibility (km)','Hour 4: Pressure (millibars)',
            #     'Hour 5: Humidity','Hour 5: Wind Speed (km/h)','Hour 5: Wind Bearing (degrees)','Hour 5: Visibility (km)','Hour 5: Pressure (millibars)']
            columns_of_interest=['Apparent Temperature (C)','Humidity','Wind Speed (km/h)','Wind Bearing (degrees)','Visibility (km)','Pressure (millibars)']    
            specific_values = df.loc[row_index, columns_of_interest]
            specific_values_list = []
            for value in specific_values:
                 specific_values_list.append(value)
            print(specific_values_list)
            prediction = reg.predict([specific_values_list])
            temp=str((prediction[0]))
            l7=Label(root,text="Temperature : "+temp)
            l7.grid(row=a,column=0,columnspan=2)
            a+=1
            row_index+=1


        
    
    l1 = Label(root, text="athletes : ")
    l1.grid(row=0, column=0)
    e1 = Entry(root, width=30)
    e1.grid(row=0, column=1)
    
    l2 = Label(root, text="events   : ")
    l2.grid(row=1, column=0)
    e2 = Entry(root, width=30)
    e2.grid(row=1, column=1)
    
    l3 = Label(root, text="age      : ")
    l3.grid(row=2, column=0)
    e3 = Entry(root, width=30)
    e3.grid(row=2, column=1)
    
    l4 = Label(root, text="height   : ")
    l4.grid(row=3, column=0)
    e4 = Entry(root, width=30)
    e4.grid(row=3, column=1)
    
    l5 = Label(root, text="weight   :")
    l5.grid(row=4, column=0)
    e5 = Entry(root, width=30)
    e5.grid(row=4, column=1)
    
    l6 = Label(root, text="prevMedals :  ")
    l6.grid(row=5, column=0)
    e6 = Entry(root, width=30)
    e6.grid(row=5, column=1)
    
    b1 = Button(root, text="Predict", padx=20, pady=15, command=Get)
    b2=Button(root,text="Use test data",pady=15,padx=20,command=Test)
    b1.grid(row=6, column=0, columnspan=2)
    b2.grid(row=7, column=0, columnspan=2)
    
    root.mainloop()


    