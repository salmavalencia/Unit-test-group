import unittest 
import code

import numpy 
import math

class test_getFileData(unittest.TestCase):
    def getFile(test):
        pathEstudiantes = "file1.txt"
        dataCount = code.getFileData(pathEstudiantes)
        test.assertAlmostEqual(dataCount, 12)

class test_groupLayout(unittest.TestCase):
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
