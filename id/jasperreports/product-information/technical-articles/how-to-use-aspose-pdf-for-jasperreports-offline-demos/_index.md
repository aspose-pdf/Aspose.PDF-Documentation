---
title: Cara - menggunakan demo offline Aspose.Pdf untuk JasperReports
type: docs
weight: 10
url: id/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF untuk JasperReports mencakup sejumlah proyek demo untuk membantu Anda memulai mengekspor laporan ke format PDF dari aplikasi Anda. Demo tersebut adalah demo standar JasperReports yang telah dimodifikasi untuk menunjukkan cara menggunakan eksportir baru.

{{% /alert %}}
### **Menjalankan Demo Aspose.PDF untuk JasperReports**
Untuk menjalankan demo Aspose.PDF untuk JasperReports:

{{% alert color="primary" %}}

1. Unduh JasperReports dari <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Pastikan untuk mengunduh seluruh proyek yang diarsipkan dengan kode sumber dan demo, bukan hanya satu JAR.
2. Buka arsip proyek ke suatu lokasi di hard disk Anda, misalnya C:\.
3. ```
Salin semua folder demo dari folder \demo di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\demo\samples, di mana ```<InstallDir>``` adalah lokasi di mana Anda telah mengekstrak JasperReports. Langkah ini diperlukan karena skrip build demo bergantung pada struktur folder JasperReports, jika tidak, Anda harus memodifikasi skrip build.
4. Salin file **aspose.pdf.jasperreports.jar** dari folder \lib di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\lib.
5. Unduh alat ANT dari <http://ant.apache.org/bindownload.cgi>.
6. Ekstrak alat ANT dan atur variabel lingkungan seperti yang dijelaskan dalam manual alat tersebut.
7. Ubah direktori saat ini ke ```<InstallDir>```\demo\hsqldb dan jalankan perintah baris berikut:
   ant runServer
8. Buka instance command prompt baru dan ubah direktori saat ini ke salah satu demo Aspose.PDF untuk JasperReports, misalnya ```<InstallDir>```\demo\samples\charts.ap.
9. Jalankan perintah berikut pada baris perintah:
10.
``` ant javac – untuk mengompilasi file sumber Java dari aplikasi uji.  
11. ant compile – untuk mengompilasi desain laporan XML dan menghasilkan file .jasper  
12. ant fill – untuk mengisi desain laporan yang sudah dikompilasi dengan data dan menghasilkan file .jrprint  
13. Jalankan perintah berikut di baris perintah:  
    ant pdf – untuk menghasilkan file PDF dari laporan demo.  
14. Buka salah satu dokumen yang dihasilkan untuk melihat, misalnya ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf di Adobe Reader atau aplikasi lainnya.  

{{% /alert %}}