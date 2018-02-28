def readTitle():
    file = open("D:/IdeaProjectsNew/PythonGit/gpPython/2.txt", encoding="utf-8")

    while 1:
        line = file.readline()

        if line.find('### ') == 1:
            print(line.replace('#### ', '').replace('\n', '|'))

        if not line:
            break
        pass  # do something


if __name__ == "__main__":
    readTitle()
