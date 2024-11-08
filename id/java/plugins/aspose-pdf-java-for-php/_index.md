---
title: Aspose.PDF Java untuk PHP
type: docs
weight: 50
url: /id/java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Pengenalan ke Aspose.PDF Java untuk PHP

### Jembatan PHP / Java

Jembatan PHP/Java adalah implementasi dari streaming, protokol jaringan berbasis XML [network protocol](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), yang dapat digunakan untuk menghubungkan mesin skrip asli, misalnya PHP, Scheme atau Python, dengan mesin virtual Java. Ini hingga 50 kali lebih cepat daripada RPC lokal melalui SOAP, memerlukan lebih sedikit sumber daya di sisi server web. Ini lebih [cepat](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) dan lebih andal daripada komunikasi langsung melalui Java Native Interface, dan tidak memerlukan komponen tambahan untuk memanggil prosedur Java dari PHP atau prosedur PHP dari Java.

Baca lebih lanjut di [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF untuk Java

Aspose.PDF untuk Java adalah komponen pembuatan dokumen PDF yang memungkinkan aplikasi Java Anda untuk membaca, menulis dan memanipulasi dokumen PDF tanpa menggunakan Adobe Acrobat.

Aspose.PDF for Java adalah komponen dengan harga terjangkau yang menawarkan kekayaan fitur yang luar biasa, termasuk: opsi kompresi PDF, pembuatan dan manipulasi tabel, dukungan grafik, fungsi gambar, fungsionalitas hyperlink yang luas, kontrol keamanan yang diperluas, dan penanganan font khusus.

Aspose.PDF for Java memungkinkan Anda untuk membuat file PDF secara langsung melalui API dan template XML yang disediakan. Menggunakan Aspose.PDF for Java juga akan memungkinkan Anda menambahkan kemampuan PDF ke aplikasi Anda dalam waktu singkat.

### Aspose.PDF Java untuk PHP

Proyek Aspose.PDF untuk PHP menunjukkan bagaimana berbagai tugas dapat dilakukan menggunakan Aspose.PDF Java API dalam PHP. Proyek ini bertujuan untuk menyediakan contoh yang berguna bagi Pengembang PHP yang ingin memanfaatkan Aspose.PDF untuk Java dalam Proyek PHP mereka menggunakan [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Persyaratan Sistem dan Platform yang Didukung

### Persyaratan Sistem

Berikut adalah persyaratan sistem untuk menggunakan Aspose.PDF untuk PHP melalui Java:

- Tomcat Server 8.0 atau di atasnya terpasang.
- PHP/JavaBridge dikonfigurasi.
- FastCGI terpasang.
- Komponen Aspose.PDF diunduh.

### Platform yang Didukung

Berikut adalah platform yang didukung:

- PHP 5.3 atau di atasnya
- Java 1.8 atau di atasnya

## Unduh dan Konfigurasi

### Unduh Perpustakaan yang Diperlukan

Unduh perpustakaan yang diperlukan yang disebutkan di bawah ini. Ini diperlukan untuk menjalankan contoh Aspose.PDF Java untuk PHP.

- **Aspose:** [Komponen Aspose.PDF untuk Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Unduh Contoh dari Situs Pengkodean Sosial

Rilis contoh yang berjalan berikut tersedia untuk diunduh di situs pengkodean sosial yang disebutkan di bawah ini:

### GitHub

- Aspose.PDF Java untuk Contoh PHP
  - [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Cara mengkonfigurasi kode sumber di Platform Linux

Silakan ikuti langkah-langkah sederhana ini untuk membuka dan memperluas kode sumber sambil menggunakan:

### 1. Instal Tomcat Server

Untuk menginstal server tomcat, jalankan perintah berikut di konsol linux. Ini akan berhasil menginstal server tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Unduh dan Konfigurasi PHP/JavaBridge

Untuk mengunduh biner PHP/JavaBridge, jalankan perintah berikut pada konsol linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Unzip biner PHP/JavaBridge dengan menjalankan perintah berikut pada konsol linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Ini akan mengekstrak file **JavaBridge.war**. Salin ke folder **webapps** tomcat8 dengan menjalankan perintah berikut pada konsol Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Dengan menyalin, tomcat8 akan secara otomatis membuat folder baru "**JavaBridge**" di **webapps**.

Jika ada pesan kesalahan muncul maka instal **FastCGI** dengan menjalankan perintah berikut pada konsol Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Jika error **JAVA_HOME** ditampilkan, buka file /etc/default/tomcat8 dan hapus komentar pada baris yang mengatur JAVA_HOME.

### 3. Konfigurasikan Aspose.PDF Java untuk Contoh PHP

Clone, contoh PHP dengan menjalankan perintah berikut di dalam folder webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Cara mengkonfigurasi kode sumber di Platform Windows

Silakan ikuti langkah-langkah sederhana di bawah ini untuk mengkonfigurasi PHP/Java Bridge di Platform Windows

1. Instal PHP5 dan konfigurasikan seperti biasanya
2. Instal JRE 6 (Java Runtime Environment) jika Anda belum memilikinya. Anda dapat memeriksanya di C:\Program Files dll. Anda dapat mengunduhnya di sini. Saya menggunakan JRE 6 karena kompatibel dengan PHP Java Bridge (PJB).

3. Instal Apache Tomcat 8.0. Anda dapat mengunduhnya di sini

4. Unduh [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Salin file ini ke direktori webapps tomcat. (contoh: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

5. Mulai ulang layanan apache tomcat.

6. Buka http://localhost:8080/JavaBridge/test.php untuk memeriksa apakah php berfungsi. Anda dapat menemukan contoh lain di sana

7. Salin file jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) Anda ke C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Klon contoh [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) di dalam folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Salin folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java ke folder contoh Aspose.PDF Java untuk PHP Anda.

10. Mulai ulang layanan apache tomcat dan mulai gunakan contoh-contohnya.


## Dukungan, Perluas dan Berkontribusi

### Dukungan

Sejak hari pertama Aspose, kami tahu bahwa hanya memberikan produk yang baik kepada pelanggan kami tidaklah cukup. Kami juga perlu memberikan layanan yang baik. Kami adalah pengembang sendiri dan memahami betapa frustrasinya ketika masalah teknis atau keanehan dalam perangkat lunak menghentikan Anda dari melakukan apa yang perlu Anda lakukan. Kami di sini untuk menyelesaikan masalah, bukan menciptakannya.

Inilah mengapa kami menawarkan dukungan gratis. Siapapun yang menggunakan produk kami, baik mereka membelinya atau menggunakan evaluasi, berhak mendapatkan perhatian dan penghormatan penuh dari kami.

Anda dapat melaporkan masalah atau saran terkait Aspose.Cells Java untuk PHP menggunakan salah satu platform berikut:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Perluas dan Berkontribusi

Aspose.PDF Java untuk PHP adalah sumber terbuka dan kode sumbernya tersedia di situs web pengkodean sosial utama yang tercantum di bawah ini.
 Pengembang didorong untuk mengunduh kode sumber dan berkontribusi dengan menyarankan atau menambahkan fitur baru atau meningkatkan yang sudah ada, sehingga orang lain juga dapat mengambil manfaat darinya.

### Kode Sumber

Anda dapat mendapatkan kode sumber terbaru dari salah satu lokasi berikut

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)