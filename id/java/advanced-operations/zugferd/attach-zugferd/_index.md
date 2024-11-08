---
title: Membuat PDF yang sesuai dengan PDF/3-A dan melampirkan faktur ZUGFeRD di Java
linktitle: Lampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /id/java/attach-zugferd/
description: Pelajari cara membuat dokumen PDF dengan ZUGFeRD di Aspose.PDF untuk Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Lampirkan ZUGFeRD ke PDF

Kami merekomendasikan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

* Tentukan variabel jalur yang menunjuk ke folder tempat file PDF input dan output berada.
* Tentukan variabel string path yang menyimpan jalur ke file PDF yang akan diproses. Gunakan metode `Paths.get` untuk menggabungkan bagian-bagian dari jalur lengkap.
* Buat pernyataan try-with-resources yang memastikan bahwa objek Document yang dibuat dari variabel jalur akan ditutup secara otomatis setelah pernyataan berakhir. Objek Document mewakili dokumen PDF yang akan dimodifikasi dan disimpan.

* Buat objek [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) dengan menyediakan jalur dan deskripsi file lain, yang berisi metadata faktur yang sesuai dengan standar ZUGFeRD.
 * Tambahkan properti ke objek spesifikasi file, seperti deskripsi, jenis MIME, dan AFrelationship. AFrelationship menunjukkan bagaimana file yang disematkan terkait dengan dokumen PDF. Dalam hal ini, diatur ke "Alternative", yang berarti file yang disematkan adalah representasi alternatif dari konten PDF.
* Tambahkan objek spesifikasi file ke koleksi file yang disematkan dalam dokumen. Nama file harus ditentukan sesuai standar ZUGFeRD, misalnya "factor-x.xml".
* Konversikan dokumen ke format PDF/A-3U, subset dari PDF yang memastikan pelestarian jangka panjang dokumen elektronik. PDF/A-3U memungkinkan penyematan file dalam format apa pun ke dalam dokumen PDF.
* Simpan dokumen yang telah dikonversi sebagai file PDF baru (misalnya "ZUGFeRD-res.pdf").
* Tutup pernyataan try-with-resources dan lepaskan objek Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Metadata faktur sesuai dengan standar ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Tambahkan lampiran ke koleksi lampiran dokumen
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```