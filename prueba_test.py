import unittest
from prueba import getFileData, randomizeData, groupLayout
import math

class Test_getFileData(unittest.TestCase):
    def test_getFileData(test):
        pathEstudiantes = "file1.txt"
        dataCount = getFileData(pathEstudiantes)
        test.assertAlmostEqual(dataCount, 12)

class Test_groupLayout(unittest.TestCase):

    def test_groupDistribution(test):
        estudiantes = 12
        grupos = float(7)
        if (estudiantes % grupos == 0):
            test.defaultTestResult(True)
        else:
            estudiantes_por_grupo = int(estudiantes/grupos)
            remanente = float(estudiantes - (estudiantes_por_grupo*grupos))
            posibles_combinaciones = (math.factorial(grupos))/(math.factorial(grupos-remanente)*math.factorial(remanente))
            probabilidad_combinacion = 1/posibles_combinaciones
            array = []
            estudiantes = int(estudiantes)
            grupos = int(grupos)
            array = groupLayout(estudiantes, grupos)
            count = 0
            ejecuciones = 10000
            for i in range (ejecuciones):
                if (groupLayout(estudiantes, grupos) == array):
                    count += 1

            test.assertFalse(count >= (probabilidad_combinacion*ejecuciones)+30)

class Test_topicDistribution(unittest.TestCase):
    def test_topicDistribution(test):
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
            array = groupLayout(temas, grupos)
            count = 0
            ejecuciones = 10000
            for i in range(ejecuciones):
                if(groupLayout(temas, grupos) == array):
                    count  += 1
            test.assertFalse(count >= (probabilidadesCombinacion * ejecuciones) + 30)

class Test_randomizeData(unittest.TestCase):
    def test_randomizeData(test):
        pathEstudiantes = "file1.txt"
        estudiantes = getFileData(pathEstudiantes)
        posiblesCombinaciones = math.factorial(estudiantes)
        posibilidadCombinacion = 1/posiblesCombinaciones

        array = []
        array = randomizeData(estudiantes, pathEstudiantes)
        count = 0
        ejecuciones = 1000
        for i in range(ejecuciones):
            if(randomizeData(estudiantes, pathEstudiantes) == array):
                count += 1
        
        test.assertFalse(count >= (posibilidadCombinacion * ejecuciones))

if __name__ == '__main__':
    unittest.main()
