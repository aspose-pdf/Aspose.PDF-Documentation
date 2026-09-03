---
title: Cara - menggunakan Aspose.PDF untuk demo offline JasperReports
linktitle: How to - use Aspose.PDF for JasperReports offline demos
type: docs
weight: 10
url: /id/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Jelajahi demo offline untuk Aspose.PDF for JasperReports. Pelajari implementasi dan fitur praktis secara langsung.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports menyertakan sejumlah proyek demo untuk membantu Anda mulai mengekspor laporan ke format PDF dari aplikasi Anda. Demo tersebut merupakan demo standar JasperReports yang telah dimodifikasi untuk menunjukkan cara menggunakan eksportir baru.

{{% /alert %}}

## Running Aspose.PDF for JasperReports Demos

Untuk menjalankan demo Aspose.PDF for JasperReports:

{{% alert color="primary" %}}

1. Unduh JasperReports dari <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Pastikan untuk mengunduh seluruh arsip proyek dengan kode sumber dan demo, bukan hanya satu JAR.
2. Buka paket proyek yang diarsipkan ke beberapa lokasi di hard disk Anda, misalnya C:\.
3. Salin semua folder demo dari folder \demo di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` adalah lokasi tempat Anda membongkar JasperReports. Langkah ini diperlukan karena skrip build demo bergantung pada struktur folder JasperReports, jika tidak, Anda harus memodifikasi skrip build.
4. Salin file **aspose.pdf.jasperreports.jar** dari folder \lib di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\lib.
5. Unduh alat ANT dari <http://ant.apache.org/bindownload.cgi>.
6. Buka kemasan alat ANT dan atur variabel lingkungan seperti yang dijelaskan dalam manual alat.
7. Ubah direktori saat ini menjadi ```<InstallDir>```\demo\hsqldb dan jalankan baris perintah berikut:
   ant runServer
8. Buka instance command prompt baru dan ubah direktori saat ini ke salah satu demo Aspose.PDF for JasperReports, misalnya ```<InstallDir>```\demo\samples\charts.ap.
9. Jalankan perintah berikut pada baris perintah:
10. ant javac – untuk mengkompilasi file sumber Java dari aplikasi pengujian.
11. ant compile – to compile the XML report design and produce the .jasper file
12. ant fill – to fill the compiled report design with data and produce the .jrprint file
13. Jalankan perintah berikut pada baris perintah:
   ant pdf – to produce a PDF file from the demo report.
14. Buka salah satu dokumen yang dihasilkan untuk dilihat, misalnya ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf di Adobe Reader atau aplikasi lain.

{{% /alert %}}

