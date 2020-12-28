import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tabulate import tabulate

global score
score = 0
global ques_answered 
ques_answered = []
global roll_no
timeron=1
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='EXAM_PORTAL',
                                         user='root',
                                         password='darshmysql31')  
     
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        data_base = cursor.fetchone()

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

root = tk.Tk()
root.title("VJTI ESE 2020")     
root.geometry("1200x700")
root.resizable(0,0)

global vjti_logo 
vjti_logo = Image.open('./assets/veermata-jijabai-technological-institute-mumbai-logo.png')
vjti_logo = vjti_logo.resize((200, 300), Image.ANTIALIAS)
vjti_logo = ImageTk.PhotoImage(vjti_logo)
global logo 
logo = Label(root,image = vjti_logo)
logo.pack(pady= 15)

login_ins = Label(root,text = "Please Enter Details for Authentication\nNOTE : Input is NOT Case Sensitive",font =("Georgia",20,"bold"))

global login_logo
login_logo_img = Image.open('./assets/veermata-jijabai-technological-institute-mumbai-logo.png')
login_logo_img = login_logo_img.resize((450, 550), Image.ANTIALIAS)
login_logo_img = ImageTk.PhotoImage(login_logo_img)
login_logo = Label(root,image = login_logo_img)

next_img = Image.open('./assets/next_button.png')
next_img = next_img.resize((240, 70), Image.ANTIALIAS)
next_img = ImageTk.PhotoImage(next_img)

ques = [
    "Which of the following is Immutable?",
    "Which of the following functions takes a Console Input in Python ?",
    "How will you open a file for reading as a Text file ?",
    "Which of The following is must to Execute a Python code ?",
    "Polymorphism is when a subclass can modify the behavior of its superclass.",
    "The append Method adds value to the list at the  ?",
    "Which of the following data types is not supported in Python ?",
    "Which of the following is executed in browser (client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in Python we use the keyword ?",
    "If s='abcbuzz' what is the output for s[:2] ?",
    "Maximum possible length of an identifier ?",
    "Output for 19%2 in Python Programming ?",
    "Which of the following piece of code is used to sort an array in descending order ?",
    "Which module is required to use DataFrames ?",
    "How to delete values in dictionary using key k ?",
    "Which piece of code is right for making a class attribute ?",
    "Which of the following commands will create a list ?",
    "What will be the output of the following Python code snippet ? d = {'john':40, 'peter':45}",
    "Suppose d = {“john”:40, “peter”:45}. To obtain the number of entries in dictionary which command do we use ?"   
]

options = [
    ["Lists","Tuples","Both","None",],
    ["get()","input()","gets()","scan()",],
    ["open('file.txt')","open('file.txt','w')","open('file.txt','r')","open('file.txt','a')",],
    ["TURBO C","Py Interpreter","Notepad","IDE",],
    ["True","False","Depends on content","Invalid",],
    ["custom location","end","center","beginning",],
    ["Strings","Numbers","Slice ","Lists",],
    ["PERL","CSS","PYTHON","JAVA",],
    ["function","void","fun","def",],
    ["all","var","let","global",],
    ["ab","buzz","abcbuzz","z",],
    ["31","45","87","63",],
    ["1","12","2","3",],
    ["arr.sort()","arr.sort(reverse=True)","arr.sort(reverse=False)","None",],
    ["pandas","math","tkinter","csv",],
    ["del dict[k]","del k","del dict","dict.pop(dict[k])",],
    ["def __init__(self):pass","def func():pass","def __init__():pass","None",],
    ["list1 = list()","list1 = []","list1 = list([1, 2, 3])","ALL",],
    ["'john and peter'","'40 and 45'","'john,peter,40,45'","None",],
    ["d.size()","len(d)","size(d)","d.len()",]
]

answers = [1,1,2,1,0,1,2,1,3,3,0,0,0,1,0,0,0,3,0,1] 

ques_asked = list()
def gen():
    global ques_asked
    while(len(ques_asked) < 10):
        x = random.randint(0,19)
        if x in ques_asked:
            continue
        else:
            ques_asked.append(x)


