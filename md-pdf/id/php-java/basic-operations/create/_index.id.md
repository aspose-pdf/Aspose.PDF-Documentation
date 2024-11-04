---
title: Membuat Dokumen PDF 
linktitle: Buat
type: docs
weight: 10
url: /php-java/create-document/
description: Pelajari cara membuat file PDF di Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk PHP via Java** API memungkinkan pengembang aplikasi untuk menyematkan fungsionalitas pemrosesan dokumen PDF dalam aplikasi mereka. Ini dapat digunakan untuk membuat dan membaca file PDF tanpa memerlukan perangkat lunak lain yang terinstal pada mesin yang digunakan. Aspose.PDF untuk PHP via Java dapat digunakan dalam berbagai jenis aplikasi seperti aplikasi Desktop, JSP, dan JSF.

## Cara membuat File PDF menggunakan PHP via Java

Untuk membuat file PDF menggunakan PHP via Java, langkah-langkah berikut dapat digunakan.

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) ke objek dokumen

1. Buat objek [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) ke koleksi [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) dari halaman
1. Simpan dokumen PDF yang dihasilkan

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```