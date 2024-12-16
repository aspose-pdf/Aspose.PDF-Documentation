---
title: Mendapatkan Preferensi Penampil dari Berkas PDF
type: docs
weight: 70
url: /id/net/get-viewer-preference-of-an-existing-pdf-file/
description: Bagian ini menunjukkan cara mendapatkan preferensi penampil dari berkas PDF yang ada menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Mendapatkan Preferensi Penampil dari Berkas PDF yang Ada

Kelas [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) mewakili mode tampilan berkas PDF; misalnya, memposisikan jendela dokumen di tengah layar, menyembunyikan menu bar aplikasi penampil, dll.

Untuk membaca pengaturan tersebut kita menggunakan kelas [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Metode ini mengembalikan variabel di mana semua pengaturan disimpan.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Ubah Preferensi Penampil
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```