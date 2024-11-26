import unittest
from MODELO.ControlPlagas import PestControl

class TestPestControl(unittest.TestCase):
    def test_initialization(self):
        pest = PestControl(ica="123", name="Insecticide", price=15.99, applicationFrequency="15 dias", deficiencyPeriod="45 dias")
        self.assertEqual(pest.ica, "123")
        self.assertEqual(pest.name, "Insecticide")
        self.assertEqual(pest.price, 15.99)
        self.assertEqual(pest.applicationFrequency, "15 dias")
        self.assertEqual(pest.deficiencyPeriod, "45 dias")

    def test_setters_and_getters(self):
        pest = PestControl(ica="124", name="Herbicide", price=19.99, applicationFrequency="18 horas", deficiencyPeriod="100 dias")
        
        # Actualizamos las propiedades
        pest.name = "Updated Herbicide"
        pest.price = 25.00
        pest.applicationFrequency = "30 horas"
        pest.deficiencyPeriod = "120 dias"
        
        # Validamos los cambios
        self.assertEqual(pest.name, "Updated Herbicide")
        self.assertEqual(pest.price, 25.00)
        self.assertEqual(pest.applicationFrequency, "30 horas")
        self.assertEqual(pest.deficiencyPeriod, "120 dias")

    def test_str_method(self):
        pest = PestControl(ica="125", name="Fungicide", price=13.49, applicationFrequency="Bisemanalmente", deficiencyPeriod="30 dias")
        expected_output = "- Fungicide - $13.49 "
        self.assertEqual(str(pest), expected_output)
