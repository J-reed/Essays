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
    def get_enum(lang_str: str):
        return SupportedLanguages.LangEnum(SupportedLanguages.string_arr.index(lang_str))

    @staticmethod
    def get_supported_languages():
        return SupportedLanguages.string_arr