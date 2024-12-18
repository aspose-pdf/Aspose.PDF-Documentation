---
title: Setel Preferensi Penampil PDF
type: docs
weight: 60
url: /id/net/set-viewer-preference-of-an-existing-pdf-file/
description: Bagian ini menunjukkan cara menyetel preferensi penampil dari file PDF yang ada menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Setel Preferensi Penampil dari File PDF yang Ada

Kelas [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) mewakili mode tampilan dari file PDF; misalnya, memposisikan jendela dokumen di tengah layar, menyembunyikan bilah menu aplikasi penampil, dll.

Metode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) dalam kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk mengubah preferensi penampil. Untuk melakukan itu, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Setelah itu, Anda dapat memanggil metode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) untuk mengatur preferensi apa pun. Akhirnya, Anda harus menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). Cuplikan kode berikut menunjukkan kepada Anda cara mengubah preferensi penampil dalam file PDF yang ada.

Sebagai contoh, kami menentukan parameter [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) yang dengannya kami memusatkan jendela, setelah menghapus toolbar atas dengan [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) dan dengan [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) membuka mode layar penuh.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Ubah Preferensi Penampil
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Menyimpan hasil PDF ke file
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```