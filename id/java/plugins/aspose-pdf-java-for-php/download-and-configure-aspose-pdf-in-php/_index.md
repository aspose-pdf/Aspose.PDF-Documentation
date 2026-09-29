---
title: Unduh dan Konfigurasikan Aspose.PDF di PHP
linktitle: Unduh dan Konfigurasikan Aspose.PDF di PHP
type: docs
weight: 10
url: /id/java/download-and-configure-aspose-pdf-in-php/
description: Pelajari cara mengunduh dan mengonfigurasi Aspose.PDF di PHP untuk integrasi mudah dan manipulasi PDF dalam proyek PHP Anda.
lastmod: "2026-09-29"
---
## Unduh Perpustakaan yang Diperlukan

Unduh perpustakaan yang diperlukan yang disebutkan di bawah ini. Ini diperlukan untuk mengeksekusi contoh Aspose.PDF Java untuk PHP.

- **Aspose:** [Komponen Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Unduh Contoh dari Situs Koding Sosial

Rilis contoh yang dapat dijalankan berikut tersedia untuk diunduh di situs pengkodean sosial yang disebutkan di bawah ini:

### GitHub

- **Aspose.PDF Java for PHP Contoh**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Cara mengonfigurasi kode sumber di Platform Linux

Harap ikuti langkah-langkah sederhana iniВ untuk membuka dan memperluas kode sumber saat menggunakan:

## 1. Instal Server Tomcat

Untuk menginstal server Tomcat, jalankan perintah berikut pada konsol Linux.В Ini akan berhasil menginstal server Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Unduh dan Konfigurasikan PHP/JavaBridge

Untuk mengunduh binary PHP/JavaBridge, jalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Ekstrak binary PHP/JavaBridge dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Ini akan mengekstrakВ **JavaBridge.war**В file. Salin ke folder tomcat88В **webapps**В dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Dengan menyalin, tomcat8 secara otomatis akan membuat folder baru "**JavaBridge**" diВ **webapps**. Setelah folder dibuat, pastikan tomcat8 Anda berjalan dan kemudian periksaВ  http://localhost:8080/JavaBridge В di peramban, seharusnya membuka halaman default JavaBridge.

Jika muncul pesan error apa pun, maka instalВ  **FastCGI**В dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Setelah menginstal php5.5 CGI, restart server tomcat8 dan periksaВ  http://localhost:8080/JavaBridge В lagi di peramban.

Jika **JAVA_HOME** error ditampilkan, maka buka file /etc/default/tomcat8 dan hapus komentar pada baris yang menetapkan JAVA_HOME. Periksa http://localhost:8080/JavaBridge В di browser lagi, seharusnya muncul dengan halaman Contoh PHP/JavaBridge.

## 3. Konfigurasikan Contoh Aspose.PDF Java untuk PHP

Klon, contoh PHP dengan menjalankan perintah berikut di dalam folder webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Cara mengonfigurasi kode sumber di Windows

Silakan ikuti langkah-langkah sederhana di bawah ini untuk mengonfigurasi PHP/Java Bridge pada Platform Windows

1. Instal PHP5 dan konfigurasikan seperti biasa
2. Instal JRE 6 (Java Runtime Environment) jika Anda belum memilikinya. Anda dapat memeriksa ini di C:\Program Files dll. Anda dapat mengunduhnya di sini. Saya menggunakan JRE 6 karena kompatibel dengan PHP Java Bridge (PJB).

3. Instal Apache Tomcat 8.0. Anda dapat mengunduhnya di sini

4. Unduh JavaBridge.war.
5. Salin file ini ke direktori webapps tomcat.
(contoh: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Mulai ulang layanan Apache Tomcat.

7. Buka  http://localhost:8080/JavaBridge/test.php  untuk memeriksa apakah php berfungsi. Anda dapat menemukan contoh lain di sana

8. Salin milik Anda [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) file jar ke C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Klon [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) contoh di dalam folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ folder.

10. Salin folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java ke folder contoh Aspose.PDF Java for PHP Anda.

11. Mulai ulang layanan apache tomcat dan mulai menggunakan contoh.
