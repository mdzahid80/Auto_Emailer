# tkinter GUI
from tkinter import *
from tkinter import simpledialog,messagebox,Text
from template_mailer import email_servers,email_template
from receiver_panel import receiver
import smtplib





custom_email_data={}
def custom_email():
    cust_mail_wnd=Tk()
    cust_mail_wnd.geometry('600x600')

    temp_label2=Label(cust_mail_wnd, text="Write a label for your email")
    temp_label2.grid(row=0,column=0)

    cust_email_label = Entry(cust_mail_wnd,width=40)
    cust_email_label.grid(row=0,column=1)

    temp_label1=Label(cust_mail_wnd, text="Write Your EMail")
    temp_label1.grid(row=1,column=0)

    def insert_default_text():
        default_text = """Subject:

Body:"""
        cust_email_textbox.delete(1.0, END)  # Clear any existing content
        cust_email_textbox.insert(1.0, default_text)

    cust_email_textbox = Text(cust_mail_wnd, height=10, width=40)
    cust_email_textbox.grid(row=1,column=1)
    insert_default_text()

    def save_cust_mail():
        mail_label=cust_email_label.get()
        mail_content=cust_email_textbox.get("1.0", "end-1c")
        cust_mail_wnd.destroy()
        global custom_email_data 
        custom_email_data = {"text": mail_content, "label": mail_label}
        print(custom_email_data) 

    
    save_btn=Button(cust_mail_wnd, text="Save & Proceed",command= save_cust_mail)
    save_btn.grid(row=2, column=0, columnspan=2)


sender_smtp_srvr=""
def selected_option_srvr(selection):
    print("Selected option:", selection)
    for server in email_servers:
        if server["Name"] == selection:
            global sender_smtp_srvr
            sender_smtp_srvr=server["server"]


sender_mail_tmplt=""
def selected_option_tmplt(selection):
    if selection == "Custom":
        custom_email()
    else:
        global sender_mail_tmplt
        for mail in email_template:
            if mail["label"]==selection:
                sender_mail_tmplt=mail["label"]
                
def send_email(email_list):
    get_data()

    for mail in email_list:
        with smtplib.SMTP(email_server_server,email_server_port) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_pass)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=mail,
                                msg=email_body)
        print("successfully sent to ",mail)
        



def new_window():
    window.destroy()

    new=receiver(callback=handle_receiver_closure)

    
    print("working fine")

def handle_receiver_closure(email_list):

    print("Received email list:", email_list)
    send_email(email_list)

    


def proceed():
    global sender_name
    global sender_email
    global sender_pass
    sender_name = sender_name_entry.get()
    sender_email = sender_email_entry.get()
    sender_pass = sender_pass_entry.get()
    
    if sender_name=='' or sender_email=='' or sender_pass=='':
        messagebox.showinfo(title="An Error Occured", message="Required fields can't be empty")
    else:
        new_window()
    

def get_data():
    global email_server_name
    global email_server_server
    global email_server_port
    global email_body

    for i in email_servers:
        if i['Name']==mail_srvr_drpdn.get():
            email_server_name=i['Name']
            email_server_server=i['server']
            email_server_port=i['port']

    x=1
    for i in email_template:
        if i['label']==mail_temp_drpdn.get():
            email_body=i['text']
            x=0
    if x==1:
        email_body=custom_email_data["text"]

window = Tk()
window.title("The Emailer-")
window.config(padx=20, pady=20)

canvas = Canvas(width=600, height=300)

sender_name_lbl=Label(text="Sender name:*", font=("Arial", 12), bg="white", fg="black", padx=10, pady=5)
sender_name_lbl.grid(row=1,column=0)

sender_email_lbl=Label(text="Email/Username:*")
sender_email_lbl.grid(row=2,column=0)

sender_pass_lbl=Label(text="Password:*")
sender_pass_lbl.grid(row=3,column=0)


sender_name_entry=Entry(width=35)
sender_name_entry.grid(row=1,column=1,columnspan=2)

sender_email_entry=Entry(width=35)
sender_email_entry.grid(row=2,column=1,columnspan=2)

sender_pass_entry=Entry(width=35)
sender_pass_entry.grid(row=3,column=1,columnspan=2)


mail_srvr_drpdn = StringVar(window)

dropdown = OptionMenu(window, mail_srvr_drpdn, *[server["Name"] for server in email_servers], command=selected_option_srvr)
mail_srvr_drpdn.set("Select an option")  
dropdown.grid(row=5,column=0)


mail_temp_drpdn = StringVar(window)
# Create a dropdown menu
dropdown = OptionMenu(window, mail_temp_drpdn,"Custom", *[mail["label"] for mail in email_template], command=selected_option_tmplt)
mail_temp_drpdn.set("Select an option") 
dropdown.grid(row=5,column=1)


next_page = Button(window , text='Next', command=proceed)
next_page.grid(row=6,column=1)


window.mainloop()
