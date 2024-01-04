import tkinter 
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="the_north_face_membership_registration"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def calculate_membership_fee():
    country = country_name.get()
    currency = currency_name.get()
    membership_status = membershipstatus_select.get()
    if not country or not currency:
        result_label.config(text="Please select both country and currency.")
        return

    # Validate country and currency selection
    valid_countries = ['Malaysia', 'United Kingdom', 'Singapore']
    valid_currencies = {
        'Malaysia': ['Malaysian Ringgit'],
        'United Kingdom': ['Sterling'],
        'Singapore': ['Singapore dollar'],
    }

    if country not in valid_countries:
        result_label.config(text="Please select a valid country.")
        return

    if currency not in valid_currencies.get(country, []):
        result_label.config(text="Match currency for the chosen country.")
        return
    
    membership_fee = 0

    if country == 'Malaysia':
        membership_fee += 200.00
    elif country == 'United Kingdom':
        membership_fee += 34.00
    elif country == 'Singapore':
        membership_fee += 57.32

    if currency == 'Malaysian Ringgit':
        membership_fee += 0
    elif currency == 'Sterling':
        membership_fee += 0
    elif currency == 'Singapore dollar':
        membership_fee += 0
    
    # Apply a discount based on the selected membership status
    if membership_status == 'Current Member':
        discount_percentage = 30
        discount_amount = (discount_percentage / 100) * membership_fee
        membership_fee -= discount_amount
    elif membership_status == 'New Member':
        discount_percentage = 5
        discount_amount = (discount_percentage / 100) * membership_fee
        membership_fee -= discount_amount

    # Display the calculated membership fee
    if country == 'Malaysia':
        result_label.config(text=f'Membership Fee: RM{membership_fee}')
    elif country == 'United Kingdom': 
        result_label.config(text=f'Membership Fee: £{membership_fee}')
    elif country == 'Singapore':
        result_label.config(text=f'Membership Fee: ${membership_fee}')
        
    FirstName = str(first_name_entry.get("1.0", "end-1c"))
    LastName = str(last_name_entry.get("1.0", "end-1c"))
    ContactNumber = str(contact_number_entry.get("1.0", "end-1c"))
    Email = str(email_entry.get("1.0", "end-1c"))
    Address = str(address_entry.get("1.0", "end-1c"))

    # Fix the SQL query and pass the actual values
    sql = "INSERT INTO membership_registration (FirstName, LastName, ContactNumber, Email, Address, country_name, currency_name, paymentmethod_name, membershipstatus_select, result_label) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (FirstName, LastName, ContactNumber, Email, Address, country, currency, paymentmethod_name.get(), membership_status, result_label.cget("text"))
    
    mycursor.execute(sql, val)
    mydb.commit()

root = tkinter.Tk()
root.title('TheNorthFace Membership Registration')
root.geometry('1520x820')
root.configure(bg="#CDC0B0")

title_label1 =tkinter.Label(root, text='M', font=('clothing logos tfb', 143), fg='#8B8378', bg='#CDC0B0')
title_label2 =tkinter.Label(root, text='MEMBERSHIP REGISTRATION', font=('Times New Roman', 66), fg='#8B8378', bg='#CDC0B0')


title_label1.grid(row=0, column=0, sticky='w')
title_label2.grid(row=0, column=1, sticky='w')

user1 =tkinter.Label(root, text='REQUIRED INFORMATION', font=('Times New Roman', 26), fg='#CDC0B0', bg='#8B8378')
FirstName =tkinter.Label(root, text='First Name', font=('Times New Roman', 26), fg='#8B8378', bg='#CDC0B0')
LastName =tkinter.Label(root, text='Last Name', font=('Times New Roman', 26), fg='#8B8378', bg='#CDC0B0')
ContactNumber =tkinter.Label(root, text='Contact Number', font=('Times New Roman', 26), fg='#8B8378', bg='#CDC0B0')
Email =tkinter.Label(root, text='Email', font=('Times New Roman', 26), fg='#8B8378', bg='#CDC0B0')
Address =tkinter.Label(root, text='Address', font=('Times New Roman', 26), fg='#8B8378', bg='#CDC0B0')


user1.grid(row=1, column=0, columnspan=2, sticky='ew')
FirstName.grid(row=2, column=0, ipady=10, sticky='ew')
LastName.grid(row=3, column=0, ipady=10, sticky='ew')
ContactNumber.grid(row=4, column=0, ipady=10, sticky='ew')
Email.grid(row=5, column=0, ipady=10, sticky='ew')
Address.grid(row=6, column=0, ipady=10, sticky='ew')

