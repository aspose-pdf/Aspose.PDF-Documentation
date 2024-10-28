---
title: Impor dan Ekspor Anotasi ke XFDF 
type: docs
weight: 20
url: /net/import-export-annotations/
description: Bagian ini menjelaskan cara mengimpor dan mengekspor anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF adalah singkatan dari XML Forms Data Format. Ini adalah format file berbasis XML. Format file ini digunakan untuk merepresentasikan data formulir atau anotasi yang terdapat dalam formulir PDF. XFDF dapat digunakan untuk berbagai tujuan, tetapi dalam kasus kami, dapat digunakan untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, atau dapat digunakan untuk mengarsipkan data formulir atau anotasi. Dalam artikel ini, kita akan melihat bagaimana Aspose.Pdf.Facades mempertimbangkan konsep ini dan bagaimana kita dapat mengimpor dan mengekspor data anotasi ke file XFDF.

## Mengimpor dan Mengekspor Anotasi ke XFDF

[Aspose.PDF for .NET](/pdf/net/) adalah komponen yang kaya fitur dalam hal mengedit dokumen PDF. As we know XFDF adalah aspek penting dari manipulasi formulir PDF, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF for .NET](/pdf/net/) telah mempertimbangkan ini dengan sangat baik, dan telah menyediakan metode untuk mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) metode menyediakan fungsionalitas untuk mengekspor anotasi dari dokumen PDF ke file XFDF, sementara metode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) memungkinkan Anda untuk mengimpor anotasi dari file XFDF yang sudah ada. Untuk mengimpor atau mengekspor anotasi, kita perlu menentukan jenis anotasi. Kita dapat menentukan jenis-jenis ini dalam bentuk enumerasi dan kemudian meneruskan enumerasi ini sebagai argumen ke salah satu metode ini. Dengan cara ini, anotasi dari jenis yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengimpor anotasi ke file XFDF:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
Kode snippet berikut menjelaskan bagaimana mengimpor/mengekspor anotasi ke file XFDF:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

Dengan cara ini, anotasi dari tipe yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```