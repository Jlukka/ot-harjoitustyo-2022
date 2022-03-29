import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti1 = Maksukortti(50)
        self.kortti2 = Maksukortti(500)

    def test_kassan_saldo_alussa_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100)

    def test_kassan_edullisten_maara_alussa_oikein(self):
        self.assertEqual(self.paate.edulliset, 0)

    def test_kassan_maukkaiden_maara_alussa_oikein(self):
        self.assertEqual(self.paate.maukkaat, 0)

    def test_edullisen_osto_kateisella_lisaa_kassaan_rahaa(self):
        self.paate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100+240)

    def test_edullisen_osto_palauttaa_oikein(self):
        takaisin = self.paate.syo_edullisesti_kateisella(250)
        self.assertEqual(takaisin, 10)

    def test_edullisen_osto_kateisella_lisaa_myydyn_edullisen(self):
        self.paate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.paate.edulliset, 1)

    def test_edullisen_epaonnistunut_osto_ei_lisaa_kassaan_rahaa(self):
        takaisin = self.paate.syo_edullisesti_kateisella(120)
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100)

    def test_edullisen_epaonnistunut_osto_palauttaa_oikein(self):
        takaisin = self.paate.syo_edullisesti_kateisella(120)
        self.assertEqual(takaisin, 120)

    def test_maukkaan_epaonnistunut_osto_ei_lisaa_myytyja(self):
        self.paate.syo_maukkaasti_kateisella(120)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_maukkaan_osto_kateisella_lisaa_kassaan_rahaa(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100+400)

    def test_maukkaan_osto_palauttaa_oikein(self):
        takaisin = self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(takaisin, 100)

    def test_maukkaan_osto_kateisella_lisaa_myydyn_edullisen(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_maukkaan_epaonnistunut_osto_ei_lisaa_kassaan_rahaa(self):
        takaisin = self.paate.syo_maukkaasti_kateisella(120)
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100)

    def test_maukkaan_epaonnistunut_osto_palauttaa_oikein(self):
        takaisin = self.paate.syo_maukkaasti_kateisella(120)
        self.assertEqual(takaisin, 120)

    def test_maukkaan_epaonnistunut_osto_ei_lisaa_myytyja(self):
        self.paate.syo_maukkaasti_kateisella(120)
        self.assertEqual(self.paate.maukkaat, 0)
        
    def test_kortilla_edullisen_osto_veloittaa_oikein(self):
        vastaus = self.paate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(str(self.kortti2), "saldo: 2.6")
        self.assertTrue(vastaus)

    def test_kortilla_edullisen_osto_lisaa_myydyn_kassaan(self):
        self.paate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.paate.edulliset, 1)

    def test_kortilla_edullisen_osto_ei_lisaa_kassaan_rahaa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.paate.kassassa_rahaa, 100*1000)

    def test_kortilla_maukkaan_osto_veloittaa_oikein(self):
        vastaus = self.paate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(str(self.kortti2), "saldo: 1.0")
        self.assertTrue(vastaus)

    def test_kortilla_maukkaan_osto_lisaa_myydyn_kassaan(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_kortilla_maukkaan_osto_ei_lisaa_kassaan_rahaa(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.paate.kassassa_rahaa, 100*1000)
    
    def test_kortilla_edullisen_epaonnistunut_osto_ei_veloita_korttia(self):
        self.paate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), "saldo: 0.5")

    def test_kortilla_maukkaan_epaonnistunut_osto_ei_veloita_korttia(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), "saldo: 0.5")

    def test_kortilla_edullisen_epaonnistunut_osto_ei_muuta_myytyjen_maaraa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kortilla_maukkaan_epaonnistunut_osto_ei_muuta_myytyjen_maaraa(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_kortilla_edullisen_epaonnistunut_osto_palauttaa_false(self):
        self.assertFalse(self.paate.syo_edullisesti_kortilla(self.kortti1))

    def test_kortilla_maukkaasti_epaonnistunut_osto_palauttaa_false(self):
        self.assertFalse(self.paate.syo_maukkaasti_kortilla(self.kortti1))

    def test_kortille_lataus_lisaa_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti1, 50)
        self.assertEqual(str(self.kortti1), "saldo: 1.0")

    def test_kortille_lataus_kasvattaa_kassaa(self):
        self.paate.lataa_rahaa_kortille(self.kortti1, 50)
        self.assertEqual(self.paate.kassassa_rahaa, 1000*100+50)

    def test_kortille_negatiivisen_lataus_ei_muuta_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti1, -50)
        self.assertEqual(str(self.kortti1), "saldo: 0.5")