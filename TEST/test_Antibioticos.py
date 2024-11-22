import unittest
from MODELO.Antibiotico import Antibiotic

class TestAntibiotic(unittest.TestCase):
    def test_crear_antibiotic(self):
        antibiotic = Antibiotic("Antibiótico A", 12000, 500, "Bovino")
        self.assertEqual(antibiotic.name, "Antibiótico A")
        self.assertEqual(antibiotic.price, 12000)
        self.assertEqual(antibiotic.dose, 500)
        self.assertEqual(antibiotic.animalType, "Bovino")

    def test_setters_antibiotic(self):
        antibiotic = Antibiotic("Antibiótico A", 12000, 500, "Bovino")
        antibiotic.name = "Antibiótico B"
        antibiotic.price = 14000
        antibiotic.dose = 600
        antibiotic.animalType = "Porcino"
        self.assertEqual(antibiotic.name, "Antibiótico B")
        self.assertEqual(antibiotic.price, 14000)
        self.assertEqual(antibiotic.dose, 600)
        self.assertEqual(antibiotic.animalType, "Porcino")

if __name__ == '__main__':
    unittest.main()
