from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        #create db object
        self.dbo = Database()
        self.apio = API()

        # Initialize main window
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.geometry("400x650")
        self.root.configure(bg="#f0f0f0")

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        label1 = Label(frame, text='Enter Email', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label1.pack(pady=(10, 5))
        
        self.email_input = Entry(frame, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(frame, text='Enter Password', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label2.pack(pady=(10, 5))
        
        self.password_input = Entry(frame, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(frame, text='Login', width=30, height=2, bg="#4caf50", fg="white", command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(frame, text='Not a member?', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label3.pack(pady=(20, 10))

        redirect_btn = Button(frame, text='Register Now', bg="#2196f3", fg="white", command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        label0 = Label(frame, text='Enter Name', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label0.pack(pady=(10, 5))
        
        self.name_input = Entry(frame, width=40)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(frame, text='Enter Email', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label1.pack(pady=(10, 5))
        
        self.email_input = Entry(frame, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(frame, text='Enter Password', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label2.pack(pady=(10, 5))
        
        self.password_input = Entry(frame, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        registration_btn = Button(frame, text='Register', width=30, height=2, bg="#4caf50", fg="white", command=self.perform_registration)
        registration_btn.pack(pady=(10, 10))

        label3 = Label(frame, text='Already a member?', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label3.pack(pady=(20, 10))

        redirect_btn = Button(frame, text='Login Now', bg="#2196f3", fg="white", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now.')
        else:
            messagebox.showerror('Error', 'Email already exists.')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful.')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect Email/Password.')

    def home_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        sentiment_btn = Button(frame, text='Sentiment Analysis', width=30, height=2, bg="#4caf50", fg="white", command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(frame, text='Name Entity Recognition', width=30, height=2, bg="#4caf50", fg="white", command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(frame, text='Emotion Prediction', width=30, height=2, bg="#4caf50", fg="white", command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(frame, text='Logout', width=30, height=2, bg="#f44336", fg="white", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        heading2 = Label(frame, text="Sentiment Analysis", bg='#f0f0f0', fg='#333', font=('verdana', 20))
        heading2.pack(pady=(10, 10))

        label1 = Label(frame, text='Enter the text', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label1.pack(pady=(10, 5))
        
        self.sentiment_input = Entry(frame, width=40)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(frame, text='Analyze Sentiment', width=30, height=2, bg="#4caf50", fg="white", command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(frame, text='', bg='#f0f0f0', fg='#333', font=('verdana', 16))
        self.sentiment_result.pack(pady=(10, 10))

        goback_btn = Button(frame, text='Go Back', width=30, height=2, bg="#2196f3", fg="white", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for sentiment, score in result['sentiment'].items():
            txt += f'{sentiment} -> {score}\n'

        self.sentiment_result['text'] = txt

    def ner_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        heading2 = Label(frame, text="Name Entity Recognition", bg='#f0f0f0', fg='#333', font=('verdana', 20))
        heading2.pack(pady=(10, 10))

        label1 = Label(frame, text='Enter the text', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label1.pack(pady=(10, 5))
        
        self.ner_input = Entry(frame, width=40)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(frame, text='Analyze Text', width=30, height=2, bg="#4caf50", fg="white", command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(frame, text='', bg='#f0f0f0', fg='#333', font=('verdana', 16))
        self.ner_result.pack(pady=(10, 10))

        goback_btn = Button(frame, text='Go Back', width=30, height=2, bg="#2196f3", fg="white", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)

        txt = ''
        for entity, label in result['entities']:
            txt += f'{entity} -> {label}\n'

        self.ner_result['text'] = txt

    def emotion_gui(self):
        self.clear()

        frame = Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        heading = Label(frame, text="NLPApp", bg='#f0f0f0', fg='#333', font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 10))

        heading2 = Label(frame, text="Emotion Prediction", bg='#f0f0f0', fg='#333', font=('verdana', 20))
        heading2.pack(pady=(10, 10))

        label1 = Label(frame, text='Enter the text', bg='#f0f0f0', fg='#333', font=('verdana', 10))
        label1.pack(pady=(10, 5))
        
        self.emotion_input = Entry(frame, width=40)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(frame, text='Analyze Text', width=30, height=2, bg="#4caf50", fg="white", command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(frame, text='', bg='#f0f0f0', fg='#333', font=('verdana', 16))
        self.emotion_result.pack(pady=(10, 10))

        goback_btn = Button(frame, text='Go Back', width=30, height=2, bg="#2196f3", fg="white", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_prediction(text)

        txt = ''
        for emotion, score in result['emotions'].items():
            txt += f'{emotion} -> {score}\n'

        self.emotion_result['text'] = txt

nlp = NLPApp()
