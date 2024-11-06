---
title: Unduh dan Konfigurasi Aspose.PDF di PHP
type: docs
weight: 10
url: id/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## Unduh Pustaka yang Diperlukan

Unduh pustaka yang diperlukan yang disebutkan di bawah ini. Ini adalah yang diperlukan untuk menjalankan contoh Aspose.PDF Java untuk PHP.

- **Aspose:** [Komponen Aspose.PDF untuk Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Unduh Contoh dari Situs Koding Sosial

Rilis contoh yang berjalan berikut tersedia untuk diunduh di situs koding sosial yang disebutkan di bawah ini:

### GitHub

- **Contoh Aspose.PDF Java untuk PHP**
  - [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Cara mengkonfigurasi kode sumber di Platform Linux

Silakan ikuti langkah-langkah sederhana ini untuk membuka dan memperluas kode sumber saat menggunakan:

## 1. Instal Server Tomcat

Untuk menginstal server Tomcat, jalankan perintah berikut di konsol Linux. Ini akan berhasil menginstal server Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Unduh dan Konfigurasi PHP/JavaBridge

Untuk mengunduh biner PHP/JavaBridge, jalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Unzip biner PHP/JavaBridge dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Ini akan mengekstrak file **JavaBridge.war**. Salin ke folder **webapps** tomcat8 dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


Dengan menyalin, tomcat8 akan secara otomatis membuat folder baru "**JavaBridge**" di **webapps**.
 Setelah folder dibuat, pastikan tomcat8 Anda berjalan dan kemudian periksa http://localhost:8080/JavaBridge di browser, itu harus membuka halaman default JavaBridge.

Jika ada pesan kesalahan muncul, maka instal **FastCGI** dengan menjalankan perintah berikut di konsol Linux.

{{< highlight actionscript3 >}}

sudo apt-get install php55-cgi

{{< /highlight >}}

Setelah menginstal php5.5 CGI, restart server tomcat8 dan periksa http://localhost:8080/JavaBridge lagi di browser.

Jika muncul kesalahan **JAVA_HOME**, maka buka file /etc/default/tomcat8 dan hilangkan komentar pada baris yang mengatur JAVA_HOME. Periksa http://localhost:8080/JavaBridge di browser lagi, itu harus membuka halaman Contoh PHP/JavaBridge.

## 3. Konfigurasi Aspose.PDF Java untuk Contoh PHP

Kloning, contoh PHP dengan menjalankan perintah berikut di dalam folder webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Cara mengkonfigurasi kode sumber di Windows

Silakan ikuti langkah-langkah sederhana di bawah ini untuk mengkonfigurasi PHP/Java Bridge pada Platform Windows

1. Instal PHP5 dan konfigurasikan seperti biasanya
2. Instal JRE 6 (Java Runtime Environment) jika Anda belum memilikinya. Anda dapat memeriksanya di C:\Program Files dll. Anda dapat mengunduhnya di sini. Saya menggunakan JRE 6 karena kompatibel dengan PHP Java Bridge (PJB).

3. Instal Apache Tomcat 8.0. Anda dapat mengunduhnya di sini

4. Unduh JavaBridge.war.
5. Salin file ini ke direktori tomcat webapps.
(contoh: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Restart layanan apache tomcat.

7. Buka http://localhost:8080/JavaBridge/test.php untuk memeriksa apakah php berfungsi. Anda dapat menemukan contoh lain di sana

8. Salin file jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) Anda ke C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Klon [Aspose.PDF Java untuk PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) contoh ke dalam folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Salin folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java ke folder contoh Aspose.PDF Java untuk PHP Anda.

11. Mulai ulang layanan apache tomcat dan mulai gunakan contoh.