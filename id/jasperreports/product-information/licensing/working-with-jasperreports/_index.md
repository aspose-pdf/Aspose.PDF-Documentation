---

title: Bekerja dengan JasperReports

type: docs

weight: 10

url: id/jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Aspose.Words untuk JasperReports tersedia secara gratis, evaluasi waktu tak terbatas dari halaman unduhan. Versi evaluasi dan berlisensi dari produk adalah unduhan yang sama.



Ketika Anda puas dengan versi evaluasi, [beli lisensi](http://www.aspose.com/purchase/default.aspx). Pastikan Anda memahami dan menyetujui syarat lisensi.



{{% /alert %}}



Lisensi tersedia untuk diunduh dari halaman pesanan setelah pesanan dibayar. Lisensi adalah file XML yang ditandatangani secara digital dan teks jelas. Lisensi berisi informasi seperti nama klien, produk yang dibeli, dan jenis lisensi. Jangan mengubah isi file lisensi: itu akan membatalkan lisensi.



Ada beberapa cara untuk mengaktifkan lisensi:



- [Panggil setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).


- [Setel parameter eksportir dalam kode](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [Setel parameter exporter di **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).



Dua yang pertama digunakan dengan JasperReports, yang terakhir dengan JasperServer.

#### **Panggil setLicense**

<ins> **Metode ini digunakan dengan JasperReports.**



1. Unduh lisensi ke komputer Anda dan salin ke folder yang sesuai (misalnya folder aplikasi Anda atau JasperReports\lib).

2. Tambahkan kode berikut ke proyek Anda:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // buat objek stream yang berisi file lisensi

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // Setel lisensi melalui objek stream

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **Setel Parameter Exporter licenseFile dalam Kode**



<ins> **Metode ini digunakan dengan JasperReports.**



1. Download lisensi ke komputer Anda dan salin ke folder yang sesuai (misalnya folder aplikasi Anda atau JasperReports\lib).

2. Tambahkan kode berikut ke proyek Anda:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();
```