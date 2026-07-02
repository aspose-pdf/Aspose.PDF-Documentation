---
title: Mengekstrak teks mentah dari file PDF
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: /id/androidjava/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Android via Java. Dari seluruh halaman, dari bagian tertentu, berdasarkan kolom, dll.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF for Java memungkinkan mengekstrak teks dari semua halaman dokumen PDF.
Untuk mengekstrak teks dari semua halaman PDF:

1. Buat sebuah objek dari [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) kelas.
1. Buka PDF menggunakan [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) kelas dan panggil [Terima](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) metode dari [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) koleksi.
1. The [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) kelas menyerap teks dari dokumen dan mengembalikannya dalam properti **Text** property.

Potongan kode berikut menunjukkan cara mengekstrak teks dari semua halaman dokumen PDF.

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## Ekstrak Teks yang disorot dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda mungkin memiliki kebutuhan untuk mengekstrak hanya teks yang disorot dari dokumen PDF. Untuk mengimplementasikan fungsionalitas ini, kami telah menambahkan metode TextMarkupAnnotation.GetMarkedText() dan TextMarkupAnnotation.GetMarkedTextFragments() dalam API. Anda dapat mengekstrak teks yang disorot dari dokumen PDF dengan menyaring TextMarkupAnnotation dan menggunakan metode yang disebutkan. Potongan kode berikut menunjukkan cara mengekstrak teks yang disorot dari dokumen PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## Akses Text Fragment dan Segment Elements dari XML

Kadang‑kadang kita perlu mengakses item TextFragement atau TextSegment saat memproses dokumen PDF yang dihasilkan dari XML. Aspose.PDF for Android via Java menyediakan akses ke item tersebut dengan nama. Potongan kode di bawah ini menunjukkan cara menggunakan fungsi ini.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

