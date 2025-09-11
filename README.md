# Football Shop - PBP

## Tautan Aplikasi
Aplikasi ini telah di-deploy di PWS: [https://rafa-rally-footballshop.pbp.cs.ui.ac.id/]  

---

## Jawaban Pertanyaan Tugas 2

langkah implementasi aplikasi football shop saya secara step-by-step:

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
   - `python manage.py runserver` buka `http://127.0.0.1:8000/`

7. **Deployment ke PWS**
   - Commit ke Git: `git add .` dan `git commit -m "Initial commit"`
   - Push ke remote PWS: `git push pws master`

---

## Bagan Request-Response Django

        Client/Browser
              │
              │ HTTP Request melakukan get
              ▼
            urls.py
        (routing URL)
              │
              │ memanggil fungsi views.py dalam main
              ▼
           views.py
           (logic)
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
- Materi sudah jelas 
- Mudah digunakan

---

# Jawaban Pertanyaan Tugas 3

---

## Mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

Platform merupakan sebuah wadah dimana data dibaca atau ditransfer satu sama lain baik dari sisi server maupun sisi klien, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya antara lain XML dan JSON. Hal inilah yang Memudahkan komunikasi antar-komponen (server - frontend - API konsumer) serta mampu memfasilitasi penyimpanan dan pertukaran data dengan format standar. Maka dari itu, mengapa data delivery penting dalam sebuah platform.
---

## XML dan JSON mana yang lebih baik.

**XML**:

* Self-descriptive
* Dikemas dalam bentuk tag
* Dapat menangani struktur data kompleks
* Perlu mengandung root element

**JSON**:

* Self-descriptive
* Sintaks ringkas dan mudah dipakai.
* Lebih mudah diparsing oleh banyak bahasa, terutama JavaScript beserta frameworknya.

**Kesimpulan:** Karena ringkas dan mudah dipakai, JSON lebih populer dan sering digunakan oleh berbagai aplikasi web modern

---

## Fungsi `is_valid()` pada form Django

`is_valid()` pada Form/ModelForm Django berfungsi menjalankan validasi field sesuai definisi model/form serta menghasilkan `data` jika valid. Selain itu `is_valid` mampu mengisi `errors` jika ada kesalahan. Hal ini penting untuk mencegah data tidak valid yang masuk dan memberikan pesan error.

## Pentingnya `csrf_token` pada form Django

Django membutuhkan `{% csrf_token %}` untuk melindungi aplikasi dari **Cross-Site Request Forgery (CSRF)**. Resiko ketika tidak menggunakan `csrf_token` adalah hacker dapat membuat form di domain berbahaya yang mengirim request ke aplikasi kita dengan menggunakan cookie korban. Cookie inilah yang dapat dimanfaatkan penyerang untuk masuk ke salah satu aplikasi kita untuk memeras, mencuri data, dsb

**Dengan CSRF Token:**

* Setiap request POST diverifikasi oleh middleware Django.
* Request dari sumber eksternal tanpa token valid baik dari bot akan ditolak mentah-mentah

---

## Implementasi Checklist (Step-by-Step)

1. **Buat Template Dasar** 
   - Membuat `base.html` dengan `{% block %}`. 
   - Melakukan ekstensi `base.html` pada setiap html template yang dibuat
2. **Buat Form** 
   - Mendefinisikan `forms.py` dengan `ModelForm`
   - Mengisi fields yang sesuai dengan model yang dibuat kemarin `["name", "description", "price", "category", "thumbnail", "stock", "is_featured"]`
3. **Buat View untuk Form** 
   - `views.py`, gunakan `form.is_valid()` lalu `form.save()`.
   - `views.py`, membuat beberapa fungsi yang mirip dengan tutorial namun dengan menyesuaikan dan menambahkan class `product` serta `product form`
   -  Mendefinisikan `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` dengan `serializers.serialize` dengan access data sesuai pada class `product`
4. **Mambahkan CSRF Token** 
   - gunakan `{% csrf_token %}` di template `create_product.html` serta set `POST` untuk menambahkan product
5. **Atur URL Routing** → daftarkan semua fungsi views atau endpoint pada `urls.py`.
6. **Testing Lokal**
   - `python manage.py runserver` buka `http://127.0.0.1:8000/`
7. **Deployment ke PWS**
   - Commit ke Git: `git add .` dan `git commit -m "Initial commit"`
   - Push ke remote PWS: `git push pws master`

---

## Feedback untuk Asisten Dosen Tutorial 2

- Penjelasan jelas dan mudah digunakan.
- Kode sangat jelas dan membantu.

---

## Screenshot akses url pada Postman

1. **XML**
![alt text](image-1.png)
2. **JSON**
![alt text](image.png)
3. **XML Dengan Product ID**
![alt text](image-3.png)
4. **JSON Dengan Product ID**
![alt text](image-2.png)

