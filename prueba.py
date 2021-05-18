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

def groupLayout(estudiantes, grupos):
    grupos_array=[]
    if estudiantes % grupos == 0:
        valor = int (estudiantes /grupos)

        for i in range (0, grupos):
            grupos_array.append(valor)
    else:
        min_grupo = int (estudiantes/grupos)
        remaining_students = estudiantes - (min_grupo*grupos)
        
        for i in range(grupos):
            grupos_array.append(min_grupo)
        
        remaining_array=[]

        while remaining_students > 0:
            random_value  = random.randint(0, grupos - 1)
            try: 
                remaining_array.index(random_value)
            except:
                grupos_array[random_value] += 1
                remaining_array.append(random_value)
                remaining_students-=1
                
    return grupos_array

def distribuirEstudiantes(estudiantes, cantidad_por_grupo):
    grupo_completo = [[] for i in range(len(cantidad_por_grupo))]

    for i, cantidad in enumerate(cantidad_por_grupo):
        for j in range(0, cantidad):
            grupo_completo[i].append(estudiantes.pop())

    return grupo_completo


def main():
    grupos = 6 #int(sys.argv[1])
    pathEstudiantes = "file1.txt" #sys.argv[2]
    pathTopics = "file2.txt" #sys.argv[3]

    estudiantes = getFileData(pathEstudiantes)
    topic = getFileData(pathTopics)
    
    if grupos > estudiantes:
        print("No pueden haber más grupos que estudiantes")
    if topic < grupos:
        print("No pueden haber más grupos que tópicos")
    else:
        estudiantes_por_grupo = groupLayout(estudiantes, grupos)
        temas_por_grupo = groupLayout(topic, grupos)
        topicReordenados = randomizeData(topic, pathTopics)
        estudiantesReordenados = randomizeData(estudiantes, pathEstudiantes)
        estudiantes_asignados = distribuirEstudiantes(estudiantesReordenados, estudiantes_por_grupo)
        temas_asignados = distribuirEstudiantes(topicReordenados, temas_por_grupo)

        print("\n Total de estudiantes:\n", estudiantes)
        print("\n Estudiantes asignados por grupo:\n", estudiantes_por_grupo)
        print("\n Total de temas:\n", topic)
        print("\n Total de temas por grupos\n", temas_por_grupo)


        counter = 1
        for grupos in estudiantes_asignados:
            print("\n Grupo ", counter, ":")
            print("\t temas: ")
            for temas in temas_asignados[counter - 1]:
                print("\t\t", temas)
            print("\tPersonas: ")
            for persona in grupos:
                print("\t\t", persona)
            print()
            counter +=1


        


    

main()