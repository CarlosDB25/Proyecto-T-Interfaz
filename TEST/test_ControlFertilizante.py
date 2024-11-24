import unittest
from MODELO.ControlFertilizantes import FertilizerControl

class TestFertilizerControl(unittest.TestCase):
    def test_crear_fertilizer_control(self):
        control = FertilizerControl("1234", "Fertilizante A", 20000, 30, 15)
        self.assertEqual(control.ica, "1234")
        self.assertEqual(control.name, "Fertilizante A")
        self.assertEqual(control.price, 20000)
        self.assertEqual(control.applicationFrequency, 30)
        self.assertEqual(control.lastAdministration, 15)

    def test_setters_fertilizer_control(self):
        control = FertilizerControl("1234", "Fertilizante A", 20000, 30, 15)
        control.ica = "5678"
        control.name = "Fertilizante B"
        control.price = 25000
        control.applicationFrequency = 45
        control.lastAdministration = 20
        self.assertEqual(control.ica, "5678")
        self.assertEqual(control.name, "Fertilizante B")
        self.assertEqual(control.price, 25000)
        self.assertEqual(control.applicationFrequency, 45)
        self.assertEqual(control.lastAdministration, 20)

if __name__ == '__main__':
    unittest.main()
