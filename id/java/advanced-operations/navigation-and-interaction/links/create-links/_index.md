---
title: Buat Tautan di file PDF
linktitle: Buat Tautan
type: docs
weight: 10
url: /id/java/create-links/
description: Bagian ini menjelaskan cara membuat tautan dalam dokumen PDF Anda dengan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Buat Tautan

Aspose.PDF untuk Java memungkinkan Anda menambahkan tautan ke file PDF eksternal sehingga Anda dapat menghubungkan beberapa dokumen bersama. Dengan menambahkan tautan ke aplikasi dalam dokumen, dimungkinkan untuk menautkan ke aplikasi dari dokumen. Ini berguna ketika Anda ingin pembaca melakukan tindakan tertentu pada titik tertentu dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur. Untuk membuat tautan aplikasi:

1. [Buat Objek Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Dapatkan [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) yang ingin Anda tambahkan tautan.

1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) menggunakan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) dan [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Juga, atur ke objek [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) dan panggil metode setAction(..).
1. Saat membuat objek [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction), tentukan aplikasi yang ingin Anda luncurkan.
1. Tambahkan tautan ke koleksi [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) objek Page.
1. Terakhir, simpan PDF yang diperbarui menggunakan metode Save objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Kode berikut menunjukkan cara membuat tautan ke aplikasi dalam file PDF.

```java
package com.aspose.pdf.contoh;

import com.aspose.pdf.*;


public class ContohTautan {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Buka dokumen
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Buat tautan
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Simpan dokumen yang telah diperbarui
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Membuat Tautan Dokumen PDF dalam File PDF

Aspose.PDF untuk Java memungkinkan Anda menambahkan tautan ke file PDF eksternal sehingga Anda dapat menghubungkan beberapa dokumen bersama.
 Untuk membuat tautan dokumen PDF:

1. Pertama, buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Kemudian, dapatkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) tertentu yang ingin Anda tambahkan tautannya.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) menggunakan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) dan [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Panggil metode setAction(..) dan berikan objek [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. Saat membuat objek [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction), tentukan file PDF yang harus diluncurkan, serta nomor halaman yang harus dibuka.
1. Tambahkan tautan ke koleksi [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) objek Page.
1. Akhirnya, simpan PDF yang telah diperbarui menggunakan metode Save objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara membuat tautan dokumen PDF dalam file PDF.

```java
    public static void CreatePDFDocumentLink() {

        // Buka dokumen
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Buat tautan
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Simpan dokumen yang telah diperbarui
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```