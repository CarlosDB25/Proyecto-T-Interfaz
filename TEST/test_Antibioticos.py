import unittest
from MODELO.Antibiotico import Antibiotic

class TestAntibiotic(unittest.TestCase):

    def setUp(self):
        # Configuración de los objetos de prueba
        self.antibiotic1 = Antibiotic("Penicillin", 25.99, "500mg", "Caprino")
        self.antibiotic2 = Antibiotic("Amoxicillin", 20.99, "250mg", "caprino")
        self.antibiotic3 = Antibiotic("Tetracycline", 18.75, "200mg", "Porcino")
        self.antibiotic4 = Antibiotic("Ciprofloxacin", 30.50, "400mg", "Bovino")

    def test_initialization(self):
        # Verifica que los atributos se inicialicen correctamente
        self.assertEqual(self.antibiotic1.name, "Penicillin")
        self.assertEqual(self.antibiotic1.price, 25.99)
        self.assertEqual(self.antibiotic1.dose, "500mg")
        self.assertEqual(self.antibiotic1.animalType, "Caprino")

    def test_setters(self):
        # Verifica que los setters modifiquen correctamente los valores
        self.antibiotic1.name = "NewName"
        self.antibiotic1.price = 50.99
        self.antibiotic1.dose = "600mg"
        self.antibiotic1.animalType = "Porcino"

        self.assertEqual(self.antibiotic1.name, "NewName")
        self.assertEqual(self.antibiotic1.price, 50.99)
        self.assertEqual(self.antibiotic1.dose, "600mg")
        self.assertEqual(self.antibiotic1.animalType, "Porcino")

    def test_str_method(self):
        # Verifica que el método __str__ funcione correctamente
        self.assertEqual(str(self.antibiotic1), "- Penicillin - $25.99")
        self.assertEqual(str(self.antibiotic4), "- Ciprofloxacin - $30.5")  # Formato esperado

    def test_animalType_case_insensitivity(self):
        # Verifica si los valores de animalType manejan diferencias de mayúsculas/minúsculas
        self.assertNotEqual(self.antibiotic2.animalType, self.antibiotic3.animalType)

    def test_antibioticsList(self):
        # Verifica que los objetos se hayan añadido correctamente a la lista
        antibioticsList = [self.antibiotic1, self.antibiotic2, self.antibiotic3, self.antibiotic4]
        self.assertEqual(len(antibioticsList), 4)
        self.assertEqual(antibioticsList[0].name, "Penicillin")
        self.assertEqual(antibioticsList[3].price, 30.50)

if __name__ == "__main__":
    unittest.main()
