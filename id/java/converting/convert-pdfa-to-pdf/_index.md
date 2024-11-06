---
title: Mengonversi PDF/A ke format PDF 
linktitle: Mengonversi PDF/A ke format PDF
type: docs
weight: 110
url: id/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF/A ke dokumen PDF dengan pustaka Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi dokumen PDF/A ke PDF

Mengonversi dokumen PDF/A ke PDF berarti menghapus batasan <abbr title="Portable Document Format Archive">PDF/A</abbr> dari dokumen asli. Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memiliki metode RemovePdfaCompliance(..) untuk menghapus informasi kepatuhan PDF dari file input/sumber.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Membuat objek Dokumen
    Document document = new Document(pdfaDocumentFileName);

    // Menghapus informasi kepatuhan PDF/A
    document.removePdfaCompliance();

    // Menyimpan keluaran dalam format XML
    document.save(documentFileName);
    document.close();
}
```


Info ini juga menghapus jika Anda membuat perubahan apa pun dalam dokumen (misalnya menambahkan halaman). Dalam contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Buat objek Dokumen
    Document document = new Document(pdfaDocumentFileName);

    // Menambahkan halaman baru (kosong) menghapus informasi kepatuhan PDF/A.
    document.getPages().add();

    // Simpan dokumen yang diperbarui
    document.save(documentFileName);
    document.close();
}
```