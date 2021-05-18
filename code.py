import math
import numpy as np
import random
import sys

def getFileData(path):
    names = 0
    with open(path, 'r') as f:
        data = f.readlines()
        names = len(data)
    f.close()
    return names

def randomizeData(fileData, path):
    new_arr = []

    for i in range(fileData):
        newf=''
        check = False
        count = 0

        with open(path, 'r') as f:
            data = f.readlines()
            ran = random.randint(0, len(data) - 1)

            while True:
                if data[ran][0] != "*":
                    for line in data:
                        if line == data[ran]:
                            newf += "*" + line.strip() + "\n"
                            new_arr.append(line)
                            check = True

                        else:
                            newf += line.strip() + "\n"
                if check == True:
                    break
                else:
                    ran = random.randint(0, len(data) - 1)
                    count = count + 1
        f.close()

        with open (path, 'w') as f:
            f.write(newf)
        f.close()

    newf2 = ""

    with open(path, 'r') as f:
        data = f.readlines()
        for line in data:
            line = line.replace("*", "")
            newf2 += line.strip() + "\n"
    f.close()

    file1 = open(path, "r+")
    file1.truncate(0)
    file1.close()

    with open(path, 'w') as f:
        f.write(newf2)
    f.close()

    return new_arr

    

def main():
    grupos = 5
    pathEstudiantes = 'C:\\Users\\salma\\Desktop\\unit-test-group\\file1.txt'
    pathTopics = 'C:\\Users\\salma\\Desktop\\unit-test-group\\file2.txt'

    estudiantes = getFileData(pathEstudiantes)
    print(estudiantes)
    topic = getFileData(pathTopics)
    print(topic)

    if grupos > estudiantes:
        print("No pueden haber más grupos que estudiantes")
    if topic < grupos:
        print("No pueden haber más grupos que tópicos")
    else:
        topicReordenados = randomizeData(topic, pathTopics)
        print(topicReordenados)
        estudiantesReordenados = randomizeData(estudiantes, pathEstudiantes)
        print(estudiantesReordenados)
    

main()