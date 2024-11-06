title: Integrasi dengan JasperReports

type: docs

weight: 20

url: id/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Untuk menggunakan Aspose.PDF untuk JasperReports dalam aplikasi Anda, salin **aspose.pdf.jasperreports.jar** dari folder \lib dalam **Aspose.PDF.JasperReports.zip** ke direktori JasperReports\lib, atau ke folder perpustakaan aplikasi Anda. Setelah itu, Anda dapat mengakses eksportir secara programatis.

{{% /alert %}}

Contoh berikut menunjukkan kode tipikal yang dibutuhkan untuk mengekspor laporan ke format PDF menggunakan Aspose.PDF untuk JasperReports. Lebih banyak contoh dapat ditemukan dalam laporan demo yang disertakan dalam unduhan produk.

{{< highlight csharp >}}

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
```

   exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);





   File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");



   exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());





   exporter.exportReport();





{{< /highlight >}}



Cuplikan kode di atas telah diuji dengan JasperReports 3.5.2. Jika menggunakan JasperReports 3.1.0, silakan coba gunakan import com.aspose.pdf.jr3_1_0.jasperreports.; dan ganti versi produk dalam kode lainnya juga.