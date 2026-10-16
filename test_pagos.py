import unittest

from pagos import registrar_pago


class TestRegistrarPago(unittest.TestCase):
    def test_registra_un_pago(self):
        pagos = {}
        self.assertTrue(registrar_pago(pagos, "YAPE-001", 1500))
        self.assertEqual(pagos, {"YAPE-001": 1500})

    def test_no_registra_dos_veces_la_misma_referencia(self):
        pagos = {}
        registrar_pago(pagos, "YAPE-001", 1500)
        self.assertFalse(registrar_pago(pagos, "YAPE-001", 1500))
        self.assertEqual(len(pagos), 1)

    def test_rechaza_monto_no_positivo(self):
        with self.assertRaises(ValueError):
            registrar_pago({}, "YAPE-002", 0)


if __name__ == "__main__":
    unittest.main()
