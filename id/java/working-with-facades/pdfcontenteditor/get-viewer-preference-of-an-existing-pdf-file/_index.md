---
title: Dapatkan Preferensi Penampil dari File PDF yang Ada
type: docs
weight: 70
url: id/java/get-viewer-preference-of-an-existing-pdf-file/
description: Bagian ini menunjukkan cara bekerja dengan Aspose.PDF Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Dapatkan Preferensi Penampil dari File PDF yang Ada

Kelas [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) mewakili mode tampilan dari file PDF; misalnya, memposisikan jendela dokumen di tengah layar, menyembunyikan bilah menu aplikasi penampil, dll.

Untuk membaca pengaturan, kita menggunakan 'getViewerPreference'. Metode ini mengembalikan variabel di mana semua pengaturan disimpan.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Ubah Preferensi Penampil
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("Jendela Tengah");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Bilah menu disembunyikan");
        }
```