---
title: "Menambahkan lampiran ke PDF dalam Java"
linktitle: "Menambahkan lampiran ke dokumen PDF"
type: docs
weight: 10
url: /id/java/add-attachment-to-pdf-document/
description: Pelajari cara menambahkan lampiran file ke dokumen PDF dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan file yang disematkan ke dokumen PDF dengan Java"
Abstract: Artikel ini menunjukkan cara melampirkan file eksternal ke dokumen PDF menggunakan Aspose.PDF for Java. Contoh ini membuka PDF yang ada, membuat FileSpecification untuk lampiran, menambahkannya ke koleksi EmbeddedFiles dokumen, dan menyimpan file yang diperbarui.
---
Untuk melampirkan file ke PDF, muat dokumen sumber, buat sebuah `FileSpecification`, tambahkan ke koleksi file tertanam, dan simpan hasilnya.

## Menambahkan lampiran ke dokumen PDF

Gunakan contoh ini ketika file eksternal harus disisipkan ke dalam PDF yang ada.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`FileSpecification`](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) untuk file yang ingin Anda sematkan.
1. Tambahkan spesifikasi berkas ke `EmbeddedFiles` Kumpulkan dan simpan dokumen yang diperbarui.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
