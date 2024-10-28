---
title: Menambahkan Aksi Javascript PDF 
type: docs
weight: 10
url: /net/adding-javascript-actions/
description: Bagian ini menjelaskan bagaimana menambahkan aksi Javascript ke file PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) yang terdapat dalam paket Aspose.Pdf.Facades memberikan fleksibilitas untuk menambahkan aksi Javascript ke file PDF. Anda dapat membuat tautan dengan aksi serial yang sesuai untuk mengeksekusi item menu di penampil PDF. Kelas ini juga menyediakan fitur untuk membuat aksi tambahan untuk kejadian dokumen.

Pertama-tama, sebuah objek digambar dalam [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), dalam contoh kami sebuah [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). Dan tetapkan aksi [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) ke Rectangle. Setelah itu, Anda dapat menyimpan dokumen Anda.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // buat tautan Javascript
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Welcome to Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // simpan file keluaran
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```