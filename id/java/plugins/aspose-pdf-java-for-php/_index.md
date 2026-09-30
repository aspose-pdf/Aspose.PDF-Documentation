---
title: Aspose.PDF Java untuk PHP
linktitle: Aspose.PDF Java untuk PHP
type: docs
weight: 50
url: /id/java/aspose-pdf-java-for-php/
description: Pelajari cara mengintegrasikan Aspose.PDF for Java ke dalam proyek PHP. Buka fungsionalitas PDF lanjutan untuk aplikasi web Anda.
lastmod: "2026-09-30"
---
## Pendahuluan untuk Aspose.PDF Java untuk PHP

### PHP / Java Bridge

PHP/Java Bridge adalah implementasi dari streaming, berbasis XML [protokol jaringan](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), yang dapat digunakan untuk menghubungkan mesin skrip native, misalnya PHP, Scheme atau Python, dengan mesin virtual Java. Itu hingga 50 kali lebih cepat daripada RPC lokal via SOAP, memerlukan sumber daya lebih sedikit di sisi server web. Itu [lebih cepat](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) dan lebih andal daripada komunikasi langsung melalui Java Native Interface, dan tidak memerlukan komponen tambahan untuk memanggil prosedur Java dari PHP atau prosedur PHP dari Java.

Baca selengkapnya di [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF for Java

Aspose.PDF for Java adalah komponen pembuatan dokumen PDF yang memungkinkan aplikasi Java Anda untuk membaca, menulis, dan memanipulasi dokumen PDF tanpa menggunakan Adobe Acrobat.

Aspose.PDF for Java adalah komponen dengan harga terjangkau yang menawarkan sejumlah besar fitur luar biasa, antara lain: opsi kompresi PDF, pembuatan dan manipulasi tabel, dukungan grafik, fungsi gambar, fungsionalitas hyperlink yang ekstensif, kontrol keamanan yang diperluas, dan penanganan Font khusus.

Aspose.PDF for Java memungkinkan Anda membuat file PDF secara langsung melalui API dan templat XML yang disediakan. Menggunakan Aspose.PDF for Java juga akan memungkinkan Anda menambahkan kemampuan PDF ke aplikasi Anda dalam waktu singkat.

### Aspose.PDF Java untuk PHP

Proyek Aspose.PDF for PHP menunjukkan bagaimana berbagai tugas dapat dilakukan menggunakan Aspose.PDF Java APIs dalam PHP. Proyek ini bertujuan untuk menyediakan contoh yang berguna bagi Pengembang PHP yang ingin memanfaatkan Aspose.PDF for Java dalam Proyek PHP mereka menggunakan [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Persyaratan sistem dan platform yang didukung

### Persyaratan sistem

Berikut adalah persyaratan sistem untuk menggunakan Aspose.PDF for PHP via Java:

- Server Tomcat 8.0 atau lebih tinggi terpasang.
- PHP/JavaBridge telah dikonfigurasi.
- FastCGI terpasang.
- Komponen Aspose.PDF yang diunduh.

### Platform yang didukung

Berikut adalah platform yang didukung:

- PHP 5.3 atau lebih tinggi
- Java 1.8 atau lebih tinggi

## Unduhan dan konfigurasi

### Mengunduh pustaka yang diperlukan

Unduh pustaka yang dibutuhkan seperti yang disebutkan di bawah ini. Ini diperlukan untuk mengeksekusi contoh Aspose.PDF Java untuk PHP.

- **Aspose:** [Aspose.PDF for Java Komponen](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Mengunduh contoh dari situs koding sosial

Rilis berikut dari contoh yang berjalan tersedia untuk diunduh di situs koding sosial yang disebutkan di bawah:

### GitHub

- Contoh Aspose.PDF Java untuk PHP
  - [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Mengonfigurasi kode sumber di platform Linux

Silakan ikuti langkah-langkah sederhana ini untuk membuka dan memperluas kode sumber saat menggunakan:

### 1. Instal Tomcat server

Untuk menginstal tomcat server, jalankan perintah berikut pada konsol linux. Ini akan berhasil menginstal tomcat server.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. unduh dan konfigurasikan PHP/JavaBridge

Untuk mengunduh binary PHP/JavaBridge, jalankan perintah berikut di konsol linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Ekstrak file biner PHP/JavaBridge dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Ini akan mengekstrak **JavaBridge.war** file. Salin ke folder tomcat88 **webapps** dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Dengan menyalin, tomcat8 akan secara otomatis membuat folder baru "**JavaBridge**" di **webapps**.

Jika ada pesan kesalahan yang muncul maka instal  **FastCGI** dengan menjalankan perintah berikut pada console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Jika **JAVA_HOME** error ditampilkan, maka buka file /etc/default/tomcat8 dan hapus komentar pada baris yang mengatur JAVA_HOME.

### 3. konfigurasikan contoh Aspose.PDF Java untuk PHP

Clone, contoh PHP dengan menjalankan perintah berikut di dalam folder webapps/JavaBridge.В

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Mengonfigurasi kode sumber pada platform Windows

Silakan ikuti langkah sederhana di bawah ini untuk mengonfigurasi PHP/Java Bridge pada Platform Windows

1. Instal PHP5 dan konfigurasikan seperti biasanya.
2. Instal JRE 6 (Java Runtime Environment) jika Anda belum memilikinya. Anda dapat memeriksanya di C:\Program Files dll. Anda dapat mengunduhnya di sini. Saya menggunakan JRE 6 karena kompatibel dengan PHP Java Bridge (PJB).

3. Instal Apache Tomcat 8.0. Anda dapat mengunduhnya di sini.

4. Unduh [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Salin file ini ke direktori webapps tomcat.
(contoh: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Mulai ulang layanan Tomcat Apache.

6. Pergi ke http://localhost:8080/JavaBridge/test.php untuk memeriksa apakah php berfungsi. Anda dapat menemukan contoh lain di sana.

7. Salin [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) file jar ke C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

8. Klon [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) contoh di dalam C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ folder.

9. Salin folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java ke folder contoh Aspose.PDF Java untuk PHP Anda.

10. Mulai ulang layanan apache tomcat dan mulai menggunakan contoh.

## Dukungan, pengembangan, dan kontribusi

### Dukungan

Sejak hari-hari pertama Aspose, kami tahu bahwa hanya memberi pelanggan kami produk yang bagus tidak akan cukup. Kami juga perlu memberikan layanan yang baik. Kami sendiri adalah pengembang dan memahami betapa menjengkelkannya ketika masalah teknis atau keanehan dalam perangkat lunak menghentikan Anda dari melakukan apa yang perlu Anda lakukan. Kami di sini untuk menyelesaikan masalah, bukan menciptakannya.

Inilah mengapa kami menawarkan dukungan gratis. Siapa pun yang menggunakan produk kami, baik mereka telah membelinya atau sedang menggunakan versi evaluasi, layak mendapatkan perhatian dan rasa hormat penuh kami.

Anda dapat melaporkan masalah atau saran apa pun yang terkait denganВ Aspose.Cells Java for PHP menggunakan salah satu platform berikut:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Memperluas dan berkontribusi

Aspose.PDF Java for PHP bersifat sumber terbuka dan kode sumbernya tersedia di situs web coding sosial utama yang tercantum di bawah ini. Pengembang didorong untuk mengunduh kode sumber dan berkontribusi dengan menyarankan atau menambahkan fitur baru atau meningkatkan yang sudah ada, sehingga orang lain juga dapat mendapat manfaat darinya.

### Kode sumber

Anda dapat mengambil kode sumber terbaru dari salah satu lokasi berikut

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
