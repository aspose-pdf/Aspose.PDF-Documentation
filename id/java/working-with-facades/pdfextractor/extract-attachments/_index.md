---
title: Extract Attachments from PDF File
type: docs
weight: 10
url: id/java/extract-attachments/
description: Bagian ini menjelaskan tentang cara mengekstrak lampiran dari pdf dengan kelas PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

Salah satu kategori utama di bawah kemampuan ekstraksi dari [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) adalah ekstraksi lampiran.
 Kategori ini menyediakan serangkaian metode, yang tidak hanya membantu mengekstrak lampiran tetapi juga menyediakan metode yang dapat memberikan informasi terkait lampiran yaitu metode [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) dan [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) memberikan informasi lampiran dan nama lampiran masing-masing. Untuk mengekstrak dan kemudian mendapatkan lampiran, kita menggunakan metode [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) dan [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--).

Cuplikan kode berikut menunjukkan cara menggunakan metode PdfExtractor:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Ekstrak lampiran
        pdfExtractor.extractAttachment();

        // Dapatkan nama lampiran
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Mengekstrak dan menyimpan...");
            // Dapatkan lampiran yang diekstrak
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```