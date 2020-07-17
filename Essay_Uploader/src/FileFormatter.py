import os
import markdown

from SupportedLanguages import SupportedLanguages

headerAndFooterFilePath = os.path.abspath('.')+"\\docs\\headers and footers\\"

# Class for taking markdown files and converting them to html pages and adds a head and footer
class FileFormatter:

    

    def __init__(self, header_file_name: str = "blog_header.html", footer_file_name: str = "blog_footer.html"):

        self.header_file_name = header_file_name
        self.footer_file_name = footer_file_name


    def get_header_and_footer_text(self, language_enum: SupportedLanguages.LangEnum):
        
        language = SupportedLanguages.get_string(language_enum)
        header_file_location = headerAndFooterFilePath + language + "\\" + self.header_file_name
        footer_file_location = headerAndFooterFilePath + language + "\\" + self.footer_file_name

        header_file = open(header_file_location, 'r')
        footer_file = open(footer_file_location, 'r')

        header_text = header_file.read()
        footer_text = footer_file.read()

        return header_text, footer_text

    def create_webpage(self, file: str, language: SupportedLanguages.LangEnum):

        # Convert markdown file to html
        file_html = markdown.markdown(file)

        # Apply do any extra formatting here!

        # Add the designated header and footer to the webpage
        header_text, footer_text = self.get_header_and_footer_text(language)
        final_file = header_text + file_html + footer_text

        return final_file