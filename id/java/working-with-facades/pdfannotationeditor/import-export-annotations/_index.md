---
title: Impor dan Ekspor Anotasi ke format XFDF menggunakan com.aspose.pdf.facades
type: docs
weight: 20
url: /id/java/import-export-annotations/
description: Bagian ini menjelaskan cara mengekspor dan mengimpor anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF adalah singkatan dari XML Forms Data Format. Ini adalah format file berbasis XML. Format file ini digunakan untuk mewakili data formulir atau anotasi yang terkandung dalam formulir PDF. XFDF dapat digunakan untuk berbagai tujuan, tetapi dalam kasus kami, ini dapat digunakan untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, atau dapat digunakan untuk mengarsipkan data formulir atau anotasi. Dalam artikel ini, kita akan melihat bagaimana Aspose.Pdf.Facades mempertimbangkan konsep ini dan bagaimana kita dapat mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) metode menyediakan fungsi untuk mengekspor anotasi dari dokumen PDF ke file XFDF, sementara metode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) memungkinkan Anda untuk mengimpor anotasi dari file XFDF yang sudah ada. Untuk mengimpor atau mengekspor anotasi, kita perlu menentukan jenis anotasi. Kita dapat menentukan jenis ini dalam bentuk enumerasi dan kemudian melewatkan enumerasi ini sebagai argumen ke salah satu metode tersebut.

Cuplikan kode berikut menunjukkan bagaimana mengimpor anotasi ke file XFDF:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

Cuplikan kode berikut menjelaskan cara impor/ekspor anotasi ke file XFDF:

```java
    public static void ImportExportXFDF01() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;
        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            annotationEditor.exportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document document = new Document();
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```

Dengan cara ini, anotasi dari jenis yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

```java
    public static void ImportExportXFDF02() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;

        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            int[] annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.exportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.close();
        } catch (IOException e) {            
            e.printStackTrace();
        }

        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```