import unittest
from MODELO.ControlPlagas import PestControl


class TestPestControl(unittest.TestCase):
    def test_crear_pest_control(self):
        control = PestControl("4321", "Plaguicida X", 15000, 60, 10)
        self.assertEqual(control.ica, "4321")
        self.assertEqual(control.name, "Plaguicida X")
        self.assertEqual(control.price, 15000)
        self.assertEqual(control.applicationFrequency, 60)
        self.assertEqual(control.defiencyPeriod, 10)

    def test_setters_pest_control(self):
        control = PestControl("4321", "Plaguicida X", 15000, 60, 10)
        control.ica = "8765"
        control.name = "Plaguicida Y"
        control.price = 18000
        control.applicationFrequency = 90
        control.defiencyPeriod = 20
        self.assertEqual(control.ica, "8765")
        self.assertEqual(control.name, "Plaguicida Y")
        self.assertEqual(control.price, 18000)
        self.assertEqual(control.applicationFrequency, 90)
        self.assertEqual(control.defiencyPeriod, 20)

if __name__ == '__main__':
    unittest.main()
