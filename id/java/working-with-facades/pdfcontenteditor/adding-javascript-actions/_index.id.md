---
title: Menambahkan aksi Javascript ke file PDF yang ada
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: Bagian ini menjelaskan cara menambahkan aksi Javascript ke file PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) yang terdapat di bawah paket com.aspose.pdf.facades menyediakan fleksibilitas untuk menambahkan aksi Javascript ke file PDF. Anda dapat membuat tautan dengan aksi serial yang sesuai untuk menjalankan item menu di penampil PDF. Kelas ini juga menyediakan fitur untuk membuat aksi tambahan untuk peristiwa dokumen.

Pertama-tama, sebuah objek digambar dalam [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), dalam contoh kami sebuah [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 Dan atur tindakan [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) ke Rectangle. Setelah itu, Anda dapat menyimpan dokumen Anda.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // buat tautan Javascript
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Selamat datang di Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // simpan file output
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```