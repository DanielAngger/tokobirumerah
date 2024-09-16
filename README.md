Daniel Angger Dewandaru
2306275973
PBP A

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