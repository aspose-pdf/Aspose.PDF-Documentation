---
title: Membuat Dokumen PDF 
linktitle: Buat
type: docs
weight: 10
url: /java/create-document/
description: Pelajari cara membuat file PDF di Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk Java** API memungkinkan pengembang aplikasi Java untuk menyematkan fungsionalitas pemrosesan dokumen PDF dalam aplikasi mereka. Ini dapat digunakan untuk membuat dan membaca file PDF tanpa memerlukan perangkat lunak lain yang terinstal pada mesin yang mendasarinya. Aspose.PDF untuk Java dapat digunakan dalam berbagai jenis aplikasi Java seperti aplikasi Desktop, JSP, dan JSF.

## Cara membuat File PDF menggunakan Java

Untuk membuat file PDF menggunakan Java, langkah-langkah berikut dapat digunakan.

1. Membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Menambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) ke objek dokumen
1. Membuat objek [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)

1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) ke koleksi [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) dari halaman
1. Simpan dokumen PDF hasil

```java
// Inisialisasi objek dokumen
Document document = new Document();
 
// Tambahkan halaman
Page page = document.getPages().add();
 
// Tambahkan teks ke halaman baru
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Simpan PDF yang diperbarui
document.save("HelloWorld_out.pdf");
```