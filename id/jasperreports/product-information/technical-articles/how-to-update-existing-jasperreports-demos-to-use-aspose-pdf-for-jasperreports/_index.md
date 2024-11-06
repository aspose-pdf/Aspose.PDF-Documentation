---
title: Cara - Memperbarui demo JasperReports yang ada untuk menggunakan Aspose.Pdf untuk JasperReports
type: docs
weight: 20
url: id/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF untuk JasperReports mencakup sejumlah proyek demo untuk membantu Anda memulai mengekspor laporan ke PDF. Demo ini didasarkan pada demo standar JasperReports yang telah dimodifikasi untuk menunjukkan cara menggunakan eksportir baru. Tutorial ini melalui langkah-langkah yang diperlukan untuk memperbarui demo JasperReports yang ada untuk menggunakan Aspose.PDF untuk JasperReports.

{{% /alert %}}
### **Memperbarui Demo untuk menggunakan Aspose.PDF**

{{% alert color="primary" %}}

Langkah-langkah berikut menjelaskan cara memperbarui demo yang ada untuk menggunakan ekstensi ekspor Aspose.PDF untuk JasperReports daripada menggunakan fitur ekspor PDF standar JasperReport.

1. Unduh JasperReports dari <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Pastikan untuk mengunduh seluruh proyek yang diarsipkan dengan kode sumber dan demo, bukan hanya satu JAR. 
Tutorial ini disiapkan menggunakan JasperReports-3.5.2.
2. Ekstrak proyek yang diarsipkan ke suatu lokasi di hard disk Anda, misalnya C:\.
3. Salin **aspose.pdf.jasperreports.jar** dari folder \lib dalam **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\lib.
4. Buka ```<InstallDir>```\jasperreports\demo\samples, (di mana ```<InstallDir>``` adalah lokasi Anda mengekstrak JasperReports) untuk memperbarui demo yang ada. Jika Anda telah memilih demo font, misalnya, untuk digunakan dengan Aspose.PDF untuk JasperReports, buatlah salinan dari demo tersebut agar demo asli tetap sama. Untuk tujuan contoh ini, kami menamai folder baru tersebut **fonts.ap**.
Catatan: demo akan berjalan dari ```<InstallDir>``` \jasperreports\demo\samples karena skrip build demo bergantung pada struktur folder JasperReports. Jika Anda mengubah folder sampel, Anda harus memodifikasi skrip build.
5. Buka file **FontsApp.java** dari folder src dan tambahkan referensi ke Aspose.PDF untuk JasperReports:

   import com.aspose.pdf.jr3_7_0.jasperreports.*;
``````
(We are using jr3_7_0 karena tutorial ini disiapkan dengan JasperReports 3.5.2.)
6. Tambahkan string baru:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; bersama dengan variabel yang ada sebagai opsi ekspor melalui Aspose.PDF untuk JasperReports.
7. Temukan segmen kode for else if (TASK_PDF.equals(taskName)) dan salin seluruh segmen.
8. Tempelkan potongan kode di bawah segmen yang sama.

```
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
```
```
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("Waktu pembuatan PDF : " + (System.currentTimeMillis() - start));
}
```

```
update
else if (TASK_PDF.equals(taskName))
sebagai
else if (TASK_ASPOSE_PDF.equals(taskName))
ganti
JRPdfExporter exporter = new JRPdfExporter();
dengan
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```
9. Buka file **build.xml**.
10. Buat salinan dari segmen berikut dan letakkan di dalam file yang sama:

```
<target name="pdf" description="Generat PDF via Aspose.PDF untuk JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  sebagai   name="aspose_pdf"
update  <arg value="pdf"/>  sebagai   <arg value="aspose_pdf"/>
```

11. Untuk menjalankan demo:

   -  Unduh alat ANT dari <http://ant.apache.org/bindownload.cgi>.
```

- Buka alat ANT dan atur variabel lingkungan seperti yang dijelaskan dalam manual alat tersebut.
- Ubah direktori saat ini ke <InstallDir>\demo\hsqldb dan jalankan baris perintah berikut:
  ant runServer

12. Buka instance command prompt baru dan ubah direktori saat ini ke <InstallDir>\demo\samples\fonts.ap dan jalankan perintah berikut di baris perintah:
13. ant javac – untuk mengompilasi file sumber Java dari aplikasi pengujian
14. ant compile – untuk mengompilasi desain laporan XML dan menghasilkan file .jasper
15. ant fill – untuk mengisi desain laporan yang telah dikompilasi dengan data dan menghasilkan file .jrprint
16. ant aspose_pdf – untuk menghasilkan file PDF menggunakan Aspose.PDF untuk JasperReports.
17. Buka PDF yang dihasilkan (**FontsReport.pdf**) dari folder <InstallDir>\demo\samples\fonts.ap\build\reports\.

{{% /alert %}}
```