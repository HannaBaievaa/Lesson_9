class TextProcessor():
    def get_clean_string(text):
        result = []
        symbol = "!@#$%^&*()_+-={}:<>?/][;.,"
        for i in text :
            if i not in symbol :
                result.append(i)
        return ("".join(result))

print(TextProcessor.get_clean_string("vi!!ctor--y"))

    def __is_punktian(s) :
       punk = "!@#$%^&*()_+-={}:<>?/][;.,"
        if s in punk:
            return True
        else :
            return False

print(TextProcessor.__is_punktian(*))

class TextLoader(TextProcessor):
    def __init__(self, text_processor, clean_string):
        self.__text_processor = text_processor
        self.__clean_string = clean_strin

    def set_clean_text():

        @property
        def text_processor(self):
            return self.__text_processor

        @property
        def set_clean_text



