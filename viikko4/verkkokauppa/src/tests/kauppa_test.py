import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        # palautetaan aina arvo 42
        #viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 8)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_usean_tuotteen_ostossa_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 13)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_saman_tuotteen_ostossa_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_loppuneen_tuotteen_ostossa_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_metodi_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekk", "1234")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekk', ANY, '1234', ANY, 13)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekk", "1234")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoskorista_voi_poistaa_tuotteita(self):


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, '12345', ANY, 8)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista