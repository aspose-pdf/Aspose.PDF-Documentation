---
title: Bekerja dengan JasperReports
linktitle: Bekerja dengan JasperReports
type: docs
weight: 10
url: /id/jasperreports/working-with-jasperreports/
description: Kuasai bekerja dengan JasperReports menggunakan Aspose.PDF. Buat dan ekspor laporan terperinci dalam format PDF dengan fitur-fitur canggih.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.Words untuk JasperReports tersedia gratis, evaluasi tanpa batas waktu dari halaman unduh. Evaluasi dan versi berlisensi produk adalah unduhan yang sama.

Jika Anda puas dengan versi evaluasinya, [membeli lisensi](https://purchase.aspose.com/buy?ppId=98899). Pastikan Anda memahami dan menyetujui persyaratan lisensi.

{{% /alert %}}

Lisensi tersedia untuk diunduh dari halaman pemesanan setelah pesanan dibayar. Lisensinya berupa file XML teks yang jelas dan ditandatangani secara digital. Lisensi berisi informasi seperti nama klien, produk yang dibeli, dan jenis lisensi. Jangan mengubah konten file lisensi: ini akan membatalkan lisensi.

Ada beberapa cara untuk mengaktifkan lisensi:

- [Hubungi setLicense](/pdf/id/jasperreports/working-with-jasperreports/#call-setlicense).
- [Tetapkan parameter eksportir dalam kode](/pdf/id/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Tetapkan parameter eksportir di **applicationContext.xml**](/pdf/id/jasperreports/working-with-jasperserver/).

Dua yang pertama digunakan dengan JasperReports, yang terakhir dengan JasperServer.

## Hubungi setLicense

Metode ini digunakan dengan JasperReports.

1. Unduh lisensi ke komputer Anda dan salin ke folder yang sesuai (misalnya folder aplikasi Anda atau JasperReports\lib).
2. Tambahkan kode berikut ke proyek Anda:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## Tetapkan Parameter Pengekspor LicenseFile dalam Kode

Metode ini digunakan dengan JasperReports.

1. Unduh lisensi ke komputer Anda dan salin ke folder yang sesuai (misalnya folder aplikasi Anda atau JasperReports\lib).
2. Tambahkan kode berikut ke proyek Anda:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


