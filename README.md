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

---

# Jawaban Pertanyaan Tugas 4

---

## Apa itu Django AuthenticationForm?

Library bawaan django yang digunakan untuk menangani proses login pengguna. Form tersebut menyediakan field username dan password, sekaligus melakukan validasi apakah kombinasi username/password masukan sesuai dengan data user yang terdaftar di database Django (user model).

**Kelebihan**:

* Terintegrasi otomatis dengan sistem autentikasi django
* Validasi dapat dilakukan otomastis
* Mudah dalam extend field tambahan

**Kekuranagan**:

* Kurang fleksibel jika ingin membangun sistem login khusus
* Tidak dilengkapi sistem autentikasi berbasis email
* Form bawaan yang sederhana

---

## Perbedaan antara Autentikasi dan Otorisasi

**Autentikasi** merupakan tahapan proses memastikan pengguna baik menggunakan password dan username, implementasi di dalam Django cukup sederhana dengan melakukan import `django.contrib.auth` yang menangani login/logout, password hashing, AuthenticationForm, middleware untuk request.user.

**Otorisasi** merupakan tahapan proses menentukan hak akses pengguna terhadap resource tertentu dalam konteks ini, dalam melihat news atau product yang perlu memerlukan role tertentu. implementasi di dalam django dapat dilakukan dengan menambahkan decorator tertentu seperti `@login_required` atau `@permission_required`.

---

## Kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web

- **session** memeiliki kelebihan yakni data tidak disimpan langsung di browser dan mendukung tipe data yang kompleks. Namun, kekurangan dari session ini memerlukan storage server-side dan lebih banyak resource di server

- **cookies** memiliki kelebihan untuk menyimpan data ylang dapat disimpan browser dalam kasus ini `last_login` yang digunakan untuk melacak aktivitas user terakhir seperti apa. Namun, kekurangan dari cookies ini sangat rentan untuk dicuri dan diubah oleh hacker.

---

## Penggunaan cookies aman secara default?

Cookies tidak sepenuhnya aman karena bisa dicuri atau dimodifikasi jika tidak diatur dengan benar, misalnya tanpa HttpOnly, Secure, atau SameSite. Django mengatasinya dengan proteksi default seperti `SESSION_COOKIE_HTTPONLY`, opsi `SESSION_COOKIE_SECURE` untuk production, token CSRF otomatis, serta dukungan `SESSION_ENGINE` agar session disimpan aman di server.

---

## Implementasi Checklist (Step-by-Step)

1. **Buat Autentikasi**
   - Melakukan konfigurasi autentikasi dengan mengaktifkan `django.contrib.auth` dan `django.contrib.sessions`.
   - Setup `urls.py` untuk menambahkan route login/logout serta menambahkan beberapa fungsi pendukung login/logout pada `views.py`.
   - Menggunakan `AuthenticationForm` didalam view login.
2. **Meritriksi Halaman News dan Main**
   - Menggunakan decorator autentikasi
   - Memasukkan `@login_required(login_url='/login')` diatas fungsi `show_main` dan `show_product`
3. **Menghubungkan Model Product dengan User**
   - Melakukan import model user.
   - Menambahkan `models.ForeignKey`
   - Melakukan set up fungsi pada `create_product` dengan menambahkan `request.user` di dalam product entry dengan tujuan menghubungkan objek produk dengan penggunanya.
4. **Menampilkan `last_login` dengan Menerapkan Cookies**
   - Menambahkan `from django.http import HttpResponseRedirect` dan `from django.urls import reverse` pada `views.py`.
   - Ubah bagian kode di fungsi login_user untuk menyimpan cookie baru bernama `last_login` yang berisikan timestamp pengguna saat melakukan login terakhir kali. 
   - Pada `show_main` bagian context tambahkan `'last_login': request.COOKIES.get('last_login', 'Never')`.
   - Pada `logout_user` tambahkan ` response = HttpResponseRedirect(reverse('main:login'))` dan `response.delete_cookie('last_login')`.
   - Tambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada dokumen `templates/main.html`

