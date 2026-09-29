---
title: Membuat PDF yang mematuhi PDF/3-A dan melampirkan faktur ZUGFeRD di Java
linktitle: Lampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /id/java/attach-zugferd/
description: Pelajari cara melampirkan XML faktur ZUGFeRD ke PDF dan mengonversinya menjadi PDF/A-3A di Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lampirkan XML faktur ZUGFeRD ke dokumen PDF dengan Java
Abstract: Artikel ini menjelaskan cara membuat dokumen faktur yang mematuhi PDF/A-3A menggunakan Aspose.PDF for Java. Artikel ini mencakup melampirkan XML faktur sebagai file tersemat, mengatur tipe MIME dan hubungan file terkait, mengonversi PDF ke PDF/A-3A, serta menyimpan dokumen akhir yang siap ZUGFeRD.
---
Gunakan `Document` dan `FileSpecification` APIs ketika Anda perlu mengemas XML faktur di dalam PDF untuk alur kerja bergaya ZUGFeRD.

## Lampirkan XML faktur ZUGFeRD ke PDF

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) untuk file faktur XML.
1. Atur metadata file tersemat, termasuk tipe MIME dan [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Tambahkan [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) ke koleksi file tersemat dokumen.
1. Konversi dokumen ke [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
