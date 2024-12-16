---
title: Working with Attachments - Facades
type: docs
weight: 50
url: /id/net/working-with-attachments-facades/
description: Bagian ini menjelaskan cara bekerja dengan Attachments - Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Dalam bagian ini, kami akan menjelaskan cara bekerja dengan lampiran dalam PDF menggunakan Aspose.PDF untuk .NET Facades. Lampiran adalah file tambahan yang dilampirkan ke dokumen induk, dapat berupa berbagai jenis file, seperti pdf, word, gambar, atau file lainnya. Anda akan belajar cara menambahkan lampiran ke pdf, mendapatkan informasi dari lampiran, dan menyimpannya ke file, menghapus lampiran dari PDF secara programatis dengan C#.

## Menambahkan Lampiran dari File dalam PDF yang Ada

Anda dapat menambahkan lampiran dalam file PDF yang ada menggunakan kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Lampiran dapat ditambahkan dari file di disk menggunakan jalur file. Anda dapat menambahkan lampiran menggunakan metode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Metode ini mengambil dua argumen: jalur file dan deskripsi lampiran. Pertama, Anda perlu membuka file PDF yang ada dan menambahkan lampiran ke dalamnya. Kemudian Anda dapat menyimpan file PDF keluaran menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) dari [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara menambahkan lampiran dari sebuah file. Sebagai contoh, mari kita tambahkan file MP3.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## Menambahkan Lampiran dari Stream di PDF yang Ada

Lampiran dapat ditambahkan dalam file PDF dari stream – FileStream – menggunakan metode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Metode ini membutuhkan tiga argumen: stream, nama lampiran, dan deskripsi lampiran. Untuk menambahkan lampiran, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, Anda dapat memanggil metode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) untuk menambahkan lampiran. Terakhir, Anda dapat memanggil metode Save untuk menyimpan file PDF yang telah diperbarui. Potongan kode berikut menunjukkan bagaimana cara menambahkan lampiran dari Stream.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Hapus Semua Lampiran dari File PDF yang Ada

Metode [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk menghapus semua lampiran dari file PDF yang ada. Panggil metode [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Terakhir, Anda harus memanggil metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan kepada Anda bagaimana menghapus semua lampiran dari file PDF yang ada.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```