def resultPage():
    global ques_txt,r1,r2,r3,r4,next_ques_btn,score,roll_no
    ques_txt.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    next_ques_btn.destroy()
    txt = Label(root,text = f"Your final test score is {score*2}! ",font=("Lucida Sans Typewriter",30,"bold"),background = '#ffffff')
    txt.pack(pady = (60,20))
    root.config(background = '#ffffff')
    result_image = Label(root,bd=0)
    result_image.pack(pady = (50,0))
    result_text = Label(root , font = ('Bahnschrift',35,"italic"),background = '#ffffff')
    result_text.pack(pady = (30,50))
    if score >= 8:
        result_img = Image.open('./assets/happy.png')
        result_img = result_img.resize((300, 300), Image.ANTIALIAS)
        result_img = ImageTk.PhotoImage(result_img)
        result_image.configure(image = result_img)
        result_image.image = result_img
        result_text.configure(text = 'You are Excellent!!!')
        result_text.configure(fg = 'green')
    elif (score >= 5 and score < 8):
        result_img = Image.open('./assets/ok.png')
        result_img = result_img.resize((300, 300), Image.ANTIALIAS)
        result_img = ImageTk.PhotoImage(result_img)
        result_image.configure(image = result_img)
        result_image.image = result_img
        result_text.configure(text = 'You can be Better!!')
        result_text.configure(fg = 'gold')
    else:
        result_img = Image.open('./assets/poor.png')
        result_img = ImageTk.PhotoImage(result_img)
        result_image.configure(image = result_img)
        result_image.image = result_img
        result_text.configure(text = 'You need to work Harder!')
        result_text.configure(fg = 'red')

    sql = "UPDATE Scores SET Score = %s where RollNo = %s "
    cursor = connection.cursor()
    cursor.execute(sql,(score*2 , int(roll_no)))
    connection.commit()
    

    sql = "SELECT * from StudentInfo"
    cursor = connection.cursor()
    cursor.execute(sql)
    stud_info = cursor.fetchall()
    print(tabulate(stud_info,['Roll No.','Name','Branch'],tablefmt = 'psql'))

    sql = "SELECT * from Scores"
    cursor = connection.cursor()
    cursor.execute(sql)
    scores_table = cursor.fetchall()
    print(tabulate(scores_table,['Roll No.','Score'],tablefmt = 'psql'))
           
def updateScore(index,ans):
    global score
    if answers[index] == ans:
        score+=1

def next_ques():
    ans = radiovar.get()
    global ques_txt,r1,r2,r3,r4,next_ques_btn
    updateScore(ques_answered.pop(),ans)
    if len(ques_asked) != 0 :
        index = ques_asked.pop(0)
        ques_answered.append(index)
        ques_txt.config(text = ques[index])
        r1['text'] = options[index][0]
        r2['text'] = options[index][1]
        r3['text'] = options[index][2]
        r4['text'] = options[index][3]
    else:
        timeron=0
        resultPage()
        
next_ques_btn = Button(root,image = next_img,relief = FLAT,border = 0,width = 240,height = 70,cursor = 'hand2',command = next_ques)
timer = Label(root,text="",font=("Georgia",20))
timer.pack(padx=(1000,0))
def set_idle_timer(t):
    hours, remainder = divmod(t, 3600)
    mins, secs = divmod(remainder, 60)
    timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
    timer.config(text=timeformat)
    t -=1
    if t==-1:
        timer.destroy()
        if timeron==1:
            resultPage()
        else:
            timer.destroy()
    else:
        root.after(1000,lambda: set_idle_timer(t))

