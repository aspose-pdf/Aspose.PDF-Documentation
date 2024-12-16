---
title: Mengubah PDF/A ke PDF 
linktitle: Mengubah PDF/A ke PDF
type: docs
weight: 350
url: /id/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: Untuk mengubah PDF/A ke PDF, Anda harus menghapus batasan dari dokumen asli. Aspose.PDF untuk Android via Java memungkinkan Anda untuk menyelesaikan masalah ini dengan mudah dan sederhana.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Mengubah dokumen PDF/A ke PDF berarti menghapus batasan <abbr title="Portable Document Format Archive">PDF/A</abbr> dari dokumen asli. Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memiliki metode RemovePdfaCompliance(..) untuk menghapus informasi kepatuhan PDF dari file input/sumber.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Membuat objek Document
            document = new Document(pdfaDocumentFileName);

            // Menghapus informasi kepatuhan PDF/A
            document.removePdfaCompliance();

            // Menyimpan output dalam format XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


Dokumen ini juga menghapus jika Anda membuat perubahan apa pun pada dokumen (misalnya menambahkan halaman). Dalam contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Membuat objek Dokumen
        document = new Document(pdfaDocumentFileName);

        // Menambahkan halaman baru (kosong) menghapus informasi kepatuhan PDF/A.
        document.getPages().add();

        // Menyimpan dokumen yang diperbarui
        document.save(pdfDocumentFileName);
    }
```