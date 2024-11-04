---
title: Setel Preferensi Penampil dari File PDF yang Ada
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: Bagian ini menunjukkan cara bekerja dengan Aspose.PDF Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Setel Preferensi Penampil dari File PDF yang Ada

Kelas [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) mewakili mode tampilan file PDF; misalnya, memposisikan jendela dokumen di tengah layar, menyembunyikan bilah menu aplikasi penampil, dll.

Metode [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) dalam kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) memungkinkan Anda mengubah preferensi penampil.
 Untuk melakukan itu, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) dan mengikat file PDF input menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

Setelah itu, Anda dapat memanggil metode [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) untuk mengatur preferensi apa pun. Terakhir, Anda harus menyimpan file PDF yang telah diperbarui menggunakan metode Save. Cuplikan kode berikut menunjukkan cara mengubah preferensi penampil dalam file PDF yang ada.

Sebagai contoh, kami menentukan parameter [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) yang dengan itu kami memusatkan jendela, setelah menghapus bilah alat atas dengan [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) dan dengan [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) membuka mode layar penuh.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Ubah Preferensi Penampil
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```