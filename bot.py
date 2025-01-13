import Math_respone as mr
import biology_response as br
import general_response as gr
import chemistry_response as cr
import astronomy_response as ar
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import re
import random
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


stop_words=set(stopwords.words('english'))
ps=PorterStemmer()




window = tk.Tk()
window.title('Bernard')
window.state('zoomed')
window.config(bg='alice blue')
window.iconbitmap('pics\\icon2.ico')
window.resizable(false,false )
menu_file = tk.Menu(window)
window.config(menu=menu_file)
file_menu = tk.Menu(menu_file)
menu_file.add_cascade(label='Menu', menu=file_menu)
file_menu.add_command(label='Help')
file_menu.add_command(label='Exit', command=window.quit)

buttonFrame = tk.Frame(window, bg='alice blue', highlightbackground='grey', highlightthickness=1)
buttonFrame.pack(side=tk.LEFT)
buttonFrame.pack_propagate(False)
buttonFrame.configure(width=300, height=2160)



pic=Image.open('pics\\science-chatbot-low-resolution-logo-color-on-transparent-background.png')
resized = pic.resize((250, 150))
logo = ImageTk.PhotoImage(resized)
logo_label = tk.Label(window, image=logo)
logo_label.pack(pady=10)

List = tk.Frame(window, bg='alice blue')
List.pack(anchor='nw')
List.configure(height=400, width=900)

label1 = tk.Label(List, text='know biology terms', bg='alice blue', font=('high tower text', 20))
img1 = Image.open('pics/leaf.png')
resImg1 = img1.resize((50, 50))
lbimg1 = ImageTk.PhotoImage(resImg1)
lbg1 = tk.Label(List, image=lbimg1)
lbg1.grid(column=0, row=0, pady=25, padx=10)
label1.grid(column=1, row=0, pady=25, sticky='w')

label2 = tk.Label(List, text='solve math problems', bg='alice blue', font=('high tower text', 20))
img2 = Image.open('pics/mm.png')
resImg2 = img2.resize((50, 50))
lbimg2 = ImageTk.PhotoImage(resImg2)
lbg2 = tk.Label(List, image=lbimg2)
lbg2.grid(column=0, row=1, pady=25, padx=10)
label2.grid(column=1, row=1, pady=25, sticky='w')

label3=tk.Label(List,text="Identify elements' properties",bg='alice blue', font=('high tower text',20))
img3=Image.open('pics/c.png')
resImg3=img3.resize((50,50))
lbimg3=ImageTk.PhotoImage(resImg3)
lbg3=tk.Label(List,image=lbimg3)
lbg3.grid(column=0,row=2,pady=25,padx=10)
label3.grid(column=1,row=2,pady=25,sticky='w')


label4=tk.Label(List,text="Imporve your physics knowledge",bg='alice blue', font=('high tower text',20))
img4=Image.open('pics/p.png')
resImg4=img4.resize((60,40))
lbimg4=ImageTk.PhotoImage(resImg4)
lbg4=tk.Label(List,image=lbimg4)
lbg4.grid(column=0,row=3,pady=25,padx=10)
label4.grid(column=1,row=3,pady=25,sticky='w')


label5=tk.Label(List,text="Discover beyond the earth",bg='alice blue', font=('high tower text',20))
img5=Image.open('pics/a.png')
resImg5=img5.resize((50,50))
lbimg5=ImageTk.PhotoImage(resImg5)
lbg5=tk.Label(List,image=lbimg5)
lbg5.grid(column=0,row=4,pady=25,padx=10)
label5.grid(column=1,row=4,pady=25,sticky='w')

