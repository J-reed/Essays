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

        # Text boxes
        
        self.blog_title_text = tk.StringVar()
        self.blog_title_entry = ttk.Entry(self, width=10, textvariable=self.blog_title_text)
        self.blog_title_entry.place(bordermode='outside', relx=0.4, rely=0.1)

        # Buttons

        self.get_files_button = ttk.Button(self, text="Upload a document", command=lambda: self.get_document(SupportedLanguages.get_enum(self.language_string_variable.get())))
        self.get_files_button.place(bordermode='outside', relx=0.4, rely=0.6)

        self.upload_files_button = ttk.Button(self, text="Upload to website", command=lambda: self.upload_blog_files(self.blog_title_text.get()))
        self.upload_files_button.place(bordermode='outside', relx=0.6, rely=0.6)

    # Function for setting loading the files into the application and assiging their language
    def get_document(self, language: SupportedLanguages.LangEnum):
        f = filedialog.askopenfile(initialdir="./", title="Select a document to upload", filetypes=(('Article files', '*.md'), ('Any file', '*.*')))
        
        file_text = f.read()
        file_language_pair = (file_text, language)
        self.files_for_upload.append(file_language_pair)


    # Function to push the added files to the website locations and update the visible webpage
    def upload_blog_files(self, blog_title: str):
        
        formatter = FileFormatter()
        webpages_and_languages = [(formatter.create_webpage(*file_language_pair), file_language_pair[1]) for file_language_pair in self.files_for_upload]

        for webpage_language_pair in webpages_and_languages:
            save_webpage_location = webpageSaveLocation + SupportedLanguages.get_string(webpage_language_pair[1]) + "\\" + blog_title+".html"

            with open(save_webpage_location, 'w') as webpage:
                webpage.write(webpage_language_pair[0])

       