---
title: Menambahkan Bookmark ke file PDF
type: docs
weight: 20
url: /id/net/how-to-create-nested-bookmarks/
description: Bagian ini menjelaskan cara membuat Nested Bookmarks dengan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Bookmark memberi Anda opsi untuk melacak/menautkan ke halaman tertentu di dalam dokumen PDF. Kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) di [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) menyediakan fitur yang memungkinkan Anda membuat bookmark sendiri dengan cara yang canggih namun intuitif dalam file PDF yang sudah ada, di halaman tertentu atau semua halaman.

## Rincian implementasi

Selain pembuatan bookmark sederhana, terkadang Anda memiliki persyaratan untuk membuat bookmark dalam bentuk bab di mana Anda menyisipkan bookmark individu di dalam bookmark bab sehingga ketika Anda mengklik tanda + untuk sebuah bab, Anda akan melihat halaman di dalamnya ketika bookmark meluas, seperti yang ditunjukkan pada gambar di bawah ini.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("Penanda 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Menyimpan PDF hasil ke file
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```