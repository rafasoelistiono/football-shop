# Football Shop - PBP

## Tautan Aplikasi
Aplikasi ini telah di-deploy di PWS: [https://rafa-rally-footballshop.pbp.cs.ui.ac.id/]  

---

## Step-by-Step Implementasi Checklist

langkah implementasi aplikasi Football Shop saya secara step-by-step:

1. **Membuat Proyek Django Baru**
   - Membuat virtual environment: `python -m venv venv`
   - Mengaktifkan environment: `source venv/bin/activate.bat`
   - Menginstall Requirements yang sesuai dengan tutorial: `pip install -r requirements.txt`
   - Membuat proyek: `django-admin startproject football_shop .`
   - Melakukan setting git, pws, dan melakukan pengunggahan repo

2. **Membuat Aplikasi `main`**
   - Perintah: `python manage.py startapp main`
   - Menambahkan `'main'` ke dalam `INSTALLED_APPS` di `settings.py` projek football-shop

3. **Membuat Model `Product`**
   - Atribut wajib: `name`, `price`, `description`, `thumbnail`, `category`, `is_featured`
   - Atribut tambahan: `stock`, `brand`, `rating`
   - Menjalankan migrasi:  
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Pada saat membuat model, saya melakukan beberapa adjustment data dan menambahkan atribut opsional seperti stock, brand, dan rating (0-5). menambahkan logic penambahan barang terjual serta popular item (based on tutorial)

4. **Membuat Views dan Template**
   - Views di `main/views.py` menampilkan nama aplikasi, nama, dan kelas
   - Template HTML di `templates/main.html`

5. **Routing**
   - Buat `main/urls.py` untuk memetakan view `home`
   - Include `main.urls` di `football_shop/urls.py`

6. **Testing Lokal**
   - `python manage.py runserver` dan buka `http://127.0.0.1:8000/`

7. **Deployment ke PWS**
   - Commit ke Git: `git add .` dan `git commit -m "Initial commit"`
   - Push ke remote PWS: `git push pws master`

---

## Bagan Request-Response Django

        Client/Browser
              │
              │ HTTP Request (GET /)
              ▼
            urls.py
        (routing URL)
              │
              │ memanggil fungsi view
              ▼
           views.py
       (logic & context)
              │
              │ mengambil data dari models.py yang berisikan product
              ▼
          models.py
           (database)
              │
              │ mengirim data ke template yang berisikan HTML
              ▼
        Template HTML
        (rendered page)
              │
              │ HTTP Response (HTML)
              ▼
        Client/Browser


**Kaitan tiap komponen:**
- `urls.py` → menentukan URL mana yang memanggil fungsi tertentu dalam kasus ini urls akan beranjak dari proyek ke main hingga masuk ke view dan tampilkan html
- `views.py` → memproses request, mengambil data dari models, dan mengirim ke template html yang dibuat
- `models.py` → berisi struktur data product yang didefinisikan
- Template HTML → menampilkan data ke user (masih tahap beta)

---

## Peran `settings.py` dalam Django
- Mengatur konfigurasi proyek secara global:
  - Mengatur Database (`DATABASES`)
  - Aplikasi yang terinstall dan fitur yang bertambah (`INSTALLED_APPS`)
  - Menambahkan host yang disetujui web (`ALLOWED_HOST`)
  - Middleware, security, localization, dsb.

---

## Cara Kerja Migrasi Database
1. `makemigrations` → membuat file migrasi berdasarkan perubahan model yang dibuat developer
2. `migrate` → mengeksekusi migrasi dan membuat/ubah tabel di database dalam kasus ini sqlite
3. Django akan otomatis melacak setiap perubahan model agar database tetap sinkron

---

## Mengapa Django Dijadikan Permulaan
- Django menyediakan banyak fitur built-in seperti admin, dan url siap pakai
- Struktur MVT nya jelas sehingga mudah dilakukan pengembangan atau debugging
- memiliki struktur yang ringkas dan mudah digunakan
- fitur testing yang mudah dan cukup lengkap librarynya

---

## Feedback untuk Asisten Dosen Tutorial 1
- Materi sudah jelas dan sistematis
- Mudah digunakan

---

