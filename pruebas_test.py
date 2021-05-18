import unittest 
import code
import math

class Test_getFileData(unittest.TestCase):
    def getFile(test):
        pathEstudiantes = "file1.txt"
        dataCount = code.getFileData(pathEstudiantes)
        test.assertAlmostEqual(dataCount, 12)

class Test_groupLayout(unittest.TestCase):
    def groupDistribution(test):
        estudiantes = 12
        grupos = float(6)
        if (estudiantes % grupos == 0):
            test.defaultTestResult()
        else:
            estudiantes_por_grupo = int(estudiantes/grupos)
            remanente = float(estudiantes - (estudiantes_por_grupo*grupos))
            posibles_combinaciones = (math.factorial(grupos))/(math.factorial(grupos-remanente)*math.factorial(remanente))
            probabilidad_combinacion = 1/posibles_combinaciones
            array = []
            estudiantes = int(estudiantes)
            grupos = int(grupos)
            array = code.groupLayout(estudiantes, grupos)
            count = 0
            ejecuciones = 10000
            for i in range (ejecuciones):
                if (code.groupLayout(estudiantes, grupos) == array):
                    count += 1

            test.assertFalse(count >= (probabilidad_combinacion*ejecuciones)+30)

class test_topicDistribution(unittest.TestCase):
    def topicDstrb_test(test):
        temas = 8
        grupos = float(6)
        if(temas % grupos == 0):
            test.defaultTestResult(True)
        else:
            temasPorGrupo = int(temas/grupos)
            remanente = float(temas - (temasPorGrupo*grupos))
            posiblesCombinaciones = (math.factorial(grupos))/(math.factorial(grupos - remanente) * math.factorial(remanente))
            probabilidadesCombinacion = 1/posiblesCombinaciones
            array = []
            temas = int(temas)
            grupos = int(grupos)
            array = code.groupLayout(temas, grupos)
            count = 0
            ejecuciones = 10000
            for i in range(ejecuciones):
                if(code.groupLayout(temas, grupos) == array):
                    count  += 1
            test.assertFalse(count >= (probabilidadesCombinacion * ejecuciones) + 30)

class test_randomizeData(unittest.TestCase):
    def rndmData_test(test):
        pathEstudiantes = "file1.txt"
        estudiantes = code.getFileData(pathEstudiantes)
        posiblesCombinaciones = math.factorial(estudiantes)
        posibilidadCombinacion = 1/posiblesCombinaciones

        array = []
        array = code.randomizeData(estudiantes, pathEstudiantes)
        count = 0
        ejecuciones = 10000
        for i in range(ejecuciones):
            if(code.randomizeData(estudiantes, pathEstudiantes) == array):
                count += 1
        
        test.assertFalse(count >= (posibilidadCombinacion * ejecuciones))