first_name_entry =tkinter.Text(root, font=('Times New Roman', 20), height=1, width=32, fg='#8B7D6B', bg='#EEDFCC')
last_name_entry =tkinter.Text(root, font=('Times New Roman', 20), height=1, width=32, fg='#8B7D6B', bg='#EEDFCC')
contact_number_entry =tkinter.Text(root, font=('Times New Roman', 20), height=1, width=32, fg='#8B7D6B', bg='#EEDFCC')
email_entry =tkinter.Text(root, font=('Times New Roman', 20), height=1, width=32, fg='#8B7D6B', bg='#EEDFCC')
address_entry =tkinter.Text(root, font=('Times New Roman', 20), height=1, width=32, fg='#8B7D6B', bg='#EEDFCC')


first_name_entry.grid(row=2, column=1, ipadx=0,pady=0, sticky='w')
last_name_entry.grid(row=3, column=1, padx=0,pady=0, sticky='w')
contact_number_entry.grid(row=4, column=1, padx=0,pady=0, sticky='w')
email_entry.grid(row=5, column=1, padx=0,pady=0, sticky='w')
address_entry.grid(row=6, column=1, padx=0,pady=0, sticky='w')


country = tkinter.Label(root, text='Choose Country', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
country.grid(row=2, column=1, ipady=20, sticky='s')
country_name= ttk.Combobox(root, values=['Malaysia', 'United Kingdom', 'Singapore'], font=('Times New Roman', 20), height=20, width=30)
country_name.grid(row=2, column=1,sticky='e')


currency = tkinter.Label(root, text='Choose Currency', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
currency.grid(row=3, column=1, ipady=30, sticky='s')


currency_name = ttk.Combobox(root, values=['Malaysian Ringgit', 'Sterling', 'Singapore dollar',], font=('Times New Roman', 20), height=20, width=30)
currency_name.grid(row=3, column=1, sticky='e')


paymentmethod = tkinter.Label(root, text='Payment Method', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
paymentmethod.grid(row=4, column=1, ipady=30, )


paymentmethod_name = ttk.Combobox(root, values=['Financial Process Exchange (FPX)', 'PayPal', 'VisaCard', 'Google Pay', 'Touch n Go eWallet'], font=('Times New Roman', 20), height=20, width=30)
paymentmethod_name.grid(row=4, column=1, sticky='e')


membershipstatus = tkinter.Label(root, text='Membership Status', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
membershipstatus.grid(row=5, column=1, ipady=30)


membershipstatus_select = ttk.Combobox(root, values=['New Member', 'Current Member'], font=('Times New Roman', 20), height=20, width=30)
membershipstatus_select.grid(row=5, column=1, sticky='e')



country = tkinter.Label(root, text='Choose Country', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
country.grid(row=2, column=1, ipady=20, sticky='s')
currency = tkinter.Label(root, text='Choose Currency', font=('Times New Roman', 30), fg='#8B8378', bg='#CDC0B0')
currency.grid(row=3, column=1, ipady=30, sticky='s')

country_name= ttk.Combobox(root, values=['Malaysia', 'United Kingdom', 'Singapore'], font=('Times New Roman', 20), height=20, width=30)
country_name.grid(row=2, column=1,sticky='e')
currency_name = ttk.Combobox(root, values=['Malaysian Ringgit', 'Sterling', 'Singapore dollar'], font=('Times New Roman', 20), height=20, width=30)
currency_name.grid(row=3, column=1, sticky='e')

result_label = tkinter.Label(root, text='MEMBERSHIP PRICE', font=('Times New Roman', 20), fg='#CDC0B0', bg='#8B7D6B')
result_label.grid(row=6, column=1, sticky='e', ipadx=85)

calculate_button = tkinter.Button(root, text="Calculate Fee", command=calculate_membership_fee, font=('Times New Roman', 20), fg='#8B7D6B', bg='#EEDFCC')
calculate_button.grid(row=6, column=1, pady=20)

#register_button = tkinter.Button(root, text="REGISTER", command = INSERT_DATA, font= ('Times New Roman', 20), bg="#8B8378", fg="#CDC0B0" )
#register_button.grid(row=7, column=2, padx=20, pady= 20) 


root.mainloop()