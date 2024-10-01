# Daniel Angger Dewandaru  
# 2306275973  
# PBP A  

## TUGAS 3  
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
-. Singkatnya kita memerlukan data delivery untuk mendukung performa serta pengalaman pengguna dalam menggunakan sebuah platform. Bila diperjelas, data delivery memungkinkan sebuah akses data real-time, yang banyak diperlukan oleh platform e-commerce. Lalu, data delivery juga memungkinkan untuk mengoptimisasi performa, karena memungkinkan pengguna untuk mengakses data secara cepat. Dan yang paling penting, pengenkripsian data sebelum dikirim menjamin keamanan data dari pihak tidak berwenang.  

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
-. Berdasarkan penggunaannya dalam banyak aplikasi modern, JSON dianggap lebih baik daripada XML, walaupun dari banyak kasus hal itu bergantung pada konteks penggunaannya. Ada beberapa alasan mengapa JSON lebih populer daripada XML. Pertama, JSON menggunakan struktur array yang lebih sederhana tanpa tag penutup, sehingga lebih ringkas dan kecil dalam ukuran, sehingga bila dikirim lebih cepat prosesnya. Kedua, JSON lebih mudah dibaca manusia dan ditulis komputer karena formatnya menyerupai bahasa pemrograman. Terakhir, JSON lebih aman karena tidak mendukung eksekusi skrip bawaan seperti XML, sehingga tidak mudah terkena XML External Entity atau XML Bombs.  

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?  
-. Dalam Django, is_valid() adalah bagian dari Model atau ModelForm yang digunakan untuk memeriksa apakah data yang dikirim melalui form sudah sesuai dengan validasi yang ditentukan. Bila sudah valid, maka selanjutnya data tersebut bisa dikirim ke database atau backend untuk diproses sesuai kebutuhan. Cara kerjanya adalah saat pengguna mengirim input pada form dan disubmit, maka data tersebut perlu divalidasi apakah sudah sesuai kriteria atau belum, nah disitulah method is_valid() berguna.  

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  
-. CSRF (Cross-Site Request Forgery) adalah sejenis serangan yang mencoba mengirim permintaan tidak sah atas nama pengguna yang sudah terautentifikasi. Nah, penambahan csrf_token mampu mencegah hal ini. Bila kita tidak menambahkan crsf_token, maka hal itu bisa membuat form yang kita buat menjadi rentan terhadap serangan CSRF, hal ini bisa terjadi karena penyerang memanfaatkan celah tersebut dengan membuat form berbahaya, yang ketika pengguna terautentifikasi mengaksesnya, form tersebut langsung mengirim pada server sasaran dengan kredensial pengguna yang terautentifikasi. Dan hal ini bisa menyebabkan penyerang melakukan sebuah aksi tanpa persetujuan.  

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
-. Pertama, pastikan Django sudah terinstal. Kedua, buatlah proyek Django yang akan diimplementasikan. Ketiga, konfigurasikan settings.py sesuai proyek kita. Keempat, buatlah form pada proyek DJango. Kelima, tambahkan csrf_token pada form tersebut. Keenam, tangani permintaan di views dengan method is_valid(). Ketujuh, tambahkan url untuk views.py. Kedelapan, tambahkan url aplikasi untuk proyek. Kesembilan, ujicoba melalui localhost. Kesepuluh, perketat keamanan dalam settings.py.  

![Alt text](<Screenshot 2024-09-16 at 21.21.31.png>) ![Alt text](<Screenshot 2024-09-16 at 21.20.46.png>) ![Alt text](<Screenshot 2024-09-16 at 21.19.31.png>) ![Alt text](<Screenshot 2024-09-16 at 21.19.03.png>)


## Tugas 4  
Apa perbedaan antara HttpResponseRedirect() dan redirect()  
-. Perbedaan antara HttpResponseRedirect() dan redirect() adalah HttpResponseRedirect() bersifat lebih eksplisit, karena harus selalu memberikan URL yang diperlukan, sementara redirect() bersifat lebih fleksibel, karena bisa menggunakan nama view dan objek model, sehingga menurut data, redirect() lebih sering digunakan.  

Jelaskan cara kerja penghubungan model Product dengan User!  
-. Untuk menghubungkan Product dan User, kita bisa menghubungkannya dengan ForeignKeys. ForeignKeys memungkinkan kita untuk menghubungkan satu atau banyak model Product dengan satu User melalui sebuah hubungan. Hubungan ini diperlukan untuk aplikasi-aplikasi seperti toko online, postingan blog, dll.  

Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.  
-. Kalau dari definisi, autentication berfungsi untuk memverifikasi identitas pengguna, sedangkan authorization berfungsi untuk memverifikasi hak akses pengguna. Autentication biasanya mengecek kredensial, misalnya username dan password, sedangkan authorization biasanya mengecek izin akses pengguna. Saat pengguna login, yang terjadi adalah penggabungan dari autentication dan authorization, yaitu sistem akan meminta dan memverifikasi kredensial pengguna, misalnya username dan password. Setelah kredensial terverifikasi, pengguna akan berhasil login. Setelah login, sistem akan menentukan izin akses pengguna, dan memberikan semua resource yang bisa diakses menurut izin aksesnya. Contoh pengimplementasian pada Django adalah melalui method autenticate() dan @permission_required.  

Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?  
-. Django bisa mengingat pengguna yang telah login dengan menggunakan cookies. Saat pengguna login, Django akan membuat session dan menyimpannya di sebuah database dan mengaitkannya dengan sebuah cookie pada browser pengguna. Kegunaan lain cookies adalah menyimpan preferensi pengguna, menerapkan CSRF, dan melakukan pelacakan perilaku. Tidak semua cookies aman digunakan, apalagi bila tidak memperhatikan praktik terbaik keamanan.  

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?  
-. Pertama, buatlah form registrasi serta login bagi pengguna. Registrasi berfungsi bagi pengguna yang belum memiliki akun dan login berfungsi bagi pengguna yang sudah memiliki akun. Kedua, konfigurasikanlah fungsi login pada projek yang akan digunakan. Ketiga, buatlah juga fungsi logout, yang bisa digunakan pengguna untuk berganti akun. Saat mengimplementasikan fungsi login dan logout, jangan lupa mengimplementasikan fungsi "last login", yang berguna untuk melacak aktivitas akun dan memverifikasinya dengan aktivitas pengguna pada akun tersebut. Keempat, restriksilah halaman main, yang hanya bisa diakses saat pengguna berhasil login. Autentifikasikan juga halaman main dengan data dari cookie pengguna dengan menggabungkan model Product dan User menggunakan ForeignKeys.  

## Tugas 5
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
-. Pertama-tama, urutan pengambilan selector biasa disebut sebagai specificity dan cascade dalam CSS. Prioritasnya adalah yang pertama inline style, yang merujuk pada gaya yang didefinisikan langsung pada HTML. Yang kedua adalah ID, yaitu ditandai dengan tanda pagar (#) sebelum didefiniskan, misalnya #id. Yang ketiga adalah Classes, Attributes, dan Pseudo-classes, Classes merujuk pada gaya yang ditandai dengan titik (.class), Attributes merujuk pada gaya yang ditandai ([]) contohnya [attributes], dan Pseudo-classes merujuk pada gaya yang ditandai dengan (:) misalnya :hover. Lalu, yang keempat adalah tag HTML, seperti div, h1, dan lain-lain. Dan yang terakhir adalah universal selector, ditandai dengan (*).