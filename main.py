from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib

def validate_name(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action == '1':  # If inserting
        if not text.isalpha() and text != ' ':
            messagebox.showwarning("Warning", "Only letters and spaces are allowed")
            return False
        if len(value_if_allowed) > 20:
            messagebox.showwarning("Warning", "Maximum length is 20 characters")
            return False
    elif action == '0':  # If deleting
        if len(value_if_allowed) < 3 and value_if_allowed != "":
            messagebox.showwarning("Warning", "Minimum length is 3 characters")
            return False
    return True
   
def clearbtn():
    bathsoapentry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    hairSparyEntry.delete(0,END)
    bodylotionentry.delete(0,END)

    teaPowerEntry.delete(0,END)
    sugarEntry.delete(0,END)
    oilEntry.delete(0,END)
    riceEntry.delete(0,END)
    wheatEntry.delete(0,END)
    DaalEntry.delete(0,END)

    maazaEntry.delete(0,END)
    spriteEntry.delete(0,END)
    frootiEntry.delete(0,END)
    thumbsupEntry.delete(0,END)
    cococolaEntry.delete(0,END)
    pepsiEntry.delete(0,END)

    bathsoapentry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairGelEntry.insert(0,0)
    hairSparyEntry.insert(0,0)
    bodylotionentry.insert(0,0)

    teaPowerEntry.insert(0,0)
    sugarEntry.insert(0,0)
    oilEntry.insert(0,0)
    riceEntry.insert(0,0)
    wheatEntry.insert(0,0)
    DaalEntry.insert(0,0)

    maazaEntry.insert(0,0)
    spriteEntry.insert(0,0)
    frootiEntry.insert(0,0)
    thumbsupEntry.insert(0,0)
    cococolaEntry.insert(0,0)
    pepsiEntry.insert(0,0)

    cosmeticEntry.delete(0,END)
    groceryspiceEntry.delete(0,END)
    drincksspiceEntry.delete(0,END)

    cosmeticTaxEntry.delete(0,END)
    groceryspiceTaxEntry.delete(0,END)
    drincksspicetaxEntry.delete(0,END)

    textarea.delete(1.0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)






def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderslentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderslentry.get(),recieverentry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=windows1)
            windows1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=windows1)

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error',"Bill is empty")
    else:
        windows1=Toplevel()
        windows1.grab_set()
        windows1.title('Send Email')
        windows1.config(bg='black')
        windows1.resizable(0,0)
        

        senderframe=LabelFrame(windows1,text='SENDER',font=('poppins',16,'bold'),bg='black',fg='white')
        senderframe.grid(row=0,column=0,padx=50,pady=20)

        sendersllabel=Label(senderframe,text="Sender's Email",font=('poppins',16,'bold'),bg='black',fg='white')
        sendersllabel.grid(row=0,column=0,padx=10,pady=10)
        senderslentry=Entry(senderframe,font=('poppins',18,'bold'),bd=6,width=18,relief='groove')
        senderslentry.grid(row=0,column=1,padx=40,pady=10)

        passwordlabel=Label(senderframe,text="Password",font=('poppins',16,'bold'),bg='black',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=10)
        passwordentry=Entry(senderframe,font=('poppins',18,'bold'),bd=6,width=18,relief='groove',show='*')
        passwordentry.grid(row=1,column=1,padx=10,pady=10)

        recipientframe=LabelFrame(windows1,text='RECIPIENT',font=('poppins',16,'bold'),bg='black',fg='white')
        recipientframe.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientframe,text="Email Address",font=('poppins',16,'bold'),bg='black',fg='white')
        recieverlabel.grid(row=0,column=0,padx=10,pady=10)
        recieverentry=Entry(recipientframe,font=('poppins',18,'bold'),bd=6,width=18,relief='groove')
        recieverentry.grid(row=0,column=1,padx=40,pady=10)

        messagelabel=Label(recipientframe,text="Message",font=('poppins',16,'bold'),bg='black',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=10)

        email_textarea=Text(recipientframe,font=('poppins',16,'bold'),bd=2,relief='sunken',width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t','\t'))

        send_button=Button(windows1,text="SEND",font=('poppins',16,'bold'),width=15,command=send_gmail)
        send_button.grid(row=2,column=0,pady=20)

    windows1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')
    

if not os.path.exists('bills'):
    os.mkdir('bills')
billnumber=random.randint(500,1000)
def save_bill():
    result=messagebox.askyesno('confirm',"Do you want to save the bill?")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'{billnumber} is saved successfully')
