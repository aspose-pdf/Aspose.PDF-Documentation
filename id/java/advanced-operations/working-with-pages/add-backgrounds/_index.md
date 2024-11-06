---
title: Tambahkan latar belakang ke PDF
linktitle: Tambahkan latar belakang
type: docs
weight: 110
url: id/java/add-backgrounds/
descriptions: Tambahkan gambar latar belakang ke file PDF Anda dengan Java. Gunakan objek BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF untuk Java, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact dengan Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // Untuk contoh lengkap dan file data, silakan kunjungi
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Buat objek Document baru
        Document doc = new Document();
        // Tambahkan halaman baru ke objek dokumen
        Page page = doc.getPages().add();
        // Buat objek BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // Tentukan gambar untuk objek backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Tambahkan backgroundartifact ke koleksi artefak halaman
        page.getArtifacts().add(background);
        // Simpan dokumen
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```