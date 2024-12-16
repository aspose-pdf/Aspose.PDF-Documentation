---
title: Membagi PDF secara programatik
linktitle: Membagi file PDF
type: docs
weight: 60
url: /id/php-java/split-document/
description: Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individual dalam aplikasi PHP Anda.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Anda dapat membagi file PDF menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Topik ini menunjukkan cara membagi halaman PDF dengan Aspose.PDF untuk PHP via Java menjadi file PDF individual dalam aplikasi PHP Anda. Untuk membagi halaman PDF menjadi file PDF satu halaman menggunakan PHP, langkah-langkah berikut dapat diikuti:

1. Melakukan loop melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Untuk setiap iterasi, buat objek Dokumen baru dan tambahkan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individual ke dalam dokumen kosong.
2. Simpan PDF baru menggunakan metode Save.

Potongan kode PHP berikut menunjukkan cara membagi halaman PDF menjadi file PDF individual.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Loop melalui semua halaman
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```