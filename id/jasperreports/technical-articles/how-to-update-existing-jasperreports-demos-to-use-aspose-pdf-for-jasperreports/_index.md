---
title: Cara - Memperbarui demo JasperReports yang ada untuk menggunakan Aspose.PDF for JasperReports
linktitle: How to - Update existing JasperReports demos to use Aspose.PDF for JasperReports
type: docs
weight: 20
url: /id/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Learn how to update existing JasperReports demos to leverage the capabilities of Aspose.PDF for JasperReports.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports includes a number of demo projects to help you get started exporting reports to PDF. These demos are based on standard JasperReports demos that have been modified to demonstrate how to use new exporters. This tutorial, goes through the steps required to update the existing JasperReports demos to use Aspose.PDF for JasperReports.

{{% /alert %}}

## Memperbarui Demo untuk menggunakan Aspose.PDF

{{% alert color="primary" %}}

The following steps explains how to update existing demos to use Aspose.PDF for JasperReports export extension rather than using JasperReport's standard PDF export feature.

1. Download JasperReports from <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Make sure to download the entire archived project with the source code and demos, not just a single JAR. This tutorial was prepared using JasperReports-3.5.2.
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. Salin **aspose.pdf.jasperreports.jar** dari folder \lib di **Aspose.PDF.JasperReports.zip** ke ```<InstallDir>```\jasperreports\lib.
4. Open ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` is the location you have unpacked JasperReports) to update an existing demo. If you have selected the fonts demo, for example, to use with Aspose.PDF for JasperReports, create a copy of it so that the original demo remains the same. For the purpose of this example, we have named the new folder **fonts.ap**.
Catatan: demo akan dijalankan dari ```<InstallDir>``` \jasperreports\demo\samples karena skrip pembuatan demo bergantung pada struktur folder JasperReports. Jika Anda mengubah folder sampel, Anda harus mengubah skrip build.
5. Buka file **FontsApp.java** dari folder src dan tambahkan referensi ke Aspose.PDF for JasperReports:
   impor com.aspose.pdf.jr3_7_0.jasperreports.*;
   (Kami menggunakan jr3_7_0 karena tutorial ini disiapkan dengan JasperReports 3.5.2.)
6. Tambahkan string baru:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; along with existing variables as an export option via Aspose.PDF for JasperReports.
7. Temukan segmen kode for else if (TASK_PDF.equals(taskName)) dan salin seluruh segmen.
8. Paste the code snippet under same segment.

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

11. To run the demo:
   -  Download the ANT tool from <http://ant.apache.org/bindownload.cgi>.
   - Unpack the ANT tool and set up environment variables as described in the tool's manual.
   -  Ubah direktori saat ini menjadi <InstallDir>\demo\hsqldb dan jalankan baris perintah berikut:
      ant runServer
12. Open a new command prompt instance and change the current directory to <InstallDir>\demo\samples\fonts.ap and run the following commands in the command line:
13. ant javac – to compile the Java source files of the test application
14. kompilasi semut – untuk mengkompilasi desain laporan XML dan menghasilkan file .jasper
15. ant fill – to fill the compiled report design with data and produce the .jrprint file
16. ant aspose_ pdf – to produce a PDF file using Aspose.PDF for JasperReports.
17. Buka PDF yang dihasilkan (**FontsReport.pdf**) dari folder <InstallDir>\demo\samples\ font.ap\build\reports\.

{{% /alert %}}

