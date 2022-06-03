import os
import webbrowser

#поиск pdf в указанной директории( или в нашей если ничего не указано)
def find_files(dir_name):
    res = []
    if dir_name: os.chdir(dir_name)

    for file in os.listdir():
        if file.endswith(".pdf"):
            res.append(os.path.join(file))

    return res

#открываю pdf в браузере
def open_file(name):
    webbrowser.open_new(name)



