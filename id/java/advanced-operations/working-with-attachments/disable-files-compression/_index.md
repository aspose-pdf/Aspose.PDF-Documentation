---
title: Menonaktifkan Kompresi File saat Menambah sebagai Sumber Daya Tertanam
linktitle: Menonaktifkan Kompresi File
type: docs
weight: 40
url: /id/java/disable-files-compression-when-adding-as-embedded-resources/
description: Artikel ini menjelaskan cara menonaktifkan kompresi file saat Menambah sebagai Sumber Daya Tertanam
lastmod: "2021-06-05"
---

Kelas [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) memungkinkan pengembang untuk menambahkan lampiran ke dokumen PDF. Secara default, lampiran dikompresi. Kami telah memperbarui API untuk memungkinkan pengembang menonaktifkan kompresi saat menambahkan file sebagai sumber daya tertanam. Ini memberikan pengembang lebih banyak kontrol atas bagaimana file diproses.

Untuk memungkinkan pengembang mengontrol kompresi file, metode [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) telah ditambahkan ke kelas [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification).
 Properti ini menentukan encoding mana yang akan digunakan untuk kompresi file. Metode ini menerima nilai dari enumerator [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding). Nilai yang mungkin adalah [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None dan [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Jika Encoding diatur ke [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, maka lampiran tidak dikompresi. Encoding default adalah [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Cuplikan kode berikut menunjukkan cara menambahkan lampiran ke dokumen PDF.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // dapatkan referensi file sumber/masukan
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // baca semua konten dari file sumber ke dalam ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // buat instance objek Stream dari konten ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // Instansiasi objek Document dari instance stream
  Document pdfDocument = new Document(is);
  // siapkan file baru untuk ditambahkan sebagai lampiran
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Sample text file");
  // Tentukan pengaturan properti Encoding menjadi FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // tambahkan lampiran ke koleksi lampiran dokumen
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // simpan keluaran baru
  pdfDocument.save("output.pdf");
    }
```