from tkinter import *
from tkinter import filedialog
from template_mailer import email_servers,email_template
import os
import pandas


global email_list
class receiver:
    def copy_from_text(self,window):
        self.clear_window(window)
        print("copy from text")
        text_data_label=Label(text="Enter the data of users")
        text_data_label.grid(row=1,column=0)
        text_data_entry=Entry(width=50)
        text_data_entry.grid(row=1,column=1)


        text_separator_label=Label(text="Enter the separator ")
        text_separator_label.grid(row=2,column=0)
        text_separator_entry=Entry(width=10)
        text_separator_entry.grid(row=2,column=1)

        proceed_but=Button(text="Proceed", command=lambda: self.separator(text_data_entry.get(),text_separator_entry.get()))
        proceed_but.grid(row=3, column=1)
        
            
    def separator(self,email_data,separate_str):
        global email_list
        email_list=email_data.split(separate_str)

        self.close_window()


    file_path=""

    def read_csv(self,window):
        
        self.clear_window(window)

        print("read csv")
        csv_data_label=Label(text="Upload the user data file")
        csv_data_label.grid(row=1,column=0)
        csv_data_entry =Button(text="Upload File", command=self.upload_file)
        csv_data_entry.grid(row=1,column=1)
        


        csv_data_label=Label(text="Enter the name of email containing data (Case Sensitive)")
        csv_data_label.grid(row=2,column=0)
        csv_data_entry=Entry(width=50)
        csv_data_entry.grid(row=2,column=1)

        global file_path
        proceed_but=Button(text="Proceed", command=lambda: self.file_process(file_path, csv_data_entry.get()))
        proceed_but.grid(row=3, column=1) 

    def upload_file(self):
        data_file = filedialog.askopenfilename()
        print("File selected:", data_file) 
        
        global file_path
        file_path=data_file

    def file_process(self,data_file_path,col_name):
        if data_file_path:
            if os.path.exists(data_file_path):
                data=pandas.read_csv(data_file_path)
                global email_list
                email_list = data[col_name].tolist()
                
                self.close_window()
                

            else:
                print("File does not exist")
        else:
            print("No file selected")




    def clear_window(self,window):
        for widget in window.winfo_children():
            widget.destroy()



    receiver_options=[
        {"Name":"copy from text","action":copy_from_text},
        {"Name":"read csv/excel sheet","action":read_csv},
    ]




    def close_window(self):
        self.window.destroy()
        if self.callback:
            self.callback(email_list)
    
    def receiver_data(self,selection):
        for option in self.receiver_options:
            if selection==option["Name"]:
                option["action"](self,self.window)
                
    def __init__(self,callback=None):

        self.window=Tk()
        self.window.title("Email Receiver")
        self.callback = callback
        rcvr_data_type = StringVar(self.window)
        lbl1=Label(text="Select the data Type for the receiver's data")
        lbl1.grid(row=0,column=0)
        dropdown = OptionMenu(self.window, rcvr_data_type, *[option["Name"] for option in self.receiver_options],
                       command=lambda selected_value: self.receiver_data(selected_value))
        rcvr_data_type.set("Select an option")  # Set the default value
        dropdown.grid(row=1,column=0,columnspan=3)
        self.window.mainloop()

        
   

        