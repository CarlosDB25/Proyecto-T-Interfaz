import unittest
from MODELO.ControlFertilizantes import FertilizerControl

class TestFertilizerControl(unittest.TestCase):
    def test_initialization(self):
        fertilizer = FertilizerControl(ica=234, name="Nitrogen Fertilizer", price=9.99, applicationFrequency="Mensual", lastAdministration="11-07-2024")
        
        # Validar inicialización de atributos
        self.assertEqual(fertilizer.ica, 234)
        self.assertEqual(fertilizer.name, "Nitrogen Fertilizer")
        self.assertEqual(fertilizer.price, 9.99)
        self.assertEqual(fertilizer.applicationFrequency, "Mensual")
        self.assertEqual(fertilizer.lastAdministration, "11-07-2024")

    def test_setters_and_getters(self):
        fertilizer = FertilizerControl(ica=235, name="Phosphorus Fertilizer", price=11.99, applicationFrequency="8 dias", lastAdministration="01-03-2024")
        
        # Cambiar valores mediante setters
        fertilizer.name = "Updated Fertilizer"
        fertilizer.price = 12.50
        fertilizer.applicationFrequency = "15 dias"
        fertilizer.lastAdministration = "05-06-2024"
        
        # Validar cambios
        self.assertEqual(fertilizer.name, "Updated Fertilizer")
        self.assertEqual(fertilizer.price, 12.50)
        self.assertEqual(fertilizer.applicationFrequency, "15 dias")
        self.assertEqual(fertilizer.lastAdministration, "05-06-2024")

    def test_str_method(self):
        fertilizer = FertilizerControl(ica=236, name="Potassium Fertilizer", price=14.25, applicationFrequency="Semanal", lastAdministration="25-10-2024")
        expected_output = "- Potassium Fertilizer - $14.25"
        self.assertEqual(str(fertilizer), expected_output)
