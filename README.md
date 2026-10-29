# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan adalah aplikasi desktop berbasis **Python** dengan arsitektur **MVC (Model-View-Controller)**. Antarmuka dibuat dengan **CustomTkinter** dan data disimpan di **MySQL**.

Fitur utama:

- Login dengan password ter-hash SHA-256
- Otorisasi berbasis peran: `admin` dapat mengelola data buku, `anggota` hanya dapat melihat
- Manajemen data buku (judul, penulis, tahun terbit)
- Logout

## 2. Struktur Direktori MVC

```
modul3zaskya-023-/
├── .github/workflows/ci_pipeline.yml   # CI GitHub Actions
├── config/database.py                  # Koneksi MySQL
├── models/                             # MODEL
│   ├── buku_model.py
│   └── user_model.py
├── views/                              # VIEW
│   ├── buku_view.py
│   └── login_view.py
├── controllers/                        # CONTROLLER
│   ├── auth_controller.py
│   └── buku_controller.py
├── tests/                              # Unit test (pytest)
│   ├── test_auth.py
│   └── test_buku.py
├── main.py                             # Titik masuk aplikasi
├── requirements.txt
└── README.md
```

## 3. Instalasi dan Konfigurasi Database MySQL

**Prasyarat:** Python 3.11+, Laragon (MySQL), Git.

**Instal dependensi:**

```bash
git clone https://github.com/kyasza/modul3zaskya-023-.git
cd modul3zaskya-023-
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt
```

**Konfigurasi database:**

1. Jalankan MySQL lewat Laragon (**Start All**).
2. Buka Terminal Laragon, lalu masuk ke MySQL: `mysql -u root -p`
3. Jalankan query berikut:

```sql
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

CREATE TABLE IF NOT EXISTS buku (
    id_buku INT PRIMARY KEY AUTO_INCREMENT,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(100) NOT NULL,
    tahun_terbit INT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
);

INSERT INTO users (username, password, role) VALUES
('petugas', SHA2('admin123', 256), 'admin'),
('mahasiswa', SHA2('user123', 256), 'anggota');
```

4. Pastikan `config/database.py` sesuai dengan MySQL kamu (bawaan Laragon: `host=localhost`, `user=root`, password kosong).

## 4. Cara Menjalankan Aplikasi

1. Pastikan MySQL di Laragon sudah menyala.
2. Aktifkan virtual environment, lalu jalankan:

```bash
python main.py
```

3. Login dengan akun uji coba:

| Username | Password | Role |
|---|---|---|
| `petugas` | `admin123` | admin |
| `mahasiswa` | `user123` | anggota |