def test():
    ins_head.destroy()
    ins_txt.destroy()
    ins_txt1.destroy()
    insPgPcdBtn.destroy()
    global ques_txt,r1,r2,r3,r4,next_ques_btn
    root.config(background="#c0e5f0")
    set_idle_timer(600)
    global first_index
    first_index = ques_asked.pop(0)
    ques_answered.append(first_index)
    ques_txt = Label(root,bg="black",fg="white",text = ques[first_index],font = ("Bookman Old Style", 30),width = 1000,justify = "center",wraplength = 800,)
    ques_txt.pack(pady=(50,30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        activebackground="gray",
        activeforeground="white",
        text = options[first_index][0],
        font = ("Bahnschrift", 20 , "bold"),
        value = 0,
        variable = radiovar,
        justify = "left",
    )
    r1.place(x = 280 , y = 230)

    r2 = Radiobutton(
        root,
        activebackground="gray",
        activeforeground="white",
        text = options[first_index][1],
        font = ("Bahnschrift", 20 , "bold"),
        value = 1,
        variable = radiovar,
        justify = "left",

    )
    r2.place(x = 280 , y = 305)

    r3 = Radiobutton(
        root,
        activebackground="gray",
        activeforeground="white",
        text = options[first_index][2],
        font = ("Bahnschrift", 20 , "bold"),
        value = 2,
        variable = radiovar,
        justify = "left",
    )
    r3.place(x = 280 , y = 380)

    r4 = Radiobutton(
        root,
        activebackground="gray",
        activeforeground="white",
        text = options[first_index][3],
        font = ("Bahnschrift", 20 , "bold"),
        value = 3,
        variable = radiovar,
        justify = "left",
    )
    r4.place(x = 280, y = 455)
    next_ques_btn.place(x = 860,y = 620)
 
def displayIns():
    ins_head.pack(pady = 2.5)
    ins_txt.pack(pady=(0,0))
    ins_txt1.pack(pady = (20,0) )
    insPgPcdBtn.pack(pady= (10,0))

def checkDetails(studBranch): 
    global roll_no
    name = name_entry.get().lower()
    rollNo = RollNo_entry.get()
    roll_no = rollNo
    branch = studBranch
    try : 
        sql = "SELECT * from StudentInfo where RollNo = %s AND Name = %s AND Branch = %s "
        cursor = connection.cursor()
        cursor.execute(sql,(int(rollNo),name,branch))
        stud = cursor.fetchone()
        if stud :
            name_label.destroy()
            name_entry.destroy()
            RollNo_label.destroy()
            RollNo_entry.destroy()
            Branch_label.destroy()
            Branch_entry.destroy()
            sub_btn.destroy()
            login_logo.destroy()
            login_ins.destroy()
            incorrect_det.destroy()
            displayIns()
            gen()
        else :
            incorrect_det.pack()       
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

def login():
    logo.destroy()
    front_title.destroy()
    front_txt.destroy()
    btnStart.destroy()
    name_label.place(x = 600 ,y = 200) 
    name_entry.place(x=750,y=200) 
    RollNo_label.place(x = 600,y=280) 
    RollNo_entry.place(x=750,y=280)
    Branch_label.place(x=600,y = 360) 
    Branch_entry.place(x=770,y= 370)
    sub_btn.place(x=760,y=500)
    login_logo.place(x = 40,y=50)
    login_ins.place(x = 550 , y = 70)
    
front_title = Label(root,text= "VEERMATA JIJABAI TECHNOLOGICAL INSTITUTE",font=("Georgia",30,"bold"))
front_title.pack(pady = 20)
front_txt = Label(root,text = "End Semester Examination 2020-2021",font=("Georgia",30))
front_txt.pack()
img = Image.open('./assets/Proceed.png')
img = img.resize((100, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

btnStart = Button(root,image = img,relief = FLAT,border = 0,width = 100,height = 100,cursor="hand2",command = login)
btnStart.pack(pady = (70,0),padx = (900,0))

start_test_img  = Image.open('./assets/starttest-button.png')
start_test_img  = start_test_img .resize((250, 80), Image.ANTIALIAS)
start_test_img  = ImageTk.PhotoImage(start_test_img )


ins_head = Label(root,text = "Read the following instructions carefully before you proceed!\n",font=("Bookman Old Style",25,"bold"))
ins_txt = Label(root,text = "1. This test will contain 10 Questions of 2 Marks each.\n\n2. There is no negative marking.So attempting all Questions is compulsory!\n\n3. 10 minutes will be given for Submission.\n\n4. If you fail to finish the test within the time limit, you will logged out automatically and responses marked uptil that point will be evaluated.\n\n5. EVERY STUDENT WILL RECEIVE A DIFFERENT QUESTION SET. HENCE DO NOT ENGAGE IN ANY MALPRACTICE.",font = ("Bahnschrift",20),justify = LEFT,wraplength=1000)
ins_txt1=Label(root,text="ALL THE BEST!!...",fg="DodgerBlue4",font = ("Felix Titling",30,"italic"))
insPgPcdBtn = Button(root,image = start_test_img ,relief = FLAT,border = 0,width = 250,height = 80,cursor = 'hand2',command = test)

rollNo = 0
name_input = ""
branch = StringVar(root)
name_label = tk.Label(root, text = 'Name :', font=('Bahnschrift', 25, 'bold')) 
name_entry = tk.Entry(root,textvariable = name_input,font=('Georgia',20 ,'normal')) 
RollNo_label = tk.Label(root, text = 'RollNo :', font = ('Bahnschrift',25,'bold'))  
RollNo_entry = tk.Entry(root, textvariable = rollNo, font = ('Georgia',20,'normal')) 
Branch_label = tk.Label(root, text = 'Branch :', font = ('Bahnschrift',25,'bold'))  
Branch_entry = OptionMenu(root, branch,"CS","IT","EXTC","ELECTRONICS","MECHANICAL","CIVIL","PRODUCTION","TEXTILE")
Branch_entry['width'] = 15
Branch_entry.configure(cursor = 'hand2', font=('Georgia', 15, 'bold'))
branch.set("CS")

sub_img = Image.open('./assets/SUBMIT-BUTTON.png')
sub_img = sub_img.resize((250, 80), Image.ANTIALIAS)
sub_img = ImageTk.PhotoImage(sub_img)
sub_btn=tk.Button(root,image = sub_img,relief = FLAT,border = 0,width = 250,height = 80,cursor = 'hand2' ,command =lambda: checkDetails(branch.get())) 

incorrect_det = Label(root,text = "Incorrect Details !",font=("Georgia",20),fg = "red") 
root.mainloop()