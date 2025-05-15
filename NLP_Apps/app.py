from tkinter import *
from mydb import *
from tkinter import messagebox
from tkinter import scrolledtext
from myapi import *

class NLPApp():

    def __init__(self):

        # Initialize the database  
        self.dbo = MyDB()
        self.aipi = API()

        # login window
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap("logo/favicon.ico")
        self.root.geometry("400x600")
        self.root.config(bg="#67dbc8")

        self.login()

        self.root.mainloop()


    def login(self):
      self.clear()
      heading = Label(self.root, text="Login", font=("Arial", 20), bg="#67dbc8",fg="white")   
      heading.pack(pady=(20,20))
      heading.configure(font=('verdana', 20, 'bold'))

      # Email
      email_label = Label(self.root, text="Enter your Email ", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
      email_label.pack(pady=(20,0))

      self.email_input = Entry(self.root, font=("Arial", 12), width=30)
      self.email_input.pack(pady=(0,20),ipady=4)

      # password
      pass_label = Label(self.root, text="Enter your password ", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
      pass_label.pack(pady=(20,0))

      self.pass_input = Entry(self.root, font=("Arial", 12), width=30,show='*')
      self.pass_input.pack(pady=(0,20),ipady=4)
    
      # register button

      login_button = Button(self.root, text="Login", font=("Arial", 12),fg="black",width=20,command=self.perform_login)
      login_button.pack(pady=(20,0)) 

      # Not a member
      login_label = Label(self.root, text="Not a member", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
      login_label.pack(pady=(20,0))

      redirect_button = Button(self.root, text="Register Now", font=("Arial", 12),fg="black",width=20,command=self.redirect)
      redirect_button.pack(pady=(20,0)) 



    def redirect(self):
        self.clear()

        heading = Label(self.root, text="Login", font=("Arial", 20), bg="#67dbc8",fg="white")   
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana', 20, 'bold'))

        # Name
        name_label = Label(self.root, text="Name ", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
        name_label.pack(pady=(20,0))

        self.name_input = Entry(self.root, font=("Arial", 12), width=30)
        self.name_input.pack(pady=(0,20),ipady=4)

        # Email
        email_label = Label(self.root, text="Enter your Email: ", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
        email_label.pack(pady=(20,0))

        self.email_input = Entry(self.root, font=("Arial", 12), width=30)
        self.email_input.pack(pady=(0,20),ipady=4)

        # password
        pass_label = Label(self.root, text="Enter your password: ", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
        pass_label.pack(pady=(20,0))

        self.pass_input = Entry(self.root, font=("Arial", 12), width=30,show='*')
        self.pass_input.pack(pady=(0,20),ipady=4)
        
        # register button
        register_button = Button(self.root, text="Register", font=("Arial", 12),fg="black",width=20,command=self.perform_registration)
        register_button.pack(pady=(20,0)) 

        # already a member
        already_label = Label(self.root, text=" Already member", font=("Arial", 12), bg="#67dbc8",fg="black",width=20)
        already_label.pack(pady=(20,0))

        redirect_button = Button(self.root, text="Login Now", font=("Arial", 12),fg="black",width=20,command=self.login)
        redirect_button.pack(pady=(20,0)) 


    def clear(self):
        # Clear the existing gui elements
        for element in self.root.pack_slaves():
            element.destroy()
       
    

    def perform_registration(self):

        # Perform registration logic here
        name = self.name_input.get()
        email = self.email_input.get()  
        password = self.pass_input.get()

        response = self.dbo.add_data(name, email, password)


        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        # Perform login logic here
        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Invalid email or password')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text="WelCome", font=("Arial", 20), bg="#67dbc8",fg="white")   
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana', 20, 'bold'))

        # Sentiment Analysis
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 0))

        # Named Entity Recognition
        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,command=self.ner_gui) 
        ner_btn.pack(pady=(20,0))

        # Language Detection
        lang_btn = Button(self.root, text='Language Detection', width=30, height=4,command=self.language_gui)
        lang_btn.pack(pady=(20,0))

        # Logout
        logout_btn = Button(self.root, text='Logout',width=20, height=4,command=self.login)
        logout_btn.pack(pady=(20, 0))

    
    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        # For Sentiment Analysis Text
        sent_label = Label(self.root, text='Enter the text',width=15, font=("Arial", 20), bg="#67dbc8",fg="black")
        sent_label.pack(pady=(20, 0))

        # For Extract the text
        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(20, 0), ipady=4)

        # For Sentiment Analysis Button
        sentiment_btn = Button(self.root, text='Analyze Sentiment',width=30, height=3, command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(20, 0))

        # For Sentiment Analysis Result
        self.sentiment_result = Label(self.root, text='',bg='#67dbc8',fg='black',width=30)
        self.sentiment_result.pack(pady=(20, 0))
        self.sentiment_result.configure(font=('verdana', 16))

        # For Goback Button
        goback_btn = Button(self.root, text='Go Back',width=20, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        # For NER Text label and extracting the text
        ner_txt_label = Label(self.root, text='Enter the text',width=15, font=("Arial", 20), bg="#67dbc8",fg="black")
        ner_txt_label.pack(pady=(20, 0))
        self.ner_txt_input = Entry(self.root, width=50)
        self.ner_txt_input.pack(pady=(20, 0), ipady=4)

        # For NER Entity label and extracting the entity
        ner_entity_label = Label(self.root, text='What would you like to search',width=30, font=("Arial", 16), bg="#67dbc8",fg="black")
        ner_entity_label.pack(pady=(20, 0))
        self.ner_entity_input = Entry(self.root, width=50)
        self.ner_entity_input.pack(pady=(20, 0), ipady=4)

        # For NER Button
        ner_btn = Button(self.root, text='Search Entity',width=20, height=1, command=self.do_ner_analysis)
        ner_btn.pack(pady=(20, 0))

        # show the result
        self.text_widget = scrolledtext.ScrolledText(self.root, height=6, width=30,
                                                      font=("Arial", 12), bg="#67dbc8",fg="black")
        self.text_widget.pack(padx=5, pady=5)
        # Configure the 'center' tag with center justification
        self.text_widget.tag_configure('center', justify='center')
        
        # For Goback Button
        goback_btn = Button(self.root, text='Go Back',width=20, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def language_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Language Detection', font=("Arial", 20), bg="#67dbc8",fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        # For Language Detection Text
        lang_label = Label(self.root, text='Enter the text',width=15, font=("Arial", 20), bg="#67dbc8",fg="black")
        lang_label.pack(pady=(20, 0))

        # For Extract the text
        self.lang_input = Entry(self.root, width=50)
        self.lang_input.pack(pady=(20, 0), ipady=4)

        # For Language Detection Button
        lang_btn = Button(self.root, text='Detected Language',width=30, height=3, command=self.do_language_detection)
        lang_btn.pack(pady=(20, 0))

        # For Language Detection Result
        self.lang_result = Label(self.root, text='',bg='#67dbc8',fg='black',width=30)
        self.lang_result.pack(pady=(20, 0))
        self.lang_result.configure(font=('verdana', 16))
      
        # For Goback Button
        goback_btn = Button(self.root, text='Go Back',width=20, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))




    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()

        # Check if the service is available
        try:
            resuslt = self.aipi.sentiment_analysis(text)
        except Exception as e:
            messagebox.showerror('Error', 'An error occurred while processing the request.')
            return
        # for output
        self.sentiment_result['text'] = resuslt


    def do_ner_analysis(self):
        text = self.ner_txt_input.get()
        entity = self.ner_entity_input.get()

        # Check if the service is available
        try:
            result = self.aipi.ner_analysis(text, entity)
        except Exception as e:
            messagebox.showerror('Error', 'An error occurred while processing the request.')
            return 
        
        # for output
        for name in result['entities']:
          self.text_widget.insert(END, name['text'] + '\n')
        # Make the text widget read-only
        self.text_widget.config(state='disabled')

    def do_language_detection(self):
        text = self.lang_input.get()

        # Check if the service is available
        try:
            result = self.aipi.language_detection(text)
        except Exception as e:
            messagebox.showerror('Error', 'An error occurred while processing the request.')
            return
        # for output
        self.lang_result['text'] = result
      
       

nlp = NLPApp()