def billarea():
    textarea.delete(1.0,END)
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror("Error","Customer details required")
    elif cosmeticEntry.get()=='' and groceryspiceEntry.get()=='' and drincksspiceEntry.get()=='':
        messagebox.showerror("Error","No Products are selected")
    elif cosmeticEntry.get()=='0 Rs' and groceryspiceEntry.get()=='0 Rs' and drincksspiceEntry.get()=='0 Rs':
        messagebox.showerror("Error","No Products are selected")
    else:
        welcome_message=f'**Welcome {nameEntry.get()}**\n\n'
        padding_length = (text_widget_width- len(welcome_message)) // 2
        centered_message = ' ' * padding_length + welcome_message
        textarea.insert(END, centered_message)
        textarea.insert(END,f'Bill Number: {billnumber}\n\n')
        textarea.insert(END,f'Customer Name: {nameEntry.get()}\n\n')
        textarea.insert(END,f'Phone Number: {phoneEntry.get()}\n\n')
        textarea.insert(END,'=========================================\n')
        textarea.insert(END,'Product\t\tQuantity\t\tPrice\n')
        textarea.insert(END,'=========================================\n')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t{facecreamEntry.get()}\t\t{facecreamprice} Rs')
        if bathsoapentry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t{bathsoapentry.get()}\t\t{bathsoapprice} Rs')
        if hairGelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t{hairGelEntry.get()}\t\t{hairGelprice} Rs')
        if hairSparyEntry.get()!='0':
            textarea.insert(END,f'\nhair Spray\t\t{hairSparyEntry.get()}\t\t{hairSparyprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t{facewashEntry.get()}\t\t{facewashprice} Rs')
        if bodylotionentry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t{bodylotionentry.get()}\t\t{bodylotionprice} Rs')

        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t{ricePrice} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t{wheatEntry.get()}\t\t{wheatprice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t{oilEntry.get()}\t\t{oilprice} Rs')
        if DaalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t{DaalEntry.get()}\t\t{daalprice} Rs')
        if teaPowerEntry.get()!='0':
            textarea.insert(END,f'\nTea Power\t\t{teaPowerEntry.get()}\t\t{teapowerprice} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t{sugarEntry.get()}\t\t{sugarprice} Rs')

        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t{frootiEntry.get()}\t\t{frootiprice} Rs')
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t{maazaEntry.get()}\t\t{maazaprice} Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t{spriteEntry.get()}\t\t{spriteprice} Rs')
        if cococolaEntry.get()!='0':
            textarea.insert(END,f'\nCoco Cola\t\t{cococolaEntry.get()}\t\t{cococolaprice} Rs')
        if thumbsupEntry.get()!='0':
            textarea.insert(END,f'\nThumbs Up\t\t{thumbsupEntry.get()}\t\t{thumbsupprice} Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t{frootiEntry.get()}\t\t{frootiprice} Rs')
        
        textarea.insert(END,'\n----------------------------------------\n')

        if cosmeticTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t{cosmeticTaxEntry.get()}')
        if groceryspiceTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t{groceryspiceTaxEntry.get()}')
        if drincksspicetaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Soft Drinks Tax\t\t{drincksspicetaxEntry.get()}')
       
        textarea.insert(END,f'\n\nTotal Bill \t\t\t{totalbill}')
        textarea.insert(END,'\n---------------------------------------\n')
        save_bill()

def total():
    global bathsoapprice,facecreamprice,facewashprice,hairSparyprice,hairGelprice,bodylotionprice
    global ricePrice,wheatprice,daalprice,oilprice,sugarprice,teapowerprice
    global maazaprice,pepsiprice,spriteprice,thumbsupprice,cococolaprice,frootiprice
   
    global totalbill
 
    bathsoapprice=int(bathsoapentry.get())*20
    facecreamprice=int(facecreamEntry.get())*120
    facewashprice=int(facewashEntry.get())*40
    hairSparyprice=int(hairSparyEntry.get())*150
    hairGelprice=int(hairGelEntry.get())*40
    bodylotionprice=int(bodylotionentry.get())*100
    totalcosmeticprice=bathsoapprice+facecreamprice+facewashprice+hairSparyprice+hairGelprice+bodylotionprice
    cosmeticEntry.delete(0,END)
    cosmeticEntry.insert(0,str(totalcosmeticprice)+" Rs")

    cosmetictax=totalcosmeticprice*0.12
    cosmeticTaxEntry.delete(0,END)
    cosmeticTaxEntry.insert(0,str(cosmetictax)+" Rs")
     
   
    ricePrice=int(riceEntry.get())*1000
    wheatprice=int(wheatEntry.get())*50
    daalprice=int(DaalEntry.get())*200
    oilprice=int(oilEntry.get())*180
    sugarprice=int(sugarEntry.get())*40
    teapowerprice=int(teaPowerEntry.get())*80
    totalgroceryprice=ricePrice+wheatprice+daalprice+oilprice+sugarprice+teapowerprice
    groceryspiceEntry.delete(0,END)
    groceryspiceEntry.insert(0,str(totalgroceryprice)+" Rs")

    grocerytax=totalgroceryprice*0.05
    groceryspiceTaxEntry.delete(0,END)
    groceryspiceTaxEntry.insert(0,str(grocerytax)+" Rs")


    maazaprice=int(maazaEntry.get())*20
    pepsiprice=int(pepsiEntry.get())*50
    spriteprice=int(spriteEntry.get())*99
    thumbsupprice=int(thumbsupEntry.get())*180
    cococolaprice=int(cococolaEntry.get())*40
    frootiprice=int(frootiEntry.get())*80
    totalcolddrinksprice=maazaprice+pepsiprice+spriteprice+thumbsupprice+cococolaprice+frootiprice
    drincksspiceEntry.delete(0,END)
    drincksspiceEntry.insert(0,str(totalcolddrinksprice)+" Rs")

    colddrinktax=totalcolddrinksprice*0.08
    drincksspicetaxEntry.delete(0,END)
    drincksspicetaxEntry.insert(0,str(colddrinktax)+" Rs")
    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddrinktax

windows=Tk()
windows.title("Billing System")
windows.geometry("1350x850")
windows.iconbitmap("icon.ico")
headingLabel=Label(windows,text="Retail Billing System",font=('poppins',30,'bold'),bg='black',fg='gold',bd=12,relief='groove')
headingLabel.pack(fill=X)


customer_details=LabelFrame(windows,text="customer details",font=('poppins',15,'bold'),bg='black',fg='gold',bd=12,relief='groove')
customer_details.pack(fill=X,pady=10)
name_var = StringVar()
validate_name_cmd = windows.register(validate_name)

nameLabel=Label(customer_details,text="Name",font=('poppins',12,'bold'),bg='black',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=8)

nameEntry=Entry(customer_details,font=('poppins', 12, 'bold'), bd=7, width=18, textvariable=name_var, validate='key',
                     validatecommand=(validate_name_cmd, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
nameEntry.grid(row=0,column=1,padx=9,pady=10)


phoneLabel=Label(customer_details,text="Phone Number",font=('poppins',12,'bold'),bg='black',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=8)

phoneEntry = Entry(customer_details, font=('poppins', 12, 'bold'), bd=7)

phoneEntry.grid(row=0,column=3,padx=20,pady=8)

billLabel=Label(customer_details,text="Bill Number",font=('poppins',12,'bold'),bg='black',fg='white')
billLabel.grid(row=0,column=4,padx=20)


billEntry=Entry(customer_details,text="Bill Number",font=('poppins',12,'bold'),bd=7)
billEntry.grid(row=0,column=5,padx=20)

searchButton=Button(customer_details,text="search",font=('poppins',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20)


productsFrame=Frame(windows)
productsFrame.pack(fill=X)

cosmoticsFrame=LabelFrame(productsFrame,text="customer details",font=('poppins',15,'bold'),bg='black',fg='gold',bd=12,relief='groove')
cosmoticsFrame.grid(row=0,column=0)

bathsoap=Label(cosmoticsFrame,text="Bath Soap",font=('poppins',12,'bold'),bg='black',fg='white')
bathsoap.grid(row=0,column=0,padx=20,pady=8,sticky='W')

bathsoapentry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
bathsoapentry.grid(row=0,column=1,padx=9,pady=10)
bathsoapentry.insert(0,0)

facecream=Label(cosmoticsFrame,text="Face Cream",font=('poppins',12,'bold'),bg='black',fg='white')
facecream.grid(row=1,column=0,padx=20,pady=8)

facecreamEntry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
facecreamEntry.grid(row=1,column=1,padx=9,pady=10,sticky='W')
facecreamEntry.insert(0,0)

facewash=Label(cosmoticsFrame,text="Face Wash",font=('poppins',12,'bold'),bg='black',fg='white')
facewash.grid(row=2,column=0,padx=20,pady=8,sticky='W')
facewashEntry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
facewashEntry.grid(row=2,column=1,padx=9,pady=10)
facewashEntry.insert(0,0)

hairSpary=Label(cosmoticsFrame,text="Hair Spray",font=('poppins',12,'bold'),bg='black',fg='white')
hairSpary.grid(row=3,column=0,padx=20,pady=8,sticky='W')
hairSparyEntry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
hairSparyEntry.grid(row=3,column=1,padx=9,pady=10)
hairSparyEntry.insert(0,0)

hairGel=Label(cosmoticsFrame,text="Hair Gel",font=('poppins',12,'bold'),bg='black',fg='white')
hairGel.grid(row=4,column=0,padx=20,pady=8,sticky='W')
hairGelEntry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
hairGelEntry.grid(row=4,column=1,padx=9,pady=10)
hairGelEntry.insert(0,0)

bodylotion=Label(cosmoticsFrame,text="Body Lotion",font=('poppins',12,'bold'),bg='black',fg='white')
bodylotion.grid(row=5,column=0,padx=20,pady=8,sticky='W')
bodylotionentry=Entry(cosmoticsFrame,font=('poppins',12,'bold'),bd=7,width=10)
bodylotionentry.grid(row=5,column=1,padx=9,pady=10)
bodylotionentry.insert(0,0)

grocery=LabelFrame(productsFrame,text="Grocery",font=('poppins',15,'bold'),bg='black',fg='gold',bd=12,relief='groove')
grocery.grid(row=0,column=1)

rice=Label(grocery,text="Rice",font=('poppins',12,'bold'),bg='black',fg='white')
rice.grid(row=0,column=0,padx=20,pady=8,sticky='W')
riceEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
riceEntry.grid(row=0,column=1,padx=9,pady=10)
riceEntry.insert(0,0)

Daal=Label(grocery,text="Daal",font=('poppins',12,'bold'),bg='black',fg='white')
Daal.grid(row=1,column=0,padx=20,pady=8,sticky='W')
DaalEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
DaalEntry.grid(row=1,column=1,padx=9,pady=10)
DaalEntry.insert(0,0)

oil=Label(grocery,text="Oil",font=('poppins',12,'bold'),bg='black',fg='white')
oil.grid(row=2,column=0,padx=20,pady=8,sticky='W')
oilEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
oilEntry.grid(row=2,column=1,padx=9,pady=10)
oilEntry.insert(0,0)

wheat=Label(grocery,text="Wheat",font=('poppins',12,'bold'),bg='black',fg='white')
wheat.grid(row=3,column=0,padx=20,pady=8,sticky='W')
wheatEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
wheatEntry.grid(row=3,column=1,padx=9,pady=10)
wheatEntry.insert(0,0)

sugar=Label(grocery,text="Sugar",font=('poppins',12,'bold'),bg='black',fg='white')
sugar.grid(row=4,column=0,padx=20,pady=8,sticky='W')
sugarEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
sugarEntry.grid(row=4,column=1,padx=9,pady=10)
sugarEntry.insert(0,0)

teaPower=Label(grocery,text="Tea Power",font=('poppins',12,'bold'),bg='black',fg='white')
teaPower.grid(row=5,column=0,padx=20,pady=8,sticky='W')
teaPowerEntry=Entry(grocery,font=('poppins',12,'bold'),bd=7,width=10)
teaPowerEntry.grid(row=5,column=1,padx=9,pady=10)
teaPowerEntry.insert(0,0)

coldDrinks=LabelFrame(productsFrame,text="Soft Drinks",font=('poppins',15,'bold'),bg='black',fg='gold',bd=12,relief='groove')
coldDrinks.grid(row=0,column=2)

maaza=Label(coldDrinks,text="Maaza",font=('poppins',12,'bold'),bg='black',fg='white')
maaza.grid(row=0,column=0,padx=20,pady=8,sticky='W')
maazaEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
maazaEntry.grid(row=0,column=1,padx=9,pady=10)
maazaEntry.insert(0,0)

pepsi=Label(coldDrinks,text="Pepsi",font=('poppins',12,'bold'),bg='black',fg='white')
pepsi.grid(row=1,column=0,padx=20,pady=8,sticky='W')
pepsiEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
pepsiEntry.grid(row=1,column=1,padx=9,pady=10)
pepsiEntry.insert(0,0)

sprite=Label(coldDrinks,text="Sprite",font=('poppins',12,'bold'),bg='black',fg='white')
sprite.grid(row=2,column=0,padx=20,pady=8,sticky='W')
spriteEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
spriteEntry.grid(row=2,column=1,padx=9,pady=10)
spriteEntry.insert(0,0)

thumbsup=Label(coldDrinks,text="Thumbs Up",font=('poppins',12,'bold'),bg='black',fg='white')
thumbsup.grid(row=3,column=0,padx=20,pady=8,sticky='W')
thumbsupEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
thumbsupEntry.grid(row=3,column=1,padx=9,pady=10)
thumbsupEntry.insert(0,0)

cococola=Label(coldDrinks,text="Coco Cola",font=('poppins',12,'bold'),bg='black',fg='white')
cococola.grid(row=4,column=0,padx=20,pady=8,sticky='W')
cococolaEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
cococolaEntry.grid(row=4,column=1,padx=9,pady=10)
cococolaEntry.insert(0,0)

frooti=Label(coldDrinks,text="Frooti",font=('poppins',12,'bold'),bg='black',fg='white')
frooti.grid(row=5,column=0,padx=20,pady=8,sticky='W')
frootiEntry=Entry(coldDrinks,font=('poppins',12,'bold'),bd=7,width=10)
frootiEntry.grid(row=5,column=1,padx=9,pady=10)
frootiEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief='groove',pady=15)
billFrame.grid(row=0,column=3)


billareaLabel=Label(billFrame,text="Bill Area",font=('poppins',15,'bold'),bg='black',fg='gold',relief='groove')
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient='vertical')
scrollbar.pack(side='right',fill=Y)
text_widget_width =58
textarea=Text(billFrame,height=18,width=text_widget_width,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(windows,text="Bill Menu",font=('poppins',15,'bold'),bg='black',fg='gold',bd=12,relief='groove')
billmenuFrame.pack(fill=X,pady=15)

cosmetic=Label(billmenuFrame,text="Cosmetic price",font=('poppins',12,'bold'),bg='black',fg='white')
cosmetic.grid(row=0,column=0,padx=20,pady=8,sticky='W')
cosmeticEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
cosmeticEntry.grid(row=0,column=1,padx=9,pady=10)


groceryspice=Label(billmenuFrame,text="Grocery Price",font=('poppins',12,'bold'),bg='black',fg='white')
groceryspice.grid(row=1,column=0,padx=20,pady=8,sticky='W')
groceryspiceEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
groceryspiceEntry.grid(row=1,column=1,padx=9,pady=10)


drincksspice=Label(billmenuFrame,text="Cold Drinks Price",font=('poppins',12,'bold'),bg='black',fg='white')
drincksspice.grid(row=2,column=0,padx=20,pady=8,sticky='W')
drincksspiceEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
drincksspiceEntry.grid(row=2,column=1,padx=9,pady=10)


cosmeticTaxlabel=Label(billmenuFrame,text="Cosmetic Tax",font=('poppins',12,'bold'),bg='black',fg='white')
cosmeticTaxlabel.grid(row=0,column=2,padx=20,pady=8,sticky='W')
cosmeticTaxEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
cosmeticTaxEntry.grid(row=0,column=3,padx=9,pady=10)


groceryspiceTaxlabel=Label(billmenuFrame,text="Grocery Tax",font=('poppins',12,'bold'),bg='black',fg='white')
groceryspiceTaxlabel.grid(row=1,column=2,padx=20,pady=8,sticky='W')
groceryspiceTaxEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
groceryspiceTaxEntry.grid(row=1,column=3,padx=9,pady=10)


drincksspicetaxlabel=Label(billmenuFrame,text="Cold Drinks Tax",font=('poppins',12,'bold'),bg='black',fg='white')
drincksspicetaxlabel.grid(row=2,column=2,padx=20,pady=8,sticky='W')
drincksspicetaxEntry=Entry(billmenuFrame,font=('poppins',12,'bold'),bd=7,width=10)
drincksspicetaxEntry.grid(row=2,column=3,padx=9,pady=10)


buttonFrame=Frame(billmenuFrame,bd=8,relief='groove')
buttonFrame.grid(row=0,column=4,rowspan=3,padx=10,sticky='E')


totalButton=Button(buttonFrame,text='Total',font=('poppins',16,'bold'),bg='black',fg='white',bd=5,width=8,command=total)
totalButton.grid(row=0,column=0,padx=10,pady=10)


billButton=Button(buttonFrame,text='Bill',font=('poppins',16,'bold'),bg='black',fg='white',bd=5,width=8,command=billarea)
billButton.grid(row=0,column=1,padx=10,pady=10)

emailButton=Button(buttonFrame,text='Email',font=('poppins',16,'bold'),bg='black',fg='white',bd=5,width=8,command=send_email)
emailButton.grid(row=0,column=2,padx=10,pady=10)

printButton=Button(buttonFrame,text='Print',font=('poppins',16,'bold'),bg='black',fg='white',bd=5,width=8,command=print_bill)
printButton.grid(row=0,column=3,padx=10,pady=10)

clearButton=Button(buttonFrame,text='Clear',font=('poppins',16,'bold'),bg='black',fg='white',bd=5,width=8,command=clearbtn)
clearButton.grid(row=0,column=4,padx=10,pady=10)







windows.mainloop()