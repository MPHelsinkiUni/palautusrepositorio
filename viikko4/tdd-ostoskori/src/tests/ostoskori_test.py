import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 10)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 13)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_korin_ostos_nimi_ja_maara_vastaavat_lisattya_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 10)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_saman_tuotteen_kahdesti_lisaaminen_luo_yhden_ostoksen(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_saman_tuotteen_kahdesti_lisaaminen_yhdistaa_nimen_ja_maaran(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_saman_tuotteen_kahdesti_lisaaminen_luo_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_tyhjenna(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.tyhjenna()

        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)