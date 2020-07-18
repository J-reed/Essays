import os
import tkinter as tk

from tkinter import filedialog
from tkinter import ttk

from FileFormatter import FileFormatter
from SupportedLanguages import SupportedLanguages


webpageSaveLocation = os.path.abspath('.')+"\\docs\\blogs\\"

class AppInit(tk.Tk):

    # Initialise the GUI
    def __init__(self, *args, **kwargs):
        # Run the default tkinter constructor
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Essay Uploader")
        tk.Tk.wm_minsize(self, 1000, 400)

        # Global Variables

        # Initialise to OptionMenu to this Language
        self.language = SupportedLanguages.LangEnum.ENGLISH
        self.files_for_upload = []

        ################
        # GUI Elements
        ################

        # Labels

        # Option Menu
        self.language_string_variable = tk.StringVar()
        self.language_string_variable.set(SupportedLanguages.get_string(self.language))
        
        self.language_box = ttk.OptionMenu(self, self.language_string_variable, *SupportedLanguages.get_supported_languages())
        self.language_box.place(bordermode='outside', relx=0.4, rely=0.3)

        # Buttons

        self.get_files_button = ttk.Button(self, text="Upload a document", command=lambda: self.get_document(SupportedLanguages.get_enum(self.language_string_variable.get())))
        self.get_files_button.place(bordermode='outside', relx=0.4, rely=0.6)

        self.upload_files_button = ttk.Button(self, text="Upload to website", command=lambda: self.upload_blog_files())
        self.upload_files_button.place(bordermode='outside', relx=0.6, rely=0.6)

    # Function for setting loading the files into the application and assiging their language
    def get_document(self, language: SupportedLanguages.LangEnum):
        f = filedialog.askopenfile(initialdir="./", title="Select a document to upload", filetypes=(('Article files', '*.md'), ('Any file', '*.*')))
        
        # Gets the name of the file selected
        file_title = ((f.name).split('/')[-1]).split('.')[0]
        print("hi ", file_title)
        # Get the contents of the file
        file_text = f.read()
        
        title_file_language_triple = [file_title, file_text, language]
        self.files_for_upload.append(title_file_language_triple)


    # Function to push the added files to the website locations and update the visible webpage
    def upload_blog_files(self):
        
        formatter = FileFormatter()
   
        for title_webpage_language_triple in self.files_for_upload:
            title = title_webpage_language_triple[0]
            webpage = formatter.create_webpage(*title_webpage_language_triple[1:])
            language = title_webpage_language_triple[2]

            save_webpage_location = webpageSaveLocation + SupportedLanguages.get_string(language) + "\\" + title +".html"

            with open(save_webpage_location, 'w') as saved_webpage_file:
                saved_webpage_file.write(webpage)

       