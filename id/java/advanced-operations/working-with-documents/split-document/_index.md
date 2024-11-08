---
title: Split PDF secara programatik
linktitle: Split file PDF
type: docs
weight: 60
url: /id/java/split-document/
description: Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individual dalam aplikasi Java Anda.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Anda dapat membagi file PDF menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Topik ini menunjukkan cara membagi halaman PDF dengan Aspose.PDF untuk Java menjadi file PDF individual dalam aplikasi Java Anda. Untuk membagi halaman PDF menjadi file PDF satu halaman menggunakan Java, langkah-langkah berikut dapat diikuti:

1. Loop melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Untuk setiap iterasi, buat objek Dokumen baru dan tambahkan objek [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individu ke dalam dokumen kosong.
1. Simpan PDF baru menggunakan metode Save.

Cuplikan kode Java berikut menunjukkan cara membagi halaman PDF menjadi file PDF individu.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Loop melalui semua halaman
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```