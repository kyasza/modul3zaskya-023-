#Zaskya (023)
from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_get_all_buku_berhasil():
    model = BukuModel()

    # Database palsu (mock) supaya data asli tidak tersentuh
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Data palsu yang "dikembalikan" oleh database
    data_palsu = [
        {'id_buku': 1, 'judul': 'Buku A', 'penulis': 'Penulis A', 'tahun_terbit': 2020},
        {'id_buku': 2, 'judul': 'Buku B', 'penulis': 'Penulis B', 'tahun_terbit': 2021},
    ]
    mock_cursor.fetchall.return_value = data_palsu

    hasil = model.get_all_buku()

    # Hasil harus sama dengan data palsu
    assert hasil == data_palsu
    # Query SELECT harus dijalankan satu kali
    mock_cursor.execute.assert_called_once()
    # Cursor harus ditutup setelah dipakai
    mock_cursor.close.assert_called_once()