def math():


    mathWindow=tk.Tk()
    mathWindow.title('Math chat bot')
    mathWindow.state('zoomed')
    mathWindow.resizable(false,false)
    mathWindow.config(bg='alice blue')

    mathHome = tk.Frame(mathWindow, height=100, highlightbackground='grey', highlightthickness=1)
    mathHome.pack(anchor='w')

    backBtn = tk.Button(mathHome, text='back', font=('magneto', 16, 'bold'), width=10, fg='white', bg='#1fb0ff', command=mathWindow.destroy)
    backBtn.grid(row=0, column=0, padx=10)

    head = tk.Label(mathHome, text='Mathematics', font=('arial', 23, 'bold'))
    head.grid(row=0, column=1, padx=480, pady=10, ipadx=60)

    mathFrame = tk.Frame(mathWindow, width=850, height=200, bg='grey')
    mathFrame.pack(side=tk.BOTTOM)

    math_text = tk.Text(mathFrame, height=4, width=160, font=('arial', 14))
    math_text.pack(pady=5, padx=5)

    scroll_frame=tk.Frame(mathWindow,bg='alice blue')
    scroll_frame.pack(fill='both',expand=1)

    scroll_canvas=tk.Canvas(scroll_frame,bg='alice blue')
    scroll_canvas.pack(side=tk.LEFT,fill='both',expand=1)

    scroll_bar=ttk.Scrollbar(scroll_frame,orient='vertical',command=scroll_canvas.yview)
    scroll_bar.pack(side='right',fill='y')

    scroll_canvas.configure(yscrollcommand=scroll_bar.set)

    boundary_frame=tk.Frame(scroll_canvas,bg='alice blue')
    boundary_frame.bind('<Configure>', lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all')))

    scroll_canvas.create_window((0,0),window=boundary_frame,anchor='nw')

    def send_to_math_label():
            numerical=0
            terminology=0
            quadratic_pattern = r'([+-]?\d*)x\^2\s*([+-]?\d*)x\s*([+-]?\d*)'
            absolute_pattern = '[|]\S+[|]'
            all_arthimetics = ['+', '-', '*', '/']

            question = math_text.get('1.0',tk.END).lower()
            question0 = question.replace(' ','')
            question0 = question0.replace('\n', '')
            real_question=word_tokenize(question)
            filtered=[]


            def calculate():
                arthimetic = False
                for i in sign:

                        if i in all_arthimetics:
                            arthimetic=True

                        else:
                            arthimetic=False
                            break

                if arthimetic==True:
                    response=mr.all_arthimetic(question0)

                else:

                    if re.fullmatch(absolute_pattern,question0):
                        response=mr.absoluteValue(question0)


                    elif re.fullmatch(quadratic_pattern,question0):
                        response=mr.quad(question0)
                    else:
                        response = 'I have no info about this problem'
                return response

            for i in real_question:
                if i not in stop_words:
                    i=ps.stem(i)
                    filtered.append(i)
            sign=re.findall('\D',question0)
            if real_question == []:
                color = 'red'
                response = gr.empty_sentences[random.randrange(len(gr.empty_sentences))]
                
            elif len(real_question)==1:
                if re.fullmatch('\w+',question0):
                    response = mr.mathChat(question,True)
                    color = 'black'
                else:
                    response = calculate()
                    color='black'
            else:
                for i in filtered:
                    if i in gr.gh:
                        terminology+=1
                    elif i in gr.gr:
                        numerical+=1
                        
                if terminology > numerical:
                            
                    response = mr.mathChat(question,False)
                    color='black'
                else:
                    question=question.replace('\n','')
                    question1=question.split(' ')
                    for i in question1:
                        if re.fullmatch('[[A-Z]*[a-z]*[A-Z]*]',i):
                            pass
                        else:
                            question0=i
                    response = calculate()
                    color='black'
                    
            label_user = tk.Label(boundary_frame, text='User: ' + question, bg='alice blue', font=('arial', 15))
            label_user.pack(anchor='nw')
            label = tk.Label(boundary_frame, text='BOT: ' + str(response), bg='alice blue', font=('arial', 15), fg=color)
            label.pack(anchor='w')

    send_btn = tk.Button(mathFrame, text='submit', font=('magneto', 16), bg='#1fb0ff',fg='white', command=send_to_math_label)
    send_btn.pack(anchor='center')
    mathWindow.mainloop()


def biology():
    bioWindow = tk.Tk()
    bioWindow.title('Biology chat bot')
    bioWindow.state('zoomed')
    bioWindow.resizable(false, false)
    bioWindow.config(bg='alice blue')

    bioHome=tk.Frame(bioWindow,height=100,highlightbackground='grey',highlightthickness=1)
    bioHome.pack(anchor='w')

    backBtn=tk.Button(bioHome,text='back',font=('magneto',16,'bold'),width=10,fg='white',bg='#1fb0ff',command=bioWindow.destroy)
    backBtn.grid(row=0,column=0,padx=10)

    head=tk.Label(bioHome,text='Biology',font=('arial',23,'bold'))
    head.grid(row=0,column=1,padx=480,pady=10,ipadx=60)

    bioFrame=tk.Frame(bioWindow,width=350,height=200,bg='grey')
    bioFrame.pack(side=tk.BOTTOM)

    bio_text = tk.Text(bioFrame, height=4, width=150,font=('arial',13))
    bio_text.pack(pady=5,padx=5)

    scroll_frame = tk.Frame(bioWindow, bg='alice blue')
    scroll_frame.pack(fill='both', expand=1)

    scroll_canvas = tk.Canvas(scroll_frame, bg='alice blue')
    scroll_canvas.pack(side=tk.LEFT, fill='both', expand=1)

    scroll_bar = ttk.Scrollbar(scroll_frame, orient='vertical', command=scroll_canvas.yview)
    scroll_bar.pack(side='right', fill='y')

    scroll_canvas.configure(yscrollcommand=scroll_bar.set)

    boundary_frame = tk.Frame(scroll_canvas, bg='alice blue')
    boundary_frame.bind('<Configure>', lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all')))

    scroll_canvas.create_window((0, 0), window=boundary_frame, anchor='nw')

    def send_to_bio_label():

        color=''
        question = bio_text.get('1.0', tk.END)
        question=question.replace('\n','')
        question_label = tk.Label(boundary_frame, text='User:  ' + question, bg='alice blue', font=('arial',13),wraplength=1400)
        question_label.pack(anchor='w', padx=15)

        if question=='':
            output=gr.empty_sentences[random.randrange(len(gr.empty_sentences))]
            color='red'

        else:
            answer = br.bioChat(question)
            output='BOT:  '+answer
            color='black'

        answer_label=tk.Label(boundary_frame,text=output,bg='alice blue',font=('arial',13),fg=color,wraplength=1400)
        answer_label.pack(anchor='w',padx=15)

    send_btn = tk.Button(bioFrame, text='submit', font=('magneto', 16), bg='#1fb0ff',fg='white', command=send_to_bio_label)
    send_btn.pack(anchor='center')

    bioWindow.mainloop()



def chemistry():

    chemWindow = tk.Tk()
    chemWindow.title('Biology chat bot')
    chemWindow.geometry('500x500')
    chemWindow.config(bg='alice blue')
    chemWindow.state('zoomed')
    chemWindow.resizable(false,false)

    chemHome = tk.Frame(chemWindow, height=100, highlightbackground='grey', highlightthickness=1)
    chemHome.pack(anchor='w')

    backBtn = tk.Button(chemHome, text='back', font=('magneto', 16, 'bold'), width=10, fg='white', bg='#1fb0ff',
                        command=bioWindow.destroy)
    backBtn.grid(row=0, column=0, padx=10)

    head = tk.Label(chemHome, text='Biology', font=('arial', 23, 'bold'))
    head.grid(row=0, column=1, padx=480, pady=10, ipadx=60)

    scroll_frame = tk.Frame(chemWindow, bg='alice blue')
    scroll_frame.pack(fill='both', expand=1)

    scroll_canvas = tk.Canvas(scroll_frame, bg='alice blue')
    scroll_canvas.pack(side=tk.LEFT, fill='both', expand=1)

    scroll_bar = ttk.Scrollbar(scroll_frame, orient='vertical', command=scroll_canvas.yview)
    scroll_bar.pack(side='right', fill='y')

    scroll_canvas.configure(yscrollcommand=scroll_bar.set)

    boundary_frame = tk.Frame(scroll_canvas, bg='alice blue')
    boundary_frame.bind('<Configure>', lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all')))

    scroll_canvas.create_window((0, 0), window=boundary_frame, anchor='nw')

    chemFrame = tk.Frame(chemWindow, width=950, height=200, bg='grey')
    chemFrame.pack(side=tk.BOTTOM)

    chem_text = tk.Text(chemFrame, width=200,height=6)
    chem_text.pack(padx=20, pady=15)

    def send_to_chem_label():
        question = chem_text.get('1.0', tk.END)
        question = question.replace(' ', '')
        question = question.replace('\n', '')

        answer = cr.elements(question)

        label=tk.Label(boundary_frame,text=answer)
        label.pack()

    send_btn = tk.Button(chemFrame, text='solve', font=('arial', 16), bg='grey', command=send_to_chem_label)
    send_btn.pack()

    chemWindow.mainloop()


def phy():
    pass


def astronomy():
    astroWindow = tk.Tk()
    astroWindow.title('Astronomy chat bot')
    astroWindow.state('zoomed')
    astroWindow.resizable(false,false)
    astroWindow.config(bg='alice blue')

    astro_text = tk.Text(astroWindow, height=6)
    astro_text.pack(padx=20, pady=15)

    def send_to_astro_label():
        question = astro_text.get('1.0', tk.END)
        question = question.replace(' ', '')
        question = question.replace('\n', '')
        question = question.replace('-','')
        question=question.lower()
        answer = ar.astro(question)
        label=tk.Label(astroWindow,text=answer,bg='alice blue')
        label.pack()

    send_btn = tk.Button(astroWindow, text='solve', font=('arial', 16), bg='grey', command=send_to_astro_label)
    send_btn.pack()


    astroWindow.mainloop()

# ....creating button on a different frame............


emptyl=tk.Label(buttonFrame,bg='alice blue',height=4,text='Science chatbot',font=('high tower text',24))
emptyl.pack()

bioBtn=tk.Button(buttonFrame,text='Biology',fg='#fff',bg='#1fb0ff', font=('magneto',15),width=18,height=2,command=biology)
bioBtn.pack(pady=20)

mathBtn=tk.Button(buttonFrame,text='Math',fg='#fff',bg='#1fb0ff', font=('magneto',15),height=2,width=18,command=math)
mathBtn.pack(pady=20)

chemBtn=tk.Button(buttonFrame,text='Chemistry', fg='#fff',bg='#1fb0ff', font=('magneto',15), width=18, height=2, command=chemistry)
chemBtn.pack(pady=20)

phyBtn=tk.Button(buttonFrame,text='Physics',fg='#fff',bg='#1fb0ff', font=('magneto',15),height=2,width=18)
phyBtn.pack(pady=20)


astroBtn=tk.Button(buttonFrame,text='Astronomy',fg='#fff',bg='#1fb0ff',font=('magneto',15),width=18,height=2,command=astronomy)
astroBtn.pack(pady=20)

window.mainloop()



