import tkinter
from tkinter import *
import random

 
questions = [
   "Who developed Python Programming Language?",
   "To add a new element to a list we use which Python command?",
   "Which of the following is used to define a block of code in Python language?",
   "Which of the following expressions is an example of type conversion?",
   "What is the order of precedence in python?",
   "Which of the following functions is a built-in function in python?",
   '''What will be the output of the "hello"+1+2+3?''',
   "What will be displayed by print(ord(‘b’) – ord(‘a’))?",
   "What arithmetic operators cannot be used with strings in Python?",
   "What is the maximum possible length of an identifier in Python?",
]
# Choice of answers provided to the student \\\

answers_choice= [
    ["Wick van Rossum","Rasmus Lerdorf"," Guido van Rossum","Niene Stom"],
    ["list1.addEnd(5)","list1.addLast(5)","list1.append(5)","list1.add(5)  "],
    ["Indentation","   Key   "," Brackets ","All of the mentioned"],
    ["4.0 + float(3)","5.3 + 6.3","5.0 + 3","3 + 7"],
    ["Exponential, Parentheses, Multiplication, Division, Addition, Subtraction","Exponential, Parentheses, Division, Multiplication, Addition, Subtraction","Parentheses, Exponential, Multiplication, Division, Subtraction, Addition","Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
    ["factorial()","print()","seed()","sqrt()"],
    ["hello123","hello","Error","hello6"],
    ["0","1","-1","2"],#ans 1 optn 98-97
    ["  *  ","  -  ","  +  ","All of the mentioned"],
    ["79 characters","31 characters","63 characters","None of the above"],
]
# Correct answer list \\\

answers=[2,2,0,0,3,1,2,1,1,3]

# Answers given by the students \\\

user_answer=[]

# Score shown at the end screen \\\
 
def seescore(score):
    labelRESULT= Label(
        root,
        font=("consolas",20),
        text=" Your Score is " + str(score) +" ",
        background="#FF8000"
    )
    labelRESULT.pack(pady=(10,10))

# The 5 questons that are mentioned in the app \\\

indexes= []

# Generating 6 random numbers to be selected as questions out of total questions \\\

def gen():
    global indexes#to make chngs is global indexes
    while(len(indexes) <6):
        x= random.randint(0,9)
        if x in indexes:
            continue#to prevent duplicate ele
        else:
            indexes.append(x)

# seeing the result \\\

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#EEC900",
        border = 0,
    )
    labelimage.pack(pady=(30,30))

    labelresulttext = Label(
         root,
         font =("consolas",25),
         background="#EEDC82",
    )
    labelresulttext.pack()
     
    if score >= 25:
        img = PhotoImage(file="GREAT.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text=" Excellent Work !! ")
        seescore(score)
    elif (score >= 10  and score < 25):
        img = PhotoImage(file="OK.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text= " You can do Better ! ")
        seescore(score)
    else:
        img = PhotoImage(file="BAD.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text=" You need to try Hard ! ")
        seescore(score)

# function to calculate the marks of correct answers given by the student \\\

def  calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:#indexes having list of random ques
        if user_answer[x] == answers[i]:
           score = score+5
        x +=1
    print(score)
    
    showresult(score)


ques=1#declaring ques with 1 bec 0th ques is done
# Registering the answers given byj the student \\\
    
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques 
    x= radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 6:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques+=1 #to change ques 
    else:
        print(indexes)
        print(user_answer)
        print(answers)
        calc()

# Creating question and option screen for the student \\\

def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion= Label(
        root,
        text=questions[indexes[0]],#in starting 0 index ques will be 1st ques then selected func will chng ques 
        font=("consolas",16,"bold"),
        width= 500,
        justify= "center",
        wraplength= 400,
        background = "#5CACEE",
    )
    lblQuestion.pack(pady=(100,30))
    global radiovar#making this variable accessable outside this function
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times",15),
        value=0,#this value we are saving in  radiovar 
        variable= radiovar,
        command= selected, 
        background = "#FF8000",
    )
    r1.pack(pady = 5)

    r2=Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times",15),
        value=1,
        variable= radiovar,
        command= selected, 
        background = "#FF8000",
    )
    r2.pack(pady = 5)

    r3=Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times",15),
        value=2,
        variable= radiovar,
        command= selected,
        background = "#FF8000", 
    )
    r3.pack(pady = 5)

    r4=Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times",15),
        value=3,
        variable= radiovar,
        command= selected,
        background = "#FF8000", 
    )
    r4.pack(pady = 5)

# Screen to be displayed after pressing the start button \\\

def startispressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


# Creating the start screen of the APP \\\

root= tkinter.Tk()
root.title("Python Quiz")
root.geometry("700x600")
root.config(background="#EEDC82")
root.resizable(0,0)


img1=PhotoImage(file="Logo_p-bg.png")
labelimage =Label(
    root,
    image=img1,
    background="#EEDC82",
    border = 0,
)
labelimage.pack(pady=(30,0))

labeltext= Label(
    root,   
    text=" Python Quiz ",
    font = ("comic sans MS",24,"bold"),
    background = "#5CACEE",
    border = 0,
)
labeltext.pack(pady=(10,0))

img2=PhotoImage(file="START-bg.png")#we have to use this to use img
btnStart= Button(
    root,
    image=img2,
    background="#EEDC82",
    relief= FLAT,
    border=0,
    command= startispressed,
)
btnStart.pack()
lblInstruction= Label(
    root,
    text="Read The Rules and\nClick Start Once You are Ready",
    background="#EEDC82",
    font=("Consolas",13),
    justify="center",
)
lblInstruction.pack(pady=(10,10))
lblRules=Label(
    root,
    text="This quiz contains 6 question\n Each question contains 5 marks\n Once selected the answer cannot be changed so, answer carefully",
    width=100,
    font=("Times",14),
    background="#FF8000",
    foreground="#000000",
)
lblRules.pack()
root.mainloop()

# --------- END ------------  \\\