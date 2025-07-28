# Suaraku Remaja 🎙️

Project web berbasis Django untuk program advokasi & konseling remaja, dilengkapi dengan fitur:
- Titipan Cerita (artikel seperti novel, editable dari admin).
- Ruang Bercerita (form curhat remaja).
- Halaman utama yang interaktif.

---

## 🚀 Persyaratan
Pastikan sudah menginstall:
- **Python 3.10+** (disarankan Python 3.13 seperti di project ini)
- **Git**
- **pip** (package manager bawaan Python)
- **Virtualenv** (opsional, tapi direkomendasikan)

---

## 🛠️ Setup Project

1. **Clone repository**
   ```bash
   git clone https://github.com/username/suaraku_django.git
   cd suaraku_django
2. Buat Virtual Environment
   python -m venv venv

   Aktifkan venv: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Jalankan migrasi database
   python manage.py migrate

5. Buat superuser (untuk admin panel)
   python manage.py createsuperuser

6. Jalankan server
   python manage.py rusnerver