---

# Jawaban Pertanyaan Tugas 5

---

## Urutan prioritas CSS selector
CSS selector merupakan metode filterisasi dan memanggil objek elemen html tertentu untuk dilakukan `styling` menggunakan css atribute. Dalam melakukan filterisasi terdapat beberapa prioritas khusus yakni:
1. Inline style `style="color: red;"`
2. ID selector `#special { color: orange; }`
3. Class selector `.highlight { color: green; }`
4. Element selector `p { color: blue; }`
5. `!important` akan mengalahkan semuanya (jika elemen yang dipanggil tidak ada konflik).

---

## Mengapa `responsive design` penting dalam pengembangan aplikasi web beserta contoh
Responsive design bertujuan untuk memastikan web terlihat baik di semua perangkat (dekstop,mobile,tablet) agar UI/UX tetap konsisten tanpa mengubah konten melainkan hanya memperbaiki tata letak dan penataan di berbagai device. Sebagian web aplikasi di internet sudah menerapkan prinsip responsive design dengan memanfaatkan berbagai framework dan library css modern seperti; wikipedia, github, dan web app lainnya. Selain itu, ada beberapa yang belum menerapkan responsive design yakni wordpress, craiglist, dan web situs yang tergolong lama (sudah jarang update UI/UX).

---

## Perbedaan margin, border, padding dan cara implementasinya
1. Margin : ruang luar antara border elemen dengan elemen lain
2. Border : garis tepi antara padding dan margin
3. Padding : ruang internal antara konten dan border (bagian dalam kotak)
### implementasi :
```
.selector {
   padding : 30px;
   margin : 10px;
   border : 2px solid #000;
}
```
---

## Konsep `flexbox` dan `grid layout` beserta kegunaannya
`flexbox` : merupakan mode satu dimensi untuk mendistribusikan ruang antar item dan alignment (vertical centering, spacing otomatis, wrapping). Kegunaan untuk menyusun komponen baris/kolom: navbar, tombol bar, card row, item yang harus fleksibel.
`grid` : merupakan model dua dimensi untuk mendistribusikan layout halaman (master regions, hero + sidebar + content) dan mampu menyusun kontrol baris/kolom eksplisit. Kegunaan untuk grid gallery, layout kompleks.

---

## Implementasi Checklist (Step-by-Step)

1. **Menambahkan Tailwind ke Aplikasi**
   - Menambahkan link cdn tailwind ke dalam `base.html`.
2. **Menambahkan Fitur Edit Product**
   - Menambahkan fungsi `edit_product` dan menambahkan beberapa pemanggilan model yang dibuat.
   - Menambahkan `urls` pada `urls.py`.
   - Menambahkan `templates.html` pada `templates` dan menyesuaikan beberapa model yang dibuat.
3. ***Menambahkan Fitur Delete Product**
   - Menambahkan fungsi `delete_product` dan menambahkan beberapa pemanggilan model yang dibuat.
   - Menambahkan `urls` pada `urls.py`.
   - Menambahkan `templates.html` pada `templates` dan menyesuaikan beberapa model yang dibuat.
4. **Menambahkan Navigation Bar pada Aplikasi**
   - Melakukan penambahan deteksi kategori by `badges` di dalam fungsi `show_main`.
   - Menambahkan `navbar.html` pada bagian main/templates.
   - Melakukan penaambahan beberapa atribut tombol filterisasi by category pada `navbar.html`.
5. **Menambahkan Static Files pada Aplikasi**
   - Menambahkan `middleware Whitenose` ke dalam settings.py.
   - Menambahkan  `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` ke dalam settings.py.
6. **Styling Aplikasi**
   - Menambahkan `global.css` ke dalam static files
   - Menghubungkan `global.css` ke dalam `base.html`
   - Melakukan perubahan styling pada sisi tata letak dan warna pada `main.html`, `login.html`, dan `register.html`

---
