---
title: Cara - Memperbarui demo JasperReports yang ada untuk menggunakan Aspose.PDF for JasperReports
linktitle: How to - Update existing JasperReports demos to use Aspose.PDF for JasperReports
type: docs
weight: 20
url: /id/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Learn how to update existing JasperReports demos to leverage the capabilities of Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports menyertakan sejumlah proyek demo untuk membantu Anda memulai mengekspor laporan ke PDF. Demo ini didasarkan pada demo JasperReports standar yang telah dimodifikasi untuk menunjukkan cara menggunakan eksportir baru. Tutorial ini akan membahas langkah-langkah yang diperlukan untuk memperbarui demo JasperReports yang ada agar menggunakan Aspose.PDF for JasperReports.

{{% /alert %}}

## Memperbarui Demo untuk menggunakan Aspose.PDF

{{% alert color="primary" %}}

Langkah-langkah berikut menjelaskan cara memperbarui demo yang ada agar menggunakan ekstensi ekspor Aspose.PDF untuk JasperReports, bukan menggunakan fitur ekspor PDF standar JasperReports.

1. Unduh JasperReports dari <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
Pastikan untuk mengunduh seluruh proyek yang diarsipkan beserta kode sumber dan demo, bukan hanya satu file JAR. Tutorial ini disiapkan menggunakan JasperReports-3.5.2.
2. Ekstrak proyek yang diarsipkan ke lokasi tertentu di hard disk Anda, misalnya C:\.
3. Salin **aspose.pdf.jasperreports.jar** dari folder \lib di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\lib.
4. Buka ```<InstallDir>```\jasperreports\demo\samples, (dengan ```<InstallDir>``` adalah lokasi Anda membongkar JasperReports) untuk memperbarui demo yang ada. Jika Anda telah memilih demo font, misalnya, untuk digunakan dengan Aspose.PDF untuk JasperReports, buat salinannya sehingga demo aslinya tetap sama. Untuk tujuan contoh ini, kami memberi nama folder baru **fonts.ap**.
Catatan: demo akan dijalankan dari ```<InstallDir>``` \jasperreports\demo\samples karena skrip pembuatan demo bergantung pada struktur folder JasperReports. Jika Anda sampel mengubah folder, Anda harus mengubah skrip build.
5. Buka file **FontsApp.java** dari folder src dan tambahkan referensi ke Aspose.PDF untuk JasperReports: 
impor com.aspose.pdf.jr3_7_0.jasperreports.*; 
(Kami menggunakan jr3_7_0 karena tutorial ini disiapkan dengan JasperReports 3.5.2.)
6. Tambahkan string baru: 
String akhir statis pribadi TASK_ASPOSE_PDF = "aspose_pdf"; beserta variabel yang ada sebagai opsi ekspor melalui Aspose.PDF untuk JasperReports.
7. Temukan kode segmen untuk else if (TASK_PDF.equals(taskName)) dan salin seluruh segmen.
8. Tempelkan cuplikan kode di bawah segmen yang sama.

```java
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
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```

9. Buka file **build.xml**.
10. Buat salinan segmen berikut dan letakkan di dalam file yang sama:

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Untuk menjalankan demo:
- Unduh alat ANT dari <http://ant.apache.org/bindownload.cgi>.
- Ekstrak alat ANT dan atur variabel lingkungan seperti yang dijelaskan dalam manual alat tersebut.
- Ubah direktori saat ini menjadi <InstallDir>\demo\hsqldb dan jalankan baris perintah berikut:
ant runServer
12. Buka instance command prompt baru dan ubah direktori saat ini ke <InstallDir>\demo\samples\fonts.ap dan jalankan perintah berikut di baris perintah:
13. `ant javac` – untuk mengkompilasi file sumber Java dari aplikasi pengujian.
14. `ant compile` – untuk mengkompilasi desain laporan XML dan menghasilkan file `.jasper`.
15. `ant fill` – untuk mengisi desain laporan yang dikompilasi dengan data dan menghasilkan file `.jrprint`.
16. `ant aspose_pdf` – untuk menghasilkan file PDF menggunakan Aspose.PDF for JasperReports.
17. Buka PDF yang dihasilkan (**FontsReport.pdf**) dari folder `<InstallDir>\demo\samples\fonts.ap\build\reports\`.

{{% /alert %}}

