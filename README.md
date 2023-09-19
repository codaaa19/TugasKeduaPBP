
# Cara Membuat Proyek Django
Membuat file `requirements.txt` yang akan diisi dengan hal-hal yang akan kita perlukan untuk didownload
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Setelah itu, kita coba download dengan menggunakan command :

1. `python -m venv venv` (untuk membuat virtual environment)

2. `env\Scripts\activate` (aktivasi virtual environment)

3. `pip install -r requirements.txt` (download isi dari requirements.txt)

Last step pada pembuatan proyek django adalah melakukan perintah `django-admin createproject <nama project kalian>`.

Perlu diperhatikan pula bahwa dalam direktori yang dibuat, akan terdapat file **manage.py** yang akan berfungsi sebagai pengatur code yang akan kita buat nanti.

Untuk memastikan berhasil/tidaknya step ini, kita dapat melakukan command `python manage.py runserver` dan kalian bisa klik `http://localhost:8000`

Jika terdapat gambar roket dan tulisan succesful, maka proyek django kalian **SUKSES DIJALANKAN**😁

# Cara Membuat dan Menjalankan Aplikasi
Tambahkan `*` pada `ALLOWED HOST` pada `settings.py` untuk mengizinkan akses untuk semua host agar memudahkan keperluan-keperluan.
```py
ALLOWED_HOSTS = ["*"]
```

Step pertama dalam pembuatan aplikasi yaitu menggunakan command `python manage.py createapp <nama app kalian>`.

Setelah itu, jangan lupa mendaftarkan aplikasi kalian dalam `settings.py` sehingga akan menjadi seperti :

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<nama app kalian>'
]
```
Untuk menjalankan aplikasi, diperlukan proses **ROUTING** terlebih dahulu melalui `urls.py` dalam folder main kalian menggunakan command : 

```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

```

Function `show_main` pada code di atas bertujuan untuk mengakses modul `main.views` untuk menampilkan aplikasi kalian. 


Setelah itu, diperlukan proses **ROUTING** melalui `urls.py` dalam folder proyek untuk memetakan function  :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<nama app kalian>', include('main.urls'))
]

```

Setelah ini, kalian akan dapat melihat tampilan aplikasi yang kalian buat dengan mengakses link `https://localhost:8000`.

# Melakukan Deployment Adaptable

Siapkan repository github kalian dan pastikan bersifat **PUBLIC**. Berlanjut ke Adaptable, kalian dapat klik `deploy a new app`  dan pilih repository github yang akan kalian deploy.

Setelah itu, kalian pilih `Python App Template`. Jika sudah masuk ke halaman database, kalian dapat memilih opsi `PostgreSQL`. Selanjutnya, kalian dapat cek versi dari python kalian menggunakan code dan masukan ke bagan `version`

```
python --version
```

Untuk mengisi bagan `command` , kalian dapat isi dengan `python manage.py migrate && gunicorn <nama proyek kalian>.wsgi`

# Bagan Request Client Web Django

![Foto Korelasi Django](hubunganDjango.png)

Tahap - tahapnya :
1. Client akan melakukan **REQUEST** kepada django melalui pengisian url pada laman browser dan akan diterima oleh `urls.py` untuk dicocokan.

2. Jika `urls.py` menerima kecocokan, maka `urls.py` akan memanggil `views.py`.

3. Pada `views.py`, akan melakukan operasi database dan akan dipetakan pada `models.py`.

4. Pada `models.py`, akan dilakukan representasi dari `views.py` dan data-data yang direpresentasikan masih dapat diubah.

5. Setelah semua step-step sebelumnya berjalan, browser akan menerima respon website yang dapat client lihat.

# Why Virtual Environment ?!

Secara garis besar, penggunaan Virtual Environment didasari dari kemudahan dan efisiensi dalam melakukan proyek tertentu. Mengapa demikian? Berkat Virtual Environment, kita dapat mengerjakan beberapa proyek dengan depedensi tanpa konfilk.

Melalui hal tersebut, maka kita dapat mengelola depedensi yang diperlukan proyek secara terpisah dan menghindari adanya konflik yang akan terjadi.

**APAKAH TETAP BISA TANPA VIRTUAL ENVIRONMENT?**

Iya, bisa. Namun, mungkin lebih kompleks dan tidak akan mendapatkan kemudahan dari penjabaran sebelumnya.

## MVC? MVT? MVVM ?
1. MVC (Model View Controller) adalah sebuah design pattern yang memisahkan model, view, dan juga controller
- Model : Mengatur dan mengelola database
- View : Menampilkan GUI
- Controller : Menyambungkan model dan view

2. MVT (Model View Template) mirip dengan MVC hanya saja terdapat perbedaan dalam controller yang diimplementasikan langsung oleh framework. 
- Model : Mengatur dan mengelola database
- View : Tempat pemrosesan permintaan dan berfungsi sebagai logic utama
- Template : Tampilan

3. MVVM (Model View ViewModel) adalah sebuah design patterpembuatan GUI yang memisahkan fokus antara tampilan aplikasi dan juga logic program.
- Model : Mengelola database dan logic aplikasi setelah menerima input dari view
- View : Representasikan UI
- ViewModel : Penghubung model dan juga view

## Bonus
Melakukan testing proyek django dengan melakukan perintah `python manage.py test` dan memgasilkan output :

![Foto Testing Django](testingDjango.png)

## GET vs POST (DJANGO)

1. Tata cara pengiriman data
- `Get` data form URL
- `Post` data form HTTP dan bersifat sembunyi (tidak menggunakan URL)

2. Benefit
- `Get` dapat menggunakan bookmark karena based on URL
- `Post` tidak dapat menggunakan bookmark karena tidak based on URL

3. (opsional)

## Perbedaan XML, JSON, AND HTML

1. Function
- HTML membuat tampilan halaman web atau dapat dikatakan sebagai kerangka web
- JSON menyimpan dan mengirimkan data dengan format data yang mudah dimengerti
- XML menyimpan dan mengirimkan data dengan format data self-descriptive

2. Struktur
- HTML membuat tampilan halaman web(heading, picture, paragpraph, and much more)
- JSON menyimpan data dengan format key:value and nested
- XML menyimpan data dengan format tree structure (parent child relationship)
