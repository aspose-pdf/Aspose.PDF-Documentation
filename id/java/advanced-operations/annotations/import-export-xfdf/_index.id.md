---
title: Impor dan Ekspor Anotasi ke format XFDF 
linktitle: Impor dan Ekspor Anotasi ke format XFDF
type: docs
weight: 40
url: /java/import-export-xfdf/
description: Anda dapat mengimpor dan mengekspor anotasi dengan format XFDF menggunakan pustaka Aspose.PDF untuk Java. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF adalah singkatan dari XML Forms Data Format. Ini adalah format file berbasis XML. Format file ini digunakan untuk merepresentasikan data formulir atau anotasi yang terdapat dalam formulir PDF. XFDF dapat digunakan untuk berbagai tujuan, tetapi dalam kasus kami, ini dapat digunakan untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, atau dapat digunakan untuk mengarsipkan data formulir atau anotasi tersebut. Dalam artikel ini, kita akan melihat bagaimana Aspose.Pdf.Facades mempertimbangkan konsep ini dan bagaimana kita dapat mengimpor dan mengekspor data anotasi ke file XFDF.

{{% /alert %}}

**Aspose.PDF untuk Java** adalah komponen yang kaya fitur ketika datang ke pengeditan dokumen PDF.
 As we know XFDF adalah aspek penting dari manipulasi formulir PDF, namespace Aspose.Pdf.Facades dalam Aspose.PDF untuk Java telah mempertimbangkan ini dengan baik, dan telah menyediakan metode untuk mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) metode menyediakan fungsi untuk mengekspor anotasi dari dokumen PDF ke file XFDF, sementara [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) metode memungkinkan Anda untuk mengimpor anotasi dari file XFDF yang sudah ada. Untuk mengimpor atau mengekspor anotasi, kita perlu menentukan jenis anotasi. Kita dapat menentukan jenis ini dalam bentuk enumerasi dan kemudian meneruskan enumerasi ini sebagai argumen ke salah satu metode ini. Dengan cara ini, anotasi dari jenis yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

Cuplikan kode berikut menunjukkan cara mengekspor anotasi ke file XFDF:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Mengimpor anotasi dari file XFDF XML Forms Data Format (XFDF)
     * dibuat oleh Adobe Acrobat, aplikasi pembuatan PDF; menyimpan deskripsi
     * elemen formulir halaman dan nilai-nilainya, seperti nama dan nilai untuk
     * bidang teks; digunakan untuk menyimpan data formulir yang dapat diimpor
     * ke dalam dokumen PDF. Anda dapat mengimpor data anotasi dari file XFDF ke PDF
     * menggunakan metode ImportAnnotationsFromXfdf di kelas PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Buat objek PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Kaitkan dokumen PDF ke Editor Anotasi
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Ekspor anotasi
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

The next code snippet describes how import annotations to an XFDF file:

```java
public static void ImportAnnotationXFDF()
{
    // Buat objek PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Buat dokumen PDF baru
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Impor anotasi
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Simpan output PDF
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Cara lain untuk mengekspor/mengimpor anotasi sekaligus

Dalam kode di bawah ini, metode ImportAnnotations memungkinkan impor anotasi langsung dari dokumen PDF lain.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Buat objek PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Buat dokumen PDF baru
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Editor Anotasi memungkinkan impor anotasi dari beberapa dokumen PDF,
        // tetapi dalam contoh ini, kita hanya menggunakan satu.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Simpan output PDF
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```