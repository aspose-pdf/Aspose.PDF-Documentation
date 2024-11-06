---
title: Mengekstraksi teks mentah dari file PDF 
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: id/androidjava/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF untuk Android melalui Java. Dari seluruh halaman, dari bagian tertentu, berdasarkan kolom, dll.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstraksi teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF untuk Java memungkinkan mengekstrak teks dari semua halaman dokumen PDF.
Untuk mengekstrak teks dari semua halaman PDF:

1. Buat objek dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Buka PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan panggil metode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) dari koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
2. Kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) menyerap teks dari dokumen dan mengembalikannya dalam properti **Text**.

Cuplikan kode berikut menunjukkan kepada Anda cara mengekstrak teks dari semua halaman dokumen PDF.

```java
public static void ExtractFromAllPages() {
        // Jalur ke direktori dokumen.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Buka dokumen
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Buat objek TextAbsorber untuk mengekstrak teks
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Terima absorber untuk semua halaman
        pdfDocument.getPages().accept(textAbsorber);

        // Dapatkan teks yang diekstraksi
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Tulis satu baris teks ke file
            writer.write(extractedText);
            // Tutup aliran
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## Ekstrak Teks yang Disorot dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda dapat memiliki kebutuhan untuk mengekstrak hanya teks yang disorot dari dokumen PDF. Untuk mengimplementasikan fungsionalitas ini, kami telah menambahkan metode TextMarkupAnnotation.GetMarkedText() dan TextMarkupAnnotation.GetMarkedTextFragments() dalam API. Anda dapat mengekstrak teks yang disorot dari dokumen PDF dengan memfilter TextMarkupAnnotation dan menggunakan metode yang disebutkan. Cuplikan kode berikut menunjukkan bagaimana Anda dapat mengekstrak teks yang disorot dari dokumen PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Melakukan loop melalui semua anotasi
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Memfilter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Mengambil fragmen teks yang disorot
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Menampilkan teks yang disorot
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## Mengakses Elemen Fragmen Teks dan Segmen dari XML

Terkadang kita perlu mengakses item TextFragment atau TextSegment saat memproses dokumen PDF yang dihasilkan dari XML. Aspose.PDF untuk Android melalui Java menyediakan akses ke item tersebut berdasarkan nama. Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }