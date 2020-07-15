import tkinter as tk

from tkinter import filedialog
from tkinter import ttk


from enum import Enum

class SupportedLanguages():

    string_arr = ["", "English", "French", "Spanish"]

    class LangEnum(Enum):
        ENGLISH = 1
        FRENCH = 2
        SPANISH = 3

    @staticmethod
    def get_string(lang: LangEnum):
        return SupportedLanguages.string_arr[lang.value]

    @staticmethod
    def get_supported_languages():
        return SupportedLanguages.string_arr

class AppInit(tk.Tk):

    # Initialise the GUI
    def __init__(self, *args, **kwargs):
        # Run the default tkinter constructor
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Essay Uploader")
        tk.Tk.wm_minsize(self, 1000, 400)

        # Global Variables

        self.language = SupportedLanguages.LangEnum.ENGLISH

        # GUI Elements

        self.button_model = ttk.Button(self, text="Button!", command=lambda: self.get_document(SupportedLanguages.LangEnum.ENGLISH))
        self.button_model.place(bordermode='outside', relx=0.4, rely=0.6)

        self.language_string_variable = tk.StringVar()
        self.language_string_variable.set(SupportedLanguages.get_string(self.language))
        
        self.language_box = ttk.OptionMenu(self, self.language_string_variable, *SupportedLanguages.get_supported_languages())
        self.language_box.place(bordermode='outside', relx=0.4, rely=0.3)

    # Function for setting the ANN model file to load
    def get_document(self, language: SupportedLanguages.LangEnum):
        f = filedialog.askopenfile(initialdir="./", title="Select a document to upload", filetypes=(('Article files', '*.docx'), ('Any file', '*.*')))

