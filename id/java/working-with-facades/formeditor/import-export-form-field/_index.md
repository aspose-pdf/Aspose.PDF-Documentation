---
title: Impor dan Ekspor Bidang Formulir
type: docs
weight: 60
url: /id/java/import-export-form-field/
description: FormEditor memungkinkan untuk mengimpor dan mengekspor data dalam format FDF, XFDF dan XML.
lastmod: "2021-12-16"
---

Aspose.PDF untuk Java menyediakan kemampuan hebat untuk membuat/memanipulasi bidang formulir di dalam dokumen PDF. Menggunakan API ini, Anda dapat mengisi bidang formulir secara programatis di dalam file PDF dengan [Ekspor Data dari FDF ke dalam File PDF](/pdf/id/java/export-data-into-a-pdf-file-facades/), dan [Impor Data dari XFDF ke dalam File PDF](/pdf/id/java/import-data-into-a-pdf-file-facades/).

```java
public static void ImportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            editor.importFdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.fdf"));
            //editor.importXml(new FileInputStream(_dataDir + "Sample-Form-01-upd.xml"));
            //editor.importXfdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        editor.save(_dataDir + "Sample-Form-01-updated.pdf");
    }
```


## Ekspor Data dari FDF ke dalam File PDF

```java
     public static void ExportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            editor.exportFdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.fdf"));
            //editor.exportXml(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xml"));
            //editor.exportXfdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
```