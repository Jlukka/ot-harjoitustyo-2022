import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodulla_kortilla_on_oikea_saldo(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")

    def test_rahan_ottaminen_rahaa_tarpeeksi_ollessa_toimii(self):
        otto = self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
        self.assertTrue(otto)

    def test_rahan_ottaminen_rahaa_liian_vahan_ollessa_toimii(self):
        otto = self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertFalse(otto)