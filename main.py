from translate import Translator

translator = Translator(to_lang="ta")


try:
    with open("translate.txt", mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("Check file path")