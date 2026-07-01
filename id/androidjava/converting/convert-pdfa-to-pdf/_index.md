---
title: Konversi PDF/A ke PDF
linktitle: Konversi PDF/A ke PDF
type: docs
weight: 350
url: /id/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: Untuk mengonversi PDF/A ke PDF, Anda harus menghapus pembatasan dari dokumen asli. Aspose.PDF for Android via Java memungkinkan Anda menyelesaikan masalah ini dengan mudah dan sederhana.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Mengonversi dokumen PDF/A ke PDF berarti menghapus <abbr title="Portable Document Format Archive
"<abbr>PDF/A</abbr> restriction dari dokumen asli. Kelas [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memiliki metode RemovePdfaCompliance(..) untuk menghapus
informasi kepatuhan PDF dari file input/sumber.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

Informasi ini juga akan dihapus jika Anda membuat perubahan apa pun pada dokumen (misalnya menambahkan halaman). Pada contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




