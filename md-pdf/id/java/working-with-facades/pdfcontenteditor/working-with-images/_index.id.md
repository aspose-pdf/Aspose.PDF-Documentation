---
title: Bekerja dengan Gambar
type: docs
weight: 30
url: /java/working-with-image/
description: Bagian ini menjelaskan cara mengganti gambar dengan Aspose.PDF Facades - seperangkat alat untuk operasi populer dengan PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hapus Gambar dari Halaman Tertentu PDF (Facades)

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) memungkinkan Anda untuk mengganti gambar dalam file PDF yang sudah ada.
 The [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method membantu Anda mencapai tujuan ini. Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) dan mengikat file PDF input menggunakan metode bindPdf. Setelah itu, Anda perlu memanggil metode [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) dengan tiga parameter: nomor halaman, indeks gambar yang akan diganti, dan jalur gambar yang akan diganti.

Cuplikan kode berikut menunjukkan cara mengganti gambar dalam file PDF yang ada.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Hapus Semua Gambar dari File PDF (Fasad)

Semua gambar dapat dihapus dari file PDF menggunakan metode [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) dari [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Panggil metode [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – overload tanpa parameter – untuk menghapus semua gambar, dan kemudian simpan file PDF yang telah diperbarui menggunakan metode Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Ganti Gambar dalam File PDF (Fasad)

Anda dapat mengganti gambar dalam file PDF menggunakan metode [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) dari [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // Mengganti gambar pada halaman kedua dengan gambar baru
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```