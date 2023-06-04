class TextProcessor():
    def get_clean_string(text):
        result = []
        symbol = "!@#$%^&*()_+-={}:<>?/][;.,"
        for i in text :
            if i not in symbol :
                result.append(i)
        return ("".join(result))
print(TextProcessor.get_clean_string("Vik--tor!&y